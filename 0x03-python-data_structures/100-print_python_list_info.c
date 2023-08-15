#include <Python.h>

/**
 * print_python_list_info - this function gets the basic info of a python list
 * @p: this is the pointer to the python list type
 */
void print_python_list_info(PyObject *p)
{
	int python_size;
	int alloc, l;
	PyObject *obj;

	python_size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", python_size);
	printf("[*] Allocated = %d\n", alloc);
	for (l = 0; l < python_size; l++)
	{
		printf("Element %d: ", l);
		obj = PyList_GetItem(p, l);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
