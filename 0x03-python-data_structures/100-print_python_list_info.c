#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

int main(void) {
    PyObject *pList;
    PyObject *pValue;

    Py_Initialize();
    pList = PyList_New(0);

    pValue = PyLong_FromLong(1);
    PyList_Append(pList, pValue);
    Py_DECREF(pValue);

    pValue = PyBytes_FromString("Python");
    PyList_Append(pList, pValue);
    Py_DECREF(pValue);

    pValue = PyFloat_FromDouble(3.14);
    PyList_Append(pList, pValue);
    Py_DECREF(pValue);

    print_python_list_info(pList);

    Py_DECREF(pList);

    return 0;
}
