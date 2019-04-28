<div align=justify>

<div align=center>

PyCAPI
======

[![latest version](https://img.shields.io/github/release-pre/brandtbucher/pycapi.svg?style=for-the-badge&label=latest)](https://pypi.org/project/pycapi/)[![latest release date](https://img.shields.io/github/release-date-pre/brandtbucher/pycapi.svg?style=for-the-badge&label=released)](https://github.com/brandtbucher/pycapi/releases)[![build status](https://img.shields.io/travis/com/brandtbucher/pycapi/master.svg?style=for-the-badge)](https://travis-ci.com/brandtbucher/pycapi)[![issues](https://img.shields.io/github/issues-raw/brandtbucher/pycapi.svg?label=issues&style=for-the-badge)](https://github.com/brandtbucher/pycapi/issues)

<br>

</div>

PyCAPI is a Python package containing over 400 fast bindings to the CPython C API. Its goal is to support as much of the Python 3.5 - 3.8 stable public APIs as possible.

To install, just run:
```sh
$ pip install pycapi
```

Where is the documentation?
---------------------------

Documentation of the full CPython C API can be found [here](https://docs.python.org/3/c-api/index.html). It's not a goal of this project to maintain a separate API reference.

Any type conversions (such as Python `int` with C `long`, or Python `bytes` with C `char*`) should be obvious, and all other semantics (such as refcounts, etc.) are identical to the documented API behavior. For simplicity, PyCAPI doesn't provide any additional functionality or utilities beyond CPython's documented stable public API.

How is PyCAPI better than `ctypes.pythonapi`?
---------------------------------------------

### It's easier to use.

`pycapi` works as expected, right out of the box:

```py
>>> import pycapi
>>> pycapi.PyNumber_Add(1, 2)
3
```

`ctypes.pythonapi` implicity requires users to specify the argument and return types as `ctypes` types:

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

`pycapi` is designed to provide properly typed bindings for *any* part of the C API that's reasonable to call from the Python layer:

```py
>>> import pycapi
>>> pycapi.PyDict_Check({})
1
```

In comparison, `ctypes.pythonapi` is loaded directly from the `Python.h` DLL. As a consequence, it isn't able to offer any APIs that happen to be implemented as macros:

```py
>>> import ctypes
>>> ctypes.pythonapi.PyDict_Check(ctypes.py_object({}))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ctypes/__init__.py", line 369, in __getattr__
    func = self.__getitem__(name)
  File "/usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ctypes/__init__.py", line 374, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: dlsym(RTLD_DEFAULT, PyDict_Check): symbol not found
```

`pycapi` is also fully loaded on import, so you can use tab-completion and other introspection techniques to discover APIs. `ctypes.pythonapi` requires you to access the attribute *before* it is loaded, and there is no way to get a complete listing of what it supports.

### It's faster.

In many cases, it can be even *faster than the built-in equivalent* in the Python layer. The numbers speak for themselves:

```py
In [1]: from pycapi import PyDict_New, PyDict_Clear, PyDict_Copy

In [2]: %timeit PyDict_New()
44.7 ns ± 1.38 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [3]: %timeit PyDict_Clear({})
54 ns ± 0.448 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [4]: %timeit PyDict_Copy({})
68.9 ns ± 0.362 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

```py
In [1]: PyDict_New = dict
   ...: PyDict_Clear = dict.clear
   ...: PyDict_Copy = dict.copy

In [2]: %timeit PyDict_New()
71.7 ns ± 0.569 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [3]: %timeit PyDict_Clear({})
55.8 ns ± 0.506 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [4]: %timeit PyDict_Copy({})
73.1 ns ± 1.06 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

```py
In [1]: import ctypes
   ...: 
   ...: PyDict_New = ctypes.pythonapi.PyDict_New
   ...: PyDict_New.argtypes = ()
   ...: PyDict_New.restype = ctypes.py_object
   ...: 
   ...: PyDict_Clear = ctypes.pythonapi.PyDict_Clear
   ...: PyDict_Clear.argtypes = (ctypes.py_object,)
   ...: PyDict_Clear.restype = None
   ...: 
   ...: PyDict_Copy = ctypes.pythonapi.PyDict_Copy
   ...: PyDict_Copy.argtypes = (ctypes.py_object,)
   ...: PyDict_Copy.restype = None

In [2]: %timeit PyDict_New()
113 ns ± 0.424 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [3]: %timeit PyDict_Clear({})
273 ns ± 3.34 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [4]: %timeit PyDict_Copy({})
378 ns ± 9.77 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

</div>
