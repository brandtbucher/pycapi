<div align=justify>

<div align=center>

- - -

PyCAPI is still in an early development stage.<br>It is incomplete, and may contain bugs in the interface between the Python and C layers.<br>If so, please report them here!

**PyCAPI is nothing more than a thin wrapper around the _actual_ underlying CPython C API.<br>As when using C or `ctypes`, there is the potential to break things if you don't know what you're doing!**

- - -

PyCAPI `0.3.0`
==============

</div>

PyCAPI is a Python package containing bindings to the CPython C API. Its goal is to support as much of the Python 3.5 - 3.8 stable public APIs as possible.

To install, just run:
```sh
$ pip install pycapi
```

Where is the documentation?
---------------------------

Documentation of the full CPython C API can be found [here](https://docs.python.org/3/c-api/index.html). It's not a goal of this project to maintain a separate API reference.

Any type conversions (such as Python `int` with C `int`, Python `bytes` with C `char*`, or Python `None` with C `NULL`) should be obvious, and all other semantics (such as refcounts, etc.) are identical to the documented API behavior. For simplicity, PyCAPI doesn't provide any additional functionality or utilities beyond CPython's documented stable public API.

How is PyCAPI better than `ctypes.pythonapi`?
---------------------------------------------

### It's easier to use.

`pythonapi` implicity requires users to specify the argument and return types as `ctypes` types:

```py
>>> import ctypes
>>> ctypes.pythonapi.PyNumber_Add(1, 2)
Segmentation fault: 11
```

```py
>>> import ctypes
>>> ctypes.pythonapi.PyNumber_Add.argtypes = (ctypes.py_object, ctypes.py_object)
>>> ctypes.pythonapi.PyNumber_Add.restype = ctypes.py_object
>>> ctypes.pythonapi.PyNumber_Add(1, 2)
3
```

### It's more complete.

Because `pythonapi` is based on a DLL, it doesn't offer any APIs that are implemented as macros:

```py
>>> ctypes.pythonapi.PyDict_Check(ctypes.py_object(d))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ctypes/__init__.py", line 369, in __getattr__
    func = self.__getitem__(name)
  File "/usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ctypes/__init__.py", line 374, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: dlsym(RTLD_DEFAULT, PyDict_Check): symbol not found
```

`pycapi` is also fully loaded on import, so you can use tab-completion and other introspection techniques to discover APIs. `pythonapi` requires you to access the attribute _before_ it is loaded, and there is no way to get a complete listing of what it supports.

### It's faster.

The numbers speak for themselves:

```py
In [1]: d = {}

In [2]: from pycapi import PyDict_Clear

In [3]: %timeit PyDict_Clear(d)
45.7 ns ± 0.189 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

```py
In [1]: d = {}

In [2]: PyDict_Clear = dict.clear

In [3]: %timeit PyDict_Clear(d)
50 ns ± 1.75 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

```py
In [1]: d = {}

In [2]: import ctypes
   ...: PyDict_Clear = ctypes.pythonapi.PyDict_Clear
   ...: PyDict_Clear.argtypes = (ctypes.py_object,)
   ...: PyDict_Clear.restype = None

In [3]: %timeit PyDict_Clear(d)
293 ns ± 4.41 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

</div>
