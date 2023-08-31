#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - this function prints info about python list
 * @p: pointer to the python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t alloc;
	Py_ssize_t i, size;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyListObject *var = (PyListObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf(" [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - this prints bytes info
 * @p: pointer to the bytes location
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	Py_ssize_t size = var->ob_size;
	char *str = PyBytes_AsString(p);

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  address of raw bytes: %p\n", (void *)str);
}

/**
 * print_python_float - prints float
 * @p: pointer to float
 */
void print_python_float(PyObject *p)
{
	double value = PyFloat_AsDouble(p);

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf(" [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: %lf\n", value);
}
