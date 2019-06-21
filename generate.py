import typing


API: typing.Tuple[
    typing.Union[typing.Tuple[str, str, str], typing.Tuple[str, str, str, str, str]],
    ...,
] = (
    # (api, arg_types, return_type, condition_c, condition_pyi),
    # arg_types is according to:
    # https://docs.python.org/3/c-api/arg.html#parsing-arguments
    # return_type is according to:
    # https://docs.python.org/3/c-api/arg.html#building-values
    ("Py_CLEAR", "O", ""),
    ("Py_CompileString", "yyi", "N"),
    ("Py_DECREF", "O", ""),
    ("Py_EnterRecursiveCall", "y", "i"),
    ("Py_Exit", "i", ""),
    ("Py_FatalError", "y", ""),
    ("Py_Finalize", "", ""),
    (
        "Py_FinalizeEx",
        "",
        "i",
        "if 0x030600F0 <= PY_VERSION_HEX",
        '(3, 6, 0, "final", 0) <= sys.version_info',
    ),
    ("Py_GetBuildInfo", "", "y"),
    ("Py_GetCompiler", "", "y"),
    ("Py_GetCopyright", "", "y"),
    ("Py_GetExecPrefix", "", "u"),
    ("Py_GetPath", "", "u"),
    ("Py_GetPlatform", "", "y"),
    ("Py_GetPrefix", "", "u"),
    ("Py_GetProgramFullPath", "", "u"),
    ("Py_GetProgramName", "", "u"),
    ("Py_GetPythonHome", "", "u"),
    ("Py_GetVersion", "", "y"),
    ("Py_INCREF", "O", ""),
    ("Py_Initialize", "", ""),
    ("Py_InitializeEx", "i", ""),
    ("Py_IsInitialized", "", "i"),
    ("Py_LeaveRecursiveCall", "", ""),
    ("Py_ReprEnter", "O", "i"),
    ("Py_ReprLeave", "O", ""),
    ("Py_SetPath", "u", ""),
    ("Py_SetProgramName", "u", ""),
    ("Py_SetPythonHome", "u", ""),
    ("Py_SetStandardStreamEncoding", "yy", "i"),
    ("Py_UNICODE_ISALNUM", "C", "i"),
    ("Py_UNICODE_ISALPHA", "C", "i"),
    ("Py_UNICODE_ISDECIMAL", "C", "i"),
    ("Py_UNICODE_ISDIGIT", "C", "i"),
    ("Py_UNICODE_ISLINEBREAK", "C", "i"),
    ("Py_UNICODE_ISLOWER", "C", "i"),
    ("Py_UNICODE_ISNUMERIC", "C", "i"),
    ("Py_UNICODE_ISPRINTABLE", "C", "i"),
    ("Py_UNICODE_ISSPACE", "C", "i"),
    ("Py_UNICODE_ISTITLE", "C", "i"),
    ("Py_UNICODE_ISUPPER", "C", "i"),
    ("Py_UNICODE_TODECIMAL", "C", "i"),
    ("Py_UNICODE_TODIGIT", "C", "i"),
    ("Py_UNICODE_TOLOWER", "C", "C"),
    ("Py_UNICODE_TONUMERIC", "C", "d"),
    ("Py_UNICODE_TOTITLE", "C", "C"),
    ("Py_UNICODE_TOUPPER", "C", "C"),
    ("Py_XDECREF", "O", ""),
    ("Py_XINCREF", "O", ""),
    ("PyAnySet_Check", "O", "i"),
    ("PyAnySet_CheckExact", "O", "i"),
    ("PyArg_ValidateKeywordArguments", "O", "i"),
    ("PyBool_Check", "O", "i"),
    ("PyBool_FromLong", "l", "N"),
    ("PyByteArray_AS_STRING", "O", "y"),
    ("PyByteArray_AsString", "O", "y"),
    ("PyByteArray_Check", "O", "i"),
    ("PyByteArray_CheckExact", "O", "i"),
    ("PyByteArray_Concat", "OO", "N"),
    ("PyByteArray_FromObject", "O", "N"),
    ("PyByteArray_FromStringAndSize", "yn", "N"),
    ("PyByteArray_GET_SIZE", "O", "n"),
    ("PyByteArray_Resize", "On", "i"),
    ("PyByteArray_Size", "O", "n"),
    ("PyBytes_AS_STRING", "O", "y"),
    ("PyBytes_AsString", "O", "y"),
    ("PyBytes_Check", "O", "i"),
    ("PyBytes_CheckExact", "O", "i"),
    ("PyBytes_FromObject", "O", "N"),
    ("PyBytes_FromString", "y", "N"),
    ("PyBytes_FromStringAndSize", "yn", "N"),
    ("PyBytes_GET_SIZE", "O", "n"),
    ("PyBytes_Size", "O", "n"),
    ("PyCallIter_Check", "O", "i"),
    ("PyCallIter_New", "OO", "N"),
    ("PyCallable_Check", "O", "i"),
    ("PyCapsule_CheckExact", "O", "i"),
    ("PyCapsule_GetName", "O", "y"),
    ("PyCapsule_IsValid", "Oy", "i"),
    ("PyCapsule_SetName", "Oy", "i"),
    ("PyCell_Check", "O", "i"),
    ("PyCell_GET", "O", "N"),
    ("PyCell_Get", "O", "N"),
    ("PyCell_New", "O", "N"),
    ("PyCell_SET", "OO", ""),
    ("PyCell_Set", "OO", "i"),
    ("PyCode_Check", "O", "i"),
    ("PyCodec_BackslashReplaceErrors", "O", "N"),
    ("PyCodec_Decode", "Oyy", "N"),
    ("PyCodec_Decoder", "y", "N"),
    ("PyCodec_Encode", "Oyy", "N"),
    ("PyCodec_Encoder", "y", "N"),
    ("PyCodec_IgnoreErrors", "O", "N"),
    ("PyCodec_IncrementalDecoder", "yy", "N"),
    ("PyCodec_IncrementalEncoder", "yy", "N"),
    ("PyCodec_KnownEncoding", "y", "i"),
    ("PyCodec_LookupError", "y", "N"),
    (
        "PyCodec_NameReplaceErrors",
        "O",
        "N",
        "if 0x030500F0 <= PY_VERSION_HEX",
        '(3, 5, 0, "final", 0) <= sys.version_info',
    ),
    ("PyCodec_Register", "O", "i"),
    ("PyCodec_RegisterError", "yO", "i"),
    ("PyCodec_ReplaceErrors", "O", "N"),
    ("PyCodec_StreamReader", "yOy", "N"),
    ("PyCodec_StreamWriter", "yOy", "N"),
    ("PyCodec_StrictErrors", "O", "N"),
    ("PyCodec_XMLCharRefReplaceErrors", "O", "N"),
    ("PyComplex_AsCComplex", "O", "D"),
    ("PyComplex_Check", "O", "i"),
    ("PyComplex_CheckExact", "O", "i"),
    ("PyComplex_FromCComplex", "D", "N"),
    ("PyComplex_FromDoubles", "dd", "N"),
    ("PyComplex_ImagAsDouble", "O", "d"),
    ("PyComplex_RealAsDouble", "O", "d"),
    (
        "PyContext_CheckExact",
        "O",
        "i",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyContext_ClearFreeList",
        "",
        "i",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyContext_Copy",
        "O",
        "N",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyContext_CopyCurrent",
        "",
        "N",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyContext_Enter",
        "O",
        "i",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyContext_Exit",
        "O",
        "i",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyContext_New",
        "",
        "N",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyContextToken_CheckExact",
        "O",
        "i",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyContextVar_CheckExact",
        "O",
        "i",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyContextVar_New",
        "yO",
        "N",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyContextVar_Reset",
        "OO",
        "i",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyContextVar_Set",
        "OO",
        "N",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    ("PyCoro_CheckExact", "O", "i"),
    ("PyDate_Check", "O", "i"),
    ("PyDate_CheckExact", "O", "i"),
    ("PyDate_FromDate", "iii", "N"),
    ("PyDate_FromTimestamp", "O", "N"),
    ("PyDateTime_Check", "O", "i"),
    ("PyDateTime_CheckExact", "O", "i"),
    ("PyDateTime_FromDateAndTime", "iiiiiii", "N"),
    ("PyDateTime_FromTimestamp", "O", "N"),
    ("PyDelta_Check", "O", "i"),
    ("PyDelta_CheckExact", "O", "i"),
    ("PyDelta_FromDSU", "iii", "N"),
    ("PyDescr_IsData", "O", "i"),
    ("PyDict_Check", "O", "i"),
    ("PyDict_CheckExact", "O", "i"),
    ("PyDict_Clear", "O", ""),
    ("PyDict_ClearFreeList", "", "i"),
    ("PyDict_Contains", "OO", "i"),
    ("PyDict_Copy", "O", "N"),
    ("PyDict_DelItem", "OO", "i"),
    ("PyDict_DelItemString", "Oy", "i"),
    ("PyDict_GetItem", "OO", "N"),
    ("PyDict_GetItemString", "Oy", "N"),
    ("PyDict_GetItemWithError", "OO", "N"),
    ("PyDict_Items", "O", "N"),
    ("PyDict_Keys", "O", "N"),
    ("PyDict_Merge", "OOi", "i"),
    ("PyDict_MergeFromSeq2", "OOi", "i"),
    ("PyDict_New", "", "N"),
    ("PyDict_SetDefault", "OOO", "N"),
    ("PyDict_SetItem", "OOO", "i"),
    ("PyDict_SetItemString", "OyO", "i"),
    ("PyDict_Size", "O", "n"),
    ("PyDict_Update", "OO", "i"),
    ("PyDict_Values", "O", "N"),
    ("PyDictProxy_New", "O", "N"),
    ("PyErr_BadArgument", "", "i"),
    ("PyErr_BadInternalCall", "", ""),
    ("PyErr_CheckSignals", "", "i"),
    ("PyErr_Clear", "", ""),
    ("PyErr_ExceptionMatches", "O", "i"),
    ("PyErr_GivenExceptionMatches", "OO", "i"),
    ("PyErr_NewException", "yOO", "N"),
    ("PyErr_NewExceptionWithDoc", "yyOO", "N"),
    ("PyErr_NoMemory", "", "N"),
    ("PyErr_Occurred", "", "N"),
    ("PyErr_Print", "", ""),
    ("PyErr_PrintEx", "i", ""),
    ("PyErr_Restore", "OOO", ""),
    (
        "PyErr_SetExcFromWindowsErr",
        "Oi",
        "N",
        "ifdef MS_WINDOWS",
        'sys.platform == "win32"',
    ),
    (
        "PyErr_SetExcFromWindowsErrWithFilename",
        "Oiy",
        "N",
        "ifdef MS_WINDOWS",
        'sys.platform == "win32"',
    ),
    (
        "PyErr_SetExcFromWindowsErrWithFilenameObject",
        "OiO",
        "N",
        "ifdef MS_WINDOWS",
        'sys.platform == "win32"',
    ),
    (
        "PyErr_SetExcFromWindowsErrWithFilenameObjects",
        "OiOO",
        "N",
        "ifdef MS_WINDOWS",
        'sys.platform == "win32"',
    ),
    ("PyErr_SetExcInfo", "OOO", ""),
    ("PyErr_SetFromErrno", "O", "N"),
    ("PyErr_SetFromErrnoWithFilename", "Oy", "N"),
    ("PyErr_SetFromErrnoWithFilenameObject", "OO", "N"),
    ("PyErr_SetFromErrnoWithFilenameObjects", "OOO", "N"),
    (
        "PyErr_SetFromWindowsErr",
        "i",
        "N",
        "ifdef MS_WINDOWS",
        'sys.platform == "win32"',
    ),
    (
        "PyErr_SetFromWindowsErrWithFilename",
        "iy",
        "N",
        "ifdef MS_WINDOWS",
        'sys.platform == "win32"',
    ),
    ("PyErr_SetImportError", "OOO", "N"),
    (
        "PyErr_SetImportErrorSubclass",
        "OOOO",
        "N",
        "if 0x030600F0 <= PY_VERSION_HEX",
        '(3, 6, 0, "final", 0) <= sys.version_info',
    ),
    ("PyErr_SetInterrupt", "", ""),
    ("PyErr_SetNone", "O", ""),
    ("PyErr_SetObject", "OO", ""),
    ("PyErr_SetString", "Oy", ""),
    ("PyErr_SyntaxLocation", "yi", ""),
    ("PyErr_SyntaxLocationEx", "yii", ""),
    ("PyErr_SyntaxLocationObject", "Oii", ""),
    ("PyErr_WarnEx", "Oyn", "i"),
    ("PyErr_WarnExplicit", "OyyiyO", "i"),
    ("PyErr_WarnExplicitObject", "OOOiOO", "i"),
    ("PyErr_WriteUnraisable", "O", ""),
    ("PyEval_AcquireLock", "", ""),
    ("PyEval_EvalCode", "OOO", "N"),
    ("PyEval_GetBuiltins", "", "N"),
    (
        "PyEval_GetCallStats",
        "O",
        "N",
        "if PY_VERSION_HEX <= 0x030600F0",
        'sys.version_info <= (3, 6, 0, "final", 0)',
    ),
    ("PyEval_GetFuncDesc", "O", "y"),
    ("PyEval_GetFuncName", "O", "y"),
    ("PyEval_GetGlobals", "", "N"),
    ("PyEval_GetLocals", "", "N"),
    ("PyEval_InitThreads", "", ""),
    ("PyEval_ReInitThreads", "", ""),
    ("PyEval_ReleaseLock", "", ""),
    ("PyEval_ThreadsInitialized", "", "i"),
    ("PyException_GetCause", "O", "N"),
    ("PyException_GetContext", "O", "N"),
    ("PyException_GetTraceback", "O", "N"),
    ("PyException_SetCause", "OO", ""),
    ("PyException_SetContext", "OO", ""),
    ("PyException_SetTraceback", "OO", "i"),
    ("PyFile_FromFd", "iyyiyyyi", "N"),
    ("PyFile_GetLine", "Oi", "N"),
    ("PyFile_WriteObject", "OOi", "i"),
    ("PyFile_WriteString", "yO", "i"),
    ("PyFloat_AS_DOUBLE", "O", "d"),
    ("PyFloat_AsDouble", "O", "d"),
    ("PyFloat_Check", "O", "i"),
    ("PyFloat_CheckExact", "O", "i"),
    ("PyFloat_ClearFreeList", "", "i"),
    ("PyFloat_FromDouble", "d", "N"),
    ("PyFloat_FromString", "O", "N"),
    ("PyFloat_GetInfo", "", "N"),
    ("PyFloat_GetMax", "", "d"),
    ("PyFloat_GetMin", "", "d"),
    ("PyFrozenSet_Check", "O", "i"),
    ("PyFrozenSet_CheckExact", "O", "i"),
    ("PyFrozenSet_New", "O", "N"),
    ("PyFunction_Check", "O", "i"),
    ("PyFunction_GetAnnotations", "O", "N"),
    ("PyFunction_GetClosure", "O", "N"),
    ("PyFunction_GetCode", "O", "N"),
    ("PyFunction_GetDefaults", "O", "N"),
    ("PyFunction_GetGlobals", "O", "N"),
    ("PyFunction_GetModule", "O", "N"),
    ("PyFunction_New", "OO", "N"),
    ("PyFunction_NewWithQualName", "OOO", "N"),
    ("PyFunction_SetAnnotations", "OO", "i"),
    ("PyFunction_SetClosure", "OO", "i"),
    ("PyFunction_SetDefaults", "OO", "i"),
    ("PyGILState_Check", "", "i"),
    ("PyGen_Check", "O", "i"),
    ("PyGen_CheckExact", "O", "i"),
    ("PyImport_AddModule", "y", "N"),
    ("PyImport_AddModuleObject", "O", "N"),
    ("PyImport_Cleanup", "", ""),
    ("PyImport_ExecCodeModule", "yO", "N"),
    ("PyImport_ExecCodeModuleEx", "yOy", "N"),
    ("PyImport_ExecCodeModuleObject", "OOOO", "N"),
    ("PyImport_ExecCodeModuleWithPathnames", "yOyy", "N"),
    ("PyImport_GetImporter", "O", "N"),
    ("PyImport_GetMagicNumber", "", "l"),
    ("PyImport_GetMagicTag", "", "y"),
    (
        "PyImport_GetModule",
        "O",
        "N",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    ("PyImport_GetModuleDict", "", "N"),
    ("PyImport_Import", "O", "N"),
    ("PyImport_ImportFrozenModule", "y", "i"),
    ("PyImport_ImportFrozenModuleObject", "O", "i"),
    ("PyImport_ImportModule", "y", "N"),
    ("PyImport_ImportModuleEx", "yOOO", "N"),
    ("PyImport_ImportModuleLevel", "yOOOi", "N"),
    ("PyImport_ImportModuleLevelObject", "OOOOi", "N"),
    ("PyImport_ImportModuleNoBlock", "y", "N"),
    ("PyImport_ReloadModule", "O", "N"),
    ("PyIndex_Check", "O", "i"),
    ("PyInstanceMethod_Check", "O", "i"),
    ("PyInstanceMethod_Function", "O", "N"),
    ("PyInstanceMethod_GET_FUNCTION", "O", "N"),
    ("PyInstanceMethod_New", "O", "N"),
    ("PyIter_Check", "O", "i"),
    ("PyIter_Next", "O", "N"),
    ("PyList_Append", "OO", "i"),
    ("PyList_AsTuple", "O", "N"),
    ("PyList_Check", "O", "i"),
    ("PyList_CheckExact", "O", "i"),
    ("PyList_ClearFreeList", "", "i"),
    ("PyList_GET_ITEM", "On", "N"),
    ("PyList_GET_SIZE", "O", "n"),
    ("PyList_GetItem", "On", "N"),
    ("PyList_GetSlice", "Onn", "N"),
    ("PyList_Insert", "OnO", "i"),
    ("PyList_New", "n", "N"),
    ("PyList_Reverse", "O", "i"),
    ("PyList_SET_ITEM", "OnO", ""),
    ("PyList_SetItem", "OnO", "i"),
    ("PyList_SetSlice", "OnnO", "i"),
    ("PyList_Size", "O", "n"),
    ("PyList_Sort", "O", "i"),
    ("PyLong_AsDouble", "O", "d"),
    ("PyLong_AsLong", "O", "l"),
    ("PyLong_AsLongLong", "O", "L"),
    ("PyLong_AsSsize_t", "O", "n"),
    ("PyLong_AsUnsignedLong", "O", "k"),
    ("PyLong_AsUnsignedLongLong", "O", "K"),
    ("PyLong_AsUnsignedLongLongMask", "O", "K"),
    ("PyLong_AsUnsignedLongMask", "O", "k"),
    ("PyLong_Check", "O", "i"),
    ("PyLong_CheckExact", "O", "i"),
    ("PyLong_FromDouble", "d", "N"),
    ("PyLong_FromLong", "l", "N"),
    ("PyLong_FromLongLong", "L", "N"),
    ("PyLong_FromSsize_t", "n", "N"),
    ("PyLong_FromUnicode", "uni", "N"),
    ("PyLong_FromUnicodeObject", "Oi", "N"),
    ("PyLong_FromUnsignedLong", "k", "N"),
    ("PyLong_FromUnsignedLongLong", "K", "N"),
    ("PyMapping_Check", "O", "i"),
    ("PyMapping_DelItem", "OO", "i"),
    ("PyMapping_DelItemString", "Oy", "i"),
    ("PyMapping_GetItemString", "Oy", "N"),
    ("PyMapping_HasKey", "OO", "i"),
    ("PyMapping_HasKeyString", "Oy", "i"),
    ("PyMapping_Items", "O", "N"),
    ("PyMapping_Keys", "O", "N"),
    ("PyMapping_Length", "O", "n"),
    ("PyMapping_SetItemString", "OyO", "i"),
    ("PyMapping_Size", "O", "n"),
    ("PyMapping_Values", "O", "N"),
    ("PyMarshal_ReadObjectFromString", "yn", "N"),
    ("PyMarshal_WriteObjectToString", "Oi", "N"),
    ("PyMemoryView_Check", "O", "i"),
    ("PyMemoryView_FromMemory", "yni", "N"),
    ("PyMemoryView_FromObject", "O", "N"),
    ("PyMemoryView_GetContiguous", "Oic", "N"),
    ("PyMethod_Check", "O", "i"),
    ("PyMethod_Function", "O", "N"),
    ("PyMethod_GET_FUNCTION", "O", "N"),
    ("PyMethod_GET_SELF", "O", "N"),
    ("PyMethod_New", "OO", "N"),
    ("PyMethod_Self", "O", "N"),
    ("PyModule_AddIntConstant", "Oyl", "i"),
    ("PyModule_AddObject", "OyO", "i"),
    ("PyModule_AddStringConstant", "Oyy", "i"),
    ("PyModule_Check", "O", "i"),
    ("PyModule_CheckExact", "O", "i"),
    ("PyModule_GetDict", "O", "N"),
    ("PyModule_GetFilename", "O", "y"),
    ("PyModule_GetFilenameObject", "O", "N"),
    ("PyModule_GetName", "O", "y"),
    ("PyModule_GetNameObject", "O", "N"),
    ("PyModule_New", "y", "N"),
    ("PyModule_NewObject", "O", "N"),
    ("PyModule_SetDocString", "Oy", "i"),
    ("PyNumber_Absolute", "O", "N"),
    ("PyNumber_Add", "OO", "N"),
    ("PyNumber_And", "OO", "N"),
    ("PyNumber_AsSsize_t", "OO", "n"),
    ("PyNumber_Check", "O", "i"),
    ("PyNumber_Divmod", "OO", "N"),
    ("PyNumber_Float", "O", "N"),
    ("PyNumber_FloorDivide", "OO", "N"),
    ("PyNumber_InPlaceAdd", "OO", "N"),
    ("PyNumber_InPlaceAnd", "OO", "N"),
    ("PyNumber_InPlaceFloorDivide", "OO", "N"),
    ("PyNumber_InPlaceLshift", "OO", "N"),
    (
        "PyNumber_InPlaceMatrixMultiply",
        "OO",
        "N",
        "if 0x030500F0 <= PY_VERSION_HEX",
        '(3, 5, 0, "final", 0) <= sys.version_info',
    ),
    ("PyNumber_InPlaceMultiply", "OO", "N"),
    ("PyNumber_InPlaceOr", "OO", "N"),
    ("PyNumber_InPlacePower", "OOO", "N"),
    ("PyNumber_InPlaceRemainder", "OO", "N"),
    ("PyNumber_InPlaceRshift", "OO", "N"),
    ("PyNumber_InPlaceSubtract", "OO", "N"),
    ("PyNumber_InPlaceTrueDivide", "OO", "N"),
    ("PyNumber_InPlaceXor", "OO", "N"),
    ("PyNumber_Index", "O", "N"),
    ("PyNumber_Invert", "O", "N"),
    ("PyNumber_Long", "O", "N"),
    ("PyNumber_Lshift", "OO", "N"),
    (
        "PyNumber_MatrixMultiply",
        "OO",
        "N",
        "if 0x030500F0 <= PY_VERSION_HEX",
        '(3, 5, 0, "final", 0) <= sys.version_info',
    ),
    ("PyNumber_Multiply", "OO", "N"),
    ("PyNumber_Negative", "O", "N"),
    ("PyNumber_Or", "OO", "N"),
    ("PyNumber_Positive", "O", "N"),
    ("PyNumber_Power", "OOO", "N"),
    ("PyNumber_Remainder", "OO", "N"),
    ("PyNumber_Rshift", "OO", "N"),
    ("PyNumber_Subtract", "OO", "N"),
    ("PyNumber_ToBase", "Oi", "N"),
    ("PyNumber_TrueDivide", "OO", "N"),
    ("PyNumber_Xor", "OO", "N"),
    ("PyOS_AfterFork", "", ""),
    (
        "PyOS_AfterFork_Child",
        "",
        "",
        "if 0x030700F0 <= PY_VERSION_HEX\nifndef MS_WINDOWS",
        '(3, 7, 0, "final", 0) <= sys.version_info and sys.platform != "win32"',
    ),
    (
        "PyOS_AfterFork_Parent",
        "",
        "",
        "if 0x030700F0 <= PY_VERSION_HEX\nifndef MS_WINDOWS",
        '(3, 7, 0, "final", 0) <= sys.version_info and sys.platform != "win32"',
    ),
    (
        "PyOS_BeforeFork",
        "",
        "",
        "if 0x030700F0 <= PY_VERSION_HEX\nifndef MS_WINDOWS",
        '(3, 7, 0, "final", 0) <= sys.version_info and sys.platform != "win32"',
    ),
    (
        "PyOS_FSPath",
        "O",
        "N",
        "if 0x030600F0 <= PY_VERSION_HEX",
        '(3, 6, 0, "final", 0) <= sys.version_info',
    ),
    ("PyObject_ASCII", "O", "N"),
    ("PyObject_AsFileDescriptor", "O", "i"),
    ("PyObject_Bytes", "O", "N"),
    ("PyObject_Call", "OOO", "N"),
    ("PyObject_CallObject", "OO", "N"),
    ("PyObject_CheckBuffer", "O", "i"),
    ("PyObject_CheckReadBuffer", "O", "i"),
    ("PyObject_DelAttr", "OO", "i"),
    ("PyObject_DelAttrString", "Oy", "i"),
    ("PyObject_DelItem", "OO", "i"),
    ("PyObject_Dir", "O", "N"),
    ("PyObject_GC_Track", "O", ""),
    ("PyObject_GenericGetAttr", "OO", "N"),
    ("PyObject_GenericSetAttr", "OOO", "i"),
    ("PyObject_GetAttr", "OO", "N"),
    ("PyObject_GetAttrString", "Oy", "N"),
    ("PyObject_GetItem", "OO", "N"),
    ("PyObject_GetIter", "O", "N"),
    ("PyObject_HasAttr", "OO", "i"),
    ("PyObject_HasAttrString", "Oy", "i"),
    ("PyObject_Hash", "O", "n"),
    ("PyObject_HashNotImplemented", "O", "n"),
    ("PyObject_IsInstance", "OO", "i"),
    ("PyObject_IsSubclass", "OO", "i"),
    ("PyObject_IsTrue", "O", "i"),
    ("PyObject_Length", "O", "n"),
    ("PyObject_LengthHint", "On", "n"),
    ("PyObject_Not", "O", "i"),
    ("PyObject_Repr", "O", "N"),
    ("PyObject_RichCompare", "OOi", "N"),
    ("PyObject_RichCompareBool", "OOi", "i"),
    ("PyObject_SetAttr", "OOO", "i"),
    ("PyObject_SetAttrString", "OyO", "i"),
    ("PyObject_SetItem", "OOO", "i"),
    ("PyObject_Size", "O", "n"),
    ("PyObject_Str", "O", "N"),
    ("PyObject_Type", "O", "N"),
    ("PyRun_SimpleString", "y", "i"),
    ("PyRun_String", "yiOO", "N"),
    ("PySeqIter_Check", "O", "i"),
    ("PySeqIter_New", "O", "N"),
    ("PySequence_Check", "O", "i"),
    ("PySequence_Concat", "OO", "N"),
    ("PySequence_Contains", "OO", "i"),
    ("PySequence_Count", "OO", "n"),
    ("PySequence_DelItem", "On", "i"),
    ("PySequence_DelSlice", "Onn", "i"),
    ("PySequence_Fast", "Oy", "N"),
    ("PySequence_Fast_GET_ITEM", "On", "N"),
    ("PySequence_Fast_GET_SIZE", "O", "n"),
    ("PySequence_GetItem", "On", "N"),
    ("PySequence_GetSlice", "Onn", "N"),
    ("PySequence_ITEM", "On", "N"),
    ("PySequence_In", "OO", "i"),
    ("PySequence_InPlaceConcat", "OO", "N"),
    ("PySequence_InPlaceRepeat", "On", "N"),
    ("PySequence_Index", "OO", "n"),
    ("PySequence_List", "O", "N"),
    ("PySequence_Repeat", "On", "N"),
    ("PySequence_SetItem", "OnO", "i"),
    ("PySequence_SetSlice", "OnnO", "i"),
    ("PySequence_Size", "O", "n"),
    ("PySequence_Tuple", "O", "N"),
    ("PySet_Add", "OO", "i"),
    ("PySet_Check", "O", "i"),
    ("PySet_Clear", "O", "i"),
    ("PySet_Contains", "OO", "i"),
    ("PySet_Discard", "OO", "i"),
    ("PySet_GET_SIZE", "O", "n"),
    ("PySet_New", "O", "N"),
    ("PySet_Pop", "O", "N"),
    ("PySet_Size", "O", "n"),
    ("PySignal_SetWakeupFd", "i", "i", "ifndef MS_WINDOWS", 'sys.platform != "win32"'),
    ("PySlice_Check", "O", "i"),
    ("PySlice_New", "OOO", "N"),
    ("PyStructSequence_GET_ITEM", "On", "N"),
    ("PyStructSequence_GetItem", "On", "N"),
    ("PyStructSequence_SetItem", "OnO", ""),
    ("PySys_AddWarnOption", "u", ""),
    ("PySys_AddWarnOptionUnicode", "O", ""),
    ("PySys_AddXOption", "u", ""),
    ("PySys_GetObject", "y", "N"),
    ("PySys_GetXOptions", "", "N"),
    ("PySys_ResetWarnOptions", "", ""),
    ("PySys_SetObject", "yO", "i"),
    ("PyThreadState_GetDict", "", "N"),
    ("PyThreadState_SetAsyncExc", "kO", "i"),
    ("PyTime_Check", "O", "i"),
    ("PyTime_CheckExact", "O", "i"),
    ("PyTime_FromTime", "iiii", "N"),
    (
        "PyTimeZone_FromOffset",
        "O",
        "N",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    (
        "PyTimeZone_FromOffsetAndName",
        "OO",
        "N",
        "if 0x030700F0 <= PY_VERSION_HEX",
        '(3, 7, 0, "final", 0) <= sys.version_info',
    ),
    ("PyTuple_Check", "O", "i"),
    ("PyTuple_CheckExact", "O", "i"),
    ("PyTuple_GET_ITEM", "On", "N"),
    ("PyTuple_GET_SIZE", "O", "n"),
    ("PyTuple_GetItem", "On", "N"),
    ("PyTuple_GetSlice", "Onn", "N"),
    ("PyTuple_New", "n", "N"),
    ("PyTuple_SET_ITEM", "OnO", ""),
    ("PyTuple_SetItem", "OnO", "i"),
    ("PyTuple_Size", "O", "n"),
    ("PyType_Check", "O", "i"),
    ("PyType_CheckExact", "O", "i"),
    ("PyUnicode_AS_DATA", "O", "y"),
    ("PyUnicode_AS_UNICODE", "O", "u"),
    ("PyUnicode_AsASCIIString", "O", "N"),
    ("PyUnicode_AsCharmapString", "OO", "N"),
    ("PyUnicode_AsEncodedString", "Oyy", "N"),
    ("PyUnicode_AsLatin1String", "O", "N"),
    ("PyUnicode_AsMBCSString", "O", "N", "ifdef MS_WINDOWS", 'sys.platform == "win32"'),
    ("PyUnicode_AsRawUnicodeEscapeString", "O", "N"),
    ("PyUnicode_AsUTF16String", "O", "N"),
    ("PyUnicode_AsUTF32String", "O", "N"),
    ("PyUnicode_AsUTF8", "O", "y"),
    ("PyUnicode_AsUTF8String", "O", "N"),
    ("PyUnicode_AsUnicode", "O", "u"),
    ("PyUnicode_AsUnicodeCopy", "O", "u"),
    ("PyUnicode_AsUnicodeEscapeString", "O", "N"),
    ("PyUnicode_AsWideChar", "Oun", "n"),
    ("PyUnicode_Check", "O", "i"),
    ("PyUnicode_CheckExact", "O", "i"),
    ("PyUnicode_Compare", "OO", "i"),
    ("PyUnicode_CompareWithASCIIString", "Oy", "i"),
    ("PyUnicode_Concat", "OO", "N"),
    ("PyUnicode_Contains", "OO", "i"),
    ("PyUnicode_CopyCharacters", "OnOnn", "n"),
    ("PyUnicode_Count", "OOnn", "n"),
    ("PyUnicode_Decode", "ynyy", "N"),
    ("PyUnicode_DecodeASCII", "yny", "N"),
    ("PyUnicode_DecodeCharmap", "ynOy", "N"),
    ("PyUnicode_DecodeFSDefault", "y", "N"),
    ("PyUnicode_DecodeFSDefaultAndSize", "yn", "N"),
    ("PyUnicode_DecodeLatin1", "yny", "N"),
    ("PyUnicode_DecodeLocale", "yy", "N"),
    ("PyUnicode_DecodeLocaleAndSize", "yny", "N"),
    ("PyUnicode_DecodeMBCS", "yny", "N", "ifdef MS_WINDOWS", 'sys.platform == "win32"'),
    ("PyUnicode_DecodeRawUnicodeEscape", "yny", "N"),
    ("PyUnicode_DecodeUTF7", "yny", "N"),
    ("PyUnicode_DecodeUTF8", "yny", "N"),
    ("PyUnicode_DecodeUnicodeEscape", "yny", "N"),
    ("PyUnicode_Encode", "unyy", "N"),
    ("PyUnicode_EncodeASCII", "uny", "N"),
    ("PyUnicode_EncodeCharmap", "unOy", "N"),
    (
        "PyUnicode_EncodeCodePage",
        "iOy",
        "N",
        "ifdef MS_WINDOWS",
        'sys.platform == "win32"',
    ),
    ("PyUnicode_EncodeFSDefault", "O", "N"),
    ("PyUnicode_EncodeLatin1", "uny", "N"),
    ("PyUnicode_EncodeLocale", "Oy", "N"),
    ("PyUnicode_EncodeMBCS", "uny", "N", "ifdef MS_WINDOWS", 'sys.platform == "win32"'),
    ("PyUnicode_EncodeRawUnicodeEscape", "un", "N"),
    ("PyUnicode_EncodeUTF16", "unyi", "N"),
    ("PyUnicode_EncodeUTF32", "unyi", "N"),
    ("PyUnicode_EncodeUTF7", "uniiy", "N"),
    ("PyUnicode_EncodeUTF8", "uny", "N"),
    ("PyUnicode_EncodeUnicodeEscape", "un", "N"),
    ("PyUnicode_Find", "OOnni", "n"),
    ("PyUnicode_Format", "OO", "N"),
    ("PyUnicode_FromEncodedObject", "Oyy", "N"),
    ("PyUnicode_FromObject", "O", "N"),
    ("PyUnicode_FromString", "y", "N"),
    ("PyUnicode_FromStringAndSize", "yn", "N"),
    ("PyUnicode_FromUnicode", "un", "N"),
    ("PyUnicode_FromWideChar", "un", "N"),
    ("PyUnicode_GET_DATA_SIZE", "O", "n"),
    ("PyUnicode_GET_LENGTH", "O", "n"),
    ("PyUnicode_GET_SIZE", "O", "n"),
    ("PyUnicode_GetLength", "O", "n"),
    ("PyUnicode_GetSize", "O", "n"),
    ("PyUnicode_InternFromString", "y", "N"),
    ("PyUnicode_Join", "OO", "N"),
    ("PyUnicode_KIND", "O", "i"),
    ("PyUnicode_READY", "O", "i"),
    ("PyUnicode_Replace", "OOOn", "N"),
    ("PyUnicode_RichCompare", "OOi", "N"),
    ("PyUnicode_Split", "OOn", "N"),
    ("PyUnicode_Splitlines", "Oi", "N"),
    ("PyUnicode_Substring", "Onn", "N"),
    ("PyUnicode_Tailmatch", "OOnni", "n"),
    ("PyUnicode_TransformDecimalToASCII", "un", "N"),
    ("PyUnicode_Translate", "OOy", "N"),
    ("PyUnicode_TranslateCharmap", "unOy", "N"),
    ("PyUnicodeDecodeError_Create", "yynnny", "N"),
    ("PyUnicodeDecodeError_GetEncoding", "O", "N"),
    ("PyUnicodeDecodeError_GetObject", "O", "N"),
    ("PyUnicodeDecodeError_GetReason", "O", "N"),
    ("PyUnicodeDecodeError_SetEnd", "On", "i"),
    ("PyUnicodeDecodeError_SetReason", "Oy", "i"),
    ("PyUnicodeDecodeError_SetStart", "On", "i"),
    ("PyUnicodeEncodeError_Create", "yunnny", "N"),
    ("PyUnicodeTranslateError_Create", "unnny", "N"),
    ("PyWeakref_Check", "O", "i"),
    ("PyWeakref_CheckProxy", "O", "i"),
    ("PyWeakref_CheckRef", "O", "i"),
    ("PyWeakref_GET_OBJECT", "O", "N"),
    ("PyWeakref_GetObject", "O", "N"),
    ("PyWeakref_NewProxy", "OO", "N"),
    ("PyWeakref_NewRef", "OO", "N"),
    ("PyWrapper_New", "OO", "N"),
)


INDENT = 4 * " "


PYCAPI_PYI = """\
\"\"\"This file is automatically generated by generate.py.\"\"\"


import sys
import typing


{}
"""

STUB = "def {}({}) -> {}: ..."

ARG_TYPES_PYI = {
    "C": "str",
    "c": "bytes",
    "D": "complex",
    "d": "float",
    "i": "int",
    "K": "int",
    "k": "int",
    "L": "int",
    "l": "int",
    "n": "int",
    "O": "object",
    "u": "str",
    "y": "bytes",
}

RETURN_TYPES_PYI = {
    "": "None",
    "C": "str",
    "D": "complex",
    "d": "float",
    "i": "int",
    "K": "int",
    "k": "int",
    "L": "int",
    "l": "int",
    "N": "typing.Any",
    "n": "int",
    "u": "typing.Optional[str]",
    "y": "typing.Optional[bytes]",
}

ARG_TYPES_C = {
    "C": "int",
    "c": "char",
    "D": "Py_complex",
    "d": "double",
    "i": "int",
    "K": "unsigned long long int",
    "k": "unsigned long int",
    "L": "long long int",
    "l": "long int",
    "n": "Py_ssize_t",
    "O": "PyObject*",
    "u": "wchar_t*",
    "y": "char*",
}

RETURN_TYPES_C = {
    "": "void",
    "C": "int",
    "D": "Py_complex",
    "d": "double",
    "i": "int",
    "K": "unsigned long long int",
    "k": "unsigned long int",
    "L": "long long int",
    "l": "long int",
    "N": "PyObject*",
    "n": "Py_ssize_t",
    "u": "const wchar_t*",
    "y": "const char*",
}

CONVERTERS = {
    "": "Py_RETURN_NONE;",
    "C": 'return PyUnicode_FromFormat("%c", result);',
    "D": "return PyComplex_FromCComplex(result);",
    "d": "return PyFloat_FromDouble(result);",
    "i": "return PyLong_FromLong(result);",
    "K": "return PyLong_FromUnsignedLongLong(result);",
    "k": "return PyLong_FromUnsignedLong(result);",
    "L": "return PyLong_FromLongLong(result);",
    "l": "return PyLong_FromLong(result);",
    "N": "return result;",
    "n": "return PyLong_FromSsize_t(result);",
    "u": "return PyUnicode_FromWideChar(result, -1);",
    "y": "return PyBytes_FromString(result);",
}

FUNCTIONDEF = """\
static PyObject* capi_{}(PyObject* Py_UNUSED(self), PyObject* {}) {{
{}
}}
"""

ERROR_CHECK_PYOBJECT = """\
if (!result) {

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}
"""

ERROR_CHECK = """\
if (PyErr_Occurred()) {
    return NULL;
}
"""

METH_NOARGS = '{{"{api}", capi_{api}, METH_NOARGS, NULL}},'
METH_O = '{{"{api}", capi_{api}, METH_O, NULL}},'
METH_VARARGS = '{{"{api}", capi_{api}, METH_VARARGS, NULL}},'

PYCAPI_C = """\
/* This file is automatically generated by generate.py. */


# include "Python.h"
# include "datetime.h"
# include "marshal.h"


// static PyTypeObject NULLType;


/* Wrapper definitions: */


{}


/* Module bindings: */


static PyMethodDef CAPIMethods[] =  {{

{}

     /* End */

    {{NULL, NULL, 0, NULL}},
}};


/* NULL */


// static int null_bool(PyObject *Py_UNUSED(null)) {{
//     return 0;
// }}

// static PyObject* null_repr(PyObject *Py_UNUSED(null)) {{
//     return PyUnicode_FromString("NULL");
// }}

// static PyNumberMethods null_as_number = {{
//     0,         /* nb_add */
//     0,         /* nb_subtract */
//     0,         /* nb_multiply */
//     0,         /* nb_remainder */
//     0,         /* nb_divmod */
//     0,         /* nb_power */
//     0,         /* nb_negative */
//     0,         /* nb_positive */
//     0,         /* nb_absolute */
//     null_bool, /* nb_bool */
//     0,         /* nb_invert */
//     0,         /* nb_lshift */
//     0,         /* nb_rshift */
//     0,         /* nb_and */
//     0,         /* nb_xor */
//     0,         /* nb_or */
//     0,         /* nb_int */
//     0,         /* nb_reserved */
//     0,         /* nb_float */
//     0,         /* nb_inplace_add */
//     0,         /* nb_inplace_subtract */
//     0,         /* nb_inplace_multiply */
//     0,         /* nb_inplace_remainder */
//     0,         /* nb_inplace_power */
//     0,         /* nb_inplace_lshift */
//     0,         /* nb_inplace_rshift */
//     0,         /* nb_inplace_and */
//     0,         /* nb_inplace_xor */
//     0,         /* nb_inplace_or */
//     0,         /* nb_floor_divide */
//     0,         /* nb_true_divide */
//     0,         /* nb_inplace_floor_divide */
//     0,         /* nb_inplace_true_divide */
//     0,         /* nb_index */
// }};

// static PyTypeObject NULLType = {{
//     {{PyObject_HEAD_INIT(&PyType_Type)}},
//     "void *",        /* tp_name */
//     0,               /* tp_basicsize */
//     0,               /* tp_itemsize */
//     0,               /* tp_dealloc */
//     0,               /* tp_print */
//     0,               /* tp_getattr */
//     0,               /* tp_setattr */
//     0,               /* tp_reserved */
//     null_repr,       /* tp_repr */
//     &null_as_number, /* tp_as_number */
//     0,               /* tp_as_sequence */
//     0,               /* tp_as_mapping */
//     0,               /* tp_hash */
//     0,               /* tp_call */
//     0,               /* tp_str */
//     0,               /* tp_getattro */
//     0,               /* tp_setattro */
//     0,               /* tp_as_buffer */
//     0,               /* tp_flags */
//     0,               /* tp_doc */
//     0,               /* tp_traverse */
//     0,               /* tp_clear */
//     0,               /* tp_richcompare */
//     0,               /* tp_weaklistoffset */
//     0,               /* tp_iter */
//     0,               /* tp_iternext */
//     0,               /* tp_methods */
//     0,               /* tp_members */
//     0,               /* tp_getset */
//     0,               /* tp_base */
//     0,               /* tp_dict */
//     0,               /* tp_descr_get */
//     0,               /* tp_descr_set */
//     0,               /* tp_dictoffset */
//     0,               /* tp_init */
//     0,               /* tp_alloc */
//     0,               /* tp_new */
// }};


/* Module initialization boilerplate: */


static struct PyModuleDef CAPIModule = {{
    PyModuleDef_HEAD_INIT, "pycapi", NULL, -1, CAPIMethods,
}};


PyObject* PyInit_pycapi(void) {{

    PyObject* capi;
    //PyObject* capi_null;

    PyDateTime_IMPORT;

    capi = PyModule_Create(&CAPIModule);
    /*
    capi_null = PyObject_New(PyObject, &NULLType);

    if (!capi_null) {{
        return NULL;
    }}

    PyModule_AddObject(capi, "_NULL", capi_null);
    */
    return capi;
}}
"""


def build_stub(api: str, arg_types: str, return_type: str) -> str:

    args_str = ", ".join(
        "__{}: {}".format(arg, ARG_TYPES_PYI[annotation])
        for arg, annotation in enumerate(arg_types)
    )
    return_str = RETURN_TYPES_PYI[return_type]

    return STUB.format(api, args_str, return_str)


def build_definition(api: str, arg_types: str, return_type: str) -> str:

    # TODO:
    #   - Clean up.
    #   - NULL args.
    #   - NULL return.

    body: typing.List[str] = []

    if arg_types and arg_types != "O":
        body.append("")
        body.extend(
            "{} arg{};".format(ARG_TYPES_C[annotation], arg)
            for arg, annotation in enumerate(arg_types)
        )
    if return_type:
        body.append("")
        body.append(f"{RETURN_TYPES_C[return_type]} result;")

    if arg_types and arg_types != "O":
        body.append("")
        if set(arg_types) == {"O"}:
            body.append(
                'if (!PyArg_UnpackTuple(args, "{}", {}, {}{})) {{'.format(
                    api,
                    len(arg_types),
                    len(arg_types),
                    "".join(", &arg{}".format(arg) for arg in range(len(arg_types))),
                )
            )
        else:
            body.append(
                'if (!PyArg_ParseTuple(args, "{}:{}"{})) {{'.format(
                    arg_types,
                    api,
                    "".join(", &arg{}".format(arg) for arg in range(len(arg_types))),
                )
            )
        body.append(INDENT + "return NULL;")
        body.append("}")

    if return_type:
        body.append("")
        body.append(
            "result = {}({});".format(
                api,
                ", ".join("arg{}".format(arg) for arg in range(len(arg_types)))
                if arg_types != "O"
                else "arg",
            )
        )
    else:
        body.append("")
        body.append(
            "{}({});".format(
                api,
                ", ".join("arg{}".format(arg) for arg in range(len(arg_types)))
                if arg_types != "O"
                else "arg",
            )
        )

    if return_type == "N":
        body.append("")
        body.extend(ERROR_CHECK_PYOBJECT.splitlines())
    else:
        body.append("")
        body.extend(ERROR_CHECK.splitlines())

    body.append("")
    body.append(CONVERTERS[return_type])

    if not arg_types:
        args = "Py_UNUSED(null)"
    elif arg_types == "O":
        args = "arg"
    else:
        args = "args"

    return FUNCTIONDEF.format(api, args, INDENT + ("\n" + INDENT).join(body))


if __name__ == "__main__":

    pycapi_c_1: typing.List[str] = []
    pycapi_c_2: typing.List[str] = []
    pycapi_pyi: typing.List[str] = []
    condition: typing.List[str] = []
    indent = False
    base = None

    new_condition: typing.List[str]

    for api, arg_types, return_type, *new_condition in sorted(
        API, key=lambda item: item[0].split("_")
    ):

        new_base = api.split("_")[0]

        # TODO: Handle conditions individually.

        if new_condition != condition:

            if condition:

                indent = False

                pycapi_c_1.append("")
                pycapi_c_2.append("")

                for _ in condition[0].splitlines():

                    pycapi_c_1.append("# endif")
                    pycapi_c_2.append(INDENT + "# endif")

            pycapi_c_1.append("")
            pycapi_c_2.append("")
            pycapi_pyi.append("")

            if new_condition:

                for c in new_condition[0].splitlines():

                    pycapi_c_1.append(f"# {c}")
                    pycapi_c_2.append(INDENT + f"# {c}")

                pycapi_pyi.append(f"if {new_condition[1]}:")

                pycapi_c_1.append("")
                pycapi_c_2.append("")
                pycapi_pyi.append("")

                indent = True

            if new_base != base:

                pycapi_c_1.extend((INDENT * indent + f"/* {new_base} */", ""))
                pycapi_c_2.extend((INDENT * (indent + 1) + f"/* {new_base} */", ""))
                pycapi_pyi.extend((INDENT * indent + f"# {new_base}", ""))

                base = new_base

        elif new_base != base:

            if base is not None:

                pycapi_c_1.append("")
                pycapi_c_2.append("")
                pycapi_pyi.append("")

            pycapi_c_1.extend((INDENT * indent + f"/* {new_base} */", ""))
            pycapi_c_2.extend((INDENT * (indent + 1) + f"/* {new_base} */", ""))
            pycapi_pyi.extend((INDENT * indent + f"# {new_base}", ""))

            base = new_base

        condition = new_condition

        if pycapi_c_1[-1]:
            pycapi_c_1.append("")

        pycapi_c_1.extend(
            (INDENT * indent + line).rstrip()
            for line in build_definition(api, arg_types, return_type).splitlines()
        )
        if not arg_types:
            pycapi_c_2.append(INDENT * (indent + 1) + METH_NOARGS.format(api=api))
        elif arg_types == "O":
            pycapi_c_2.append(INDENT * (indent + 1) + METH_O.format(api=api))
        else:
            pycapi_c_2.append(INDENT * (indent + 1) + METH_VARARGS.format(api=api))
        pycapi_pyi.append(INDENT * indent + build_stub(api, arg_types, return_type))

    if condition:

        pycapi_c_1.append("")
        pycapi_c_2.append("")

        pycapi_c_1.append("# endif")
        pycapi_c_2.append(INDENT + "# endif")

    pycapi_c = PYCAPI_C.format("\n".join(pycapi_c_1), "\n".join(pycapi_c_2))

    with open("pycapi.c", "w") as file:
        file.write(pycapi_c)

    with open("pycapi.pyi", "w") as file:
        file.write(PYCAPI_PYI.format("\n".join(pycapi_pyi)))
