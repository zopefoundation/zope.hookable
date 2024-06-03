/*############################################################################
 #
 #  Copyright (c) 2003 Zope Foundation and Contributors.
 #  All Rights Reserved.
 #
 #  This software is subject to the provisions of the Zope Public License,
 #  Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
 #  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
 #  WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 #  WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
 #  FOR A PARTICULAR PURPOSE.
 #
 ############################################################################*/

static char module__doc__[] = (
    "Provide an efficient implementation for hookable objects"
);

#include "Python.h"
#include "structmember.h"

typedef struct
{
    PyObject_HEAD
    PyObject* original;
    PyObject* implementation;
} hookable;

static int
hookable_init(hookable* self, PyObject* args, PyObject* kwds)
{
    static char* kwlist[] = { "implementation", NULL };
    PyObject* implementation;

    if (!PyArg_ParseTupleAndKeywords(
          args, kwds, "O:hookable", kwlist, &implementation))
        return -1;

    /* Both 'self->original' and 'self->implementation' are originally
     * set to the passed-in 'implementation', hence the need for
     * two increfs.
     */
    Py_INCREF(implementation);
    Py_XDECREF(self->original);
    self->original = implementation;

    Py_INCREF(implementation);
    Py_XDECREF(self->implementation);
    self->implementation = implementation;

    return 0;
}

static int
hookable_traverse(hookable* self, visitproc visit, void* arg)
{
#if PY_VERSION_HEX >= 0x03090000
    Py_VISIT(Py_TYPE(self));
#endif
    Py_VISIT(self->implementation);
    Py_VISIT(self->original);
    return 0;
}

static int
hookable_clear(hookable* self)
{
    Py_XDECREF(self->original);
    self->original = NULL;

    Py_XDECREF(self->implementation);
    self->implementation = NULL;

    return 0;
}

static void
hookable_dealloc(hookable* self)
{
    PyObject_GC_UnTrack((PyObject*)self);
    PyTypeObject* tp = Py_TYPE(self);

    Py_XDECREF(self->original);
    Py_XDECREF(self->implementation);

    tp->tp_free((PyObject*)self);

    /* heap types must decref their type when dealloc'ed */
    Py_DECREF(tp);
}

static PyObject*
hookable_call(hookable* self, PyObject* args, PyObject* kw)
{
    if (self->implementation != NULL)
        return PyObject_Call(self->implementation, args, kw);

    PyErr_SetString(PyExc_TypeError, "Hookable has no implementation");
    return NULL;
}

static PyObject*
hookable_getattro(hookable* self, PyObject* name)
{
    PyObject* result = NULL;
    const char* name_as_string;
    int maybe_special_name;

    name_as_string = PyUnicode_AsUTF8(name);
    if (name_as_string == NULL) { return NULL; }

    maybe_special_name = name_as_string[0] == '_' && name_as_string[1] == '_';

    if (maybe_special_name) {
        /* pass through __doc__ to the original implementation */
        if (strcmp("__doc__", name_as_string) == 0) {
            return PyObject_GetAttr(self->original, name);
        }
        /* synthesize __bases__ and __dict__ if the original fails */
        if (strcmp("__bases__", name_as_string) == 0) {
            result = PyObject_GetAttr(self->original, name);
            if (result == NULL) {
                PyErr_Clear();
                result = PyTuple_New(0);
            }
            return result;
        }
        if (strcmp("__dict__", name_as_string) == 0) {
            result = PyObject_GetAttr(self->original, name);
            if (result == NULL) {
                PyErr_Clear();
                result = PyDict_New();
            }
            return result;
        }
    }

    return PyObject_GenericGetAttr((PyObject*)self, name);
}

static char hookable_sethook__doc__[] = (
    "Set the hook implementation for the hookable object\n\n"
    "Return the previous hook implementation, or None."
);

static PyObject*
hookable_sethook(hookable* self, PyObject* implementation)
{
    PyObject* current;

    current = self->implementation;
    Py_INCREF(implementation);
    self->implementation = implementation;

    if (current == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    return current;
}

static char hookable_reset__doc__[] = (
    "Reset the hook to the original value"
);

static PyObject*
hookable_reset(hookable* self)
{
    Py_XINCREF(self->original);
    Py_XDECREF(self->implementation);

    self->implementation = self->original;

    Py_INCREF(Py_None);
    return Py_None;
}

static struct PyMethodDef hookable_methods[] = {
    { "sethook",
        (PyCFunction)hookable_sethook, METH_O, hookable_sethook__doc__ },
    { "reset",
        (PyCFunction)hookable_reset, METH_NOARGS, hookable_reset__doc__},
    { NULL, NULL } /* sentinel */
};

static PyMemberDef hookable_members[] = {
    { "original",
        T_OBJECT_EX, offsetof(hookable, original), READONLY },
    { "implementation",
        T_OBJECT_EX, offsetof(hookable, implementation), READONLY },
    { NULL } /* Sentinel */
};

static char hookable__name__[] = "zope.hookable.hookable";
static char hookable__doc__[] =
  "Callable objects that support being overridden";


/*
 * Heap type: hookable
 */
static PyType_Slot hookable_type_slots[] = {
    {Py_tp_doc,         hookable__doc__},
    {Py_tp_init,        hookable_init},
    {Py_tp_call,        hookable_call},
    {Py_tp_getattro,    hookable_getattro},
    {Py_tp_traverse,    hookable_traverse},
    {Py_tp_clear,       hookable_clear},
    {Py_tp_dealloc,     hookable_dealloc},
    {Py_tp_members,     hookable_members},
    {Py_tp_methods,     hookable_methods},
    {0,                 NULL}
};

static PyType_Spec hookable_type_spec = {
    .name       = hookable__name__,
    .basicsize  = sizeof(hookable),
    .flags      = Py_TPFLAGS_DEFAULT |
                  Py_TPFLAGS_BASETYPE |
#if PY_VERSION_HEX >= 0x030c0000
                  Py_TPFLAGS_MANAGED_WEAKREF |
#endif
                  Py_TPFLAGS_HAVE_GC,
    .slots      = hookable_type_slots
};

/*
 * Module initialization
 */

static struct PyMethodDef hookable_module_methods[] = {
    { NULL, NULL }  /* sentinel */
};


/* Handler for the 'execute' phase of multi-phase initialization
 *
 * See: https://docs.python.org/3/c-api/module.html#multi-phase-initialization
 * and: https://peps.python.org/pep-0489/#module-execution-phase
 */
static int
hookable_module_exec(PyObject* module)
{
    PyObject* hookable_type;

    hookable_type = PyType_FromSpec(&hookable_type_spec);
    if (hookable_type == NULL) { return -1; }

    if (PyModule_AddObject(module, "hookable", hookable_type) < 0)
        return -1;

    return 0;
}


/* Slot definitions for multi-phase initialization
 *
 * See: https://docs.python.org/3/c-api/module.html#multi-phase-initialization
 * and: https://peps.python.org/pep-0489
 */
static PyModuleDef_Slot hookable_module_slots[] = {
    {Py_mod_exec,       hookable_module_exec},
    {0,                 NULL}
};

static struct PyModuleDef hookable_module_def = {
    PyModuleDef_HEAD_INIT,
    .m_name     = "_zope_hookable",
    .m_doc      = module__doc__,
    .m_methods  = hookable_module_methods,
    .m_slots    = hookable_module_slots
};

static PyObject*
init(void)
{
    return PyModuleDef_Init(&hookable_module_def);
}

PyMODINIT_FUNC
PyInit__zope_hookable(void)
{
    return init();
}
