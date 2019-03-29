# include "Python.h"

static PyMethodDef CAPIMethods[] =  {
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef CAPIModule = {
    PyModuleDef_HEAD_INIT, "pycapi", NULL, -1, CAPIMethods,
};

PyObject* PyInit_pycapi(void) {
    return PyModule_Create(&CAPIModule);
}
