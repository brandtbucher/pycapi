"""This file is automatically generated by generate.py."""


import sys
import typing


# PyAnySet

def PyAnySet_Check(__0: object) -> int: ...
def PyAnySet_CheckExact(__0: object) -> int: ...

# PyBool

def PyBool_Check(__0: object) -> int: ...
def PyBool_FromLong(__0: int) -> typing.Any: ...

# PyByteArray

def PyByteArray_AS_STRING(__0: object) -> typing.Optional[bytes]: ...
def PyByteArray_AsString(__0: object) -> typing.Optional[bytes]: ...
def PyByteArray_Check(__0: object) -> int: ...
def PyByteArray_CheckExact(__0: object) -> int: ...
def PyByteArray_Concat(__0: object, __1: object) -> typing.Any: ...
def PyByteArray_FromObject(__0: object) -> typing.Any: ...
def PyByteArray_FromStringAndSize(__0: bytes, __1: int) -> typing.Any: ...
def PyByteArray_GET_SIZE(__0: object) -> int: ...
def PyByteArray_Resize(__0: object, __1: int) -> int: ...
def PyByteArray_Size(__0: object) -> int: ...

# PyBytes

def PyBytes_AS_STRING(__0: object) -> typing.Optional[bytes]: ...
def PyBytes_AsString(__0: object) -> typing.Optional[bytes]: ...
def PyBytes_Check(__0: object) -> int: ...
def PyBytes_CheckExact(__0: object) -> int: ...
def PyBytes_FromObject(__0: object) -> typing.Any: ...
def PyBytes_FromString(__0: bytes) -> typing.Any: ...
def PyBytes_FromStringAndSize(__0: bytes, __1: int) -> typing.Any: ...
def PyBytes_GET_SIZE(__0: object) -> int: ...
def PyBytes_Size(__0: object) -> int: ...

# PyCallIter

def PyCallIter_Check(__0: object) -> int: ...
def PyCallIter_New(__0: object, __1: object) -> typing.Any: ...

# PyCallable

def PyCallable_Check(__0: object) -> int: ...

# PyCapsule

def PyCapsule_CheckExact(__0: object) -> int: ...
def PyCapsule_GetName(__0: object) -> typing.Optional[bytes]: ...

# PyCell

def PyCell_Check(__0: object) -> int: ...
def PyCell_GET(__0: object) -> typing.Any: ...
def PyCell_Get(__0: object) -> typing.Any: ...
def PyCell_New(__0: object) -> typing.Any: ...
def PyCell_SET(__0: object, __1: object) -> None: ...
def PyCell_Set(__0: object, __1: object) -> int: ...

# PyCode

def PyCode_Check(__0: object) -> int: ...

# PyCodec

def PyCodec_BackslashReplaceErrors(__0: object) -> typing.Any: ...
def PyCodec_Decode(__0: object, __1: bytes, __2: bytes) -> typing.Any: ...
def PyCodec_Decoder(__0: bytes) -> typing.Any: ...
def PyCodec_Encode(__0: object, __1: bytes, __2: bytes) -> typing.Any: ...
def PyCodec_Encoder(__0: bytes) -> typing.Any: ...
def PyCodec_IgnoreErrors(__0: object) -> typing.Any: ...
def PyCodec_IncrementalDecoder(__0: bytes, __1: bytes) -> typing.Any: ...
def PyCodec_IncrementalEncoder(__0: bytes, __1: bytes) -> typing.Any: ...
def PyCodec_KnownEncoding(__0: bytes) -> int: ...
def PyCodec_LookupError(__0: bytes) -> typing.Any: ...

if (3, 5, 0, "final", 0) <= sys.version_info:

    def PyCodec_NameReplaceErrors(__0: object) -> typing.Any: ...

def PyCodec_Register(__0: object) -> int: ...
def PyCodec_RegisterError(__0: bytes, __1: object) -> int: ...
def PyCodec_ReplaceErrors(__0: object) -> typing.Any: ...
def PyCodec_StreamReader(__0: bytes, __1: object, __2: bytes) -> typing.Any: ...
def PyCodec_StreamWriter(__0: bytes, __1: object, __2: bytes) -> typing.Any: ...
def PyCodec_StrictErrors(__0: object) -> typing.Any: ...
def PyCodec_XMLCharRefReplaceErrors(__0: object) -> typing.Any: ...

# PyComplex

def PyComplex_AsCComplex(__0: object) -> complex: ...
def PyComplex_Check(__0: object) -> int: ...
def PyComplex_CheckExact(__0: object) -> int: ...
def PyComplex_FromCComplex(__0: complex) -> typing.Any: ...
def PyComplex_FromDoubles(__0: float, __1: float) -> typing.Any: ...
def PyComplex_ImagAsDouble(__0: object) -> float: ...
def PyComplex_RealAsDouble(__0: object) -> float: ...

if (3, 7, 0, "final", 0) <= sys.version_info:

    # PyContextToken

    def PyContextToken_CheckExact(__0: object) -> int: ...

    # PyContextVar

    def PyContextVar_CheckExact(__0: object) -> int: ...
    def PyContextVar_Reset(__0: object, __1: object) -> int: ...
    def PyContextVar_Set(__0: object, __1: object) -> typing.Any: ...

    # PyContext

    def PyContext_CheckExact(__0: object) -> int: ...
    def PyContext_ClearFreeList() -> int: ...
    def PyContext_Copy(__0: object) -> typing.Any: ...
    def PyContext_CopyCurrent() -> typing.Any: ...
    def PyContext_Enter(__0: object) -> int: ...
    def PyContext_Exit(__0: object) -> int: ...
    def PyContext_New() -> typing.Any: ...

# PyCoro

def PyCoro_CheckExact(__0: object) -> int: ...

# PyDateTime

def PyDateTime_Check(__0: object) -> int: ...
def PyDateTime_CheckExact(__0: object) -> int: ...
def PyDateTime_FromDateAndTime(__0: int, __1: int, __2: int, __3: int, __4: int, __5: int, __6: int) -> typing.Any: ...
def PyDateTime_FromTimestamp(__0: object) -> typing.Any: ...

# PyDate

def PyDate_Check(__0: object) -> int: ...
def PyDate_CheckExact(__0: object) -> int: ...
def PyDate_FromDate(__0: int, __1: int, __2: int) -> typing.Any: ...
def PyDate_FromTimestamp(__0: object) -> typing.Any: ...

# PyDelta

def PyDelta_Check(__0: object) -> int: ...
def PyDelta_CheckExact(__0: object) -> int: ...
def PyDelta_FromDSU(__0: int, __1: int, __2: int) -> typing.Any: ...

# PyDescr

def PyDescr_IsData(__0: object) -> int: ...

# PyDictProxy

def PyDictProxy_New(__0: object) -> typing.Any: ...

# PyDict

def PyDict_Check(__0: object) -> int: ...
def PyDict_CheckExact(__0: object) -> int: ...
def PyDict_Clear(__0: object) -> None: ...
def PyDict_Contains(__0: object, __1: object) -> int: ...
def PyDict_Copy(__0: object) -> typing.Any: ...
def PyDict_DelItem(__0: object, __1: object) -> int: ...
def PyDict_GetItem(__0: object, __1: object) -> typing.Any: ...
def PyDict_GetItemWithError(__0: object, __1: object) -> typing.Any: ...
def PyDict_Items(__0: object) -> typing.Any: ...
def PyDict_Keys(__0: object) -> typing.Any: ...
def PyDict_New() -> typing.Any: ...
def PyDict_SetDefault(__0: object, __1: object, __2: object) -> typing.Any: ...
def PyDict_SetItem(__0: object, __1: object, __2: object) -> int: ...
def PyDict_Size(__0: object) -> int: ...
def PyDict_Update(__0: object, __1: object) -> int: ...
def PyDict_Values(__0: object) -> typing.Any: ...

# PyErr

def PyErr_BadArgument() -> int: ...
def PyErr_BadInternalCall() -> None: ...
def PyErr_CheckSignals() -> int: ...
def PyErr_Clear() -> None: ...
def PyErr_ExceptionMatches(__0: object) -> int: ...
def PyErr_GivenExceptionMatches(__0: object, __1: object) -> int: ...
def PyErr_NoMemory() -> typing.Any: ...
def PyErr_Occurred() -> typing.Any: ...
def PyErr_Print() -> None: ...
def PyErr_Restore(__0: object, __1: object, __2: object) -> None: ...
def PyErr_SetExcInfo(__0: object, __1: object, __2: object) -> None: ...
def PyErr_SetFromErrno(__0: object) -> typing.Any: ...
def PyErr_SetFromErrnoWithFilenameObject(__0: object, __1: object) -> typing.Any: ...
def PyErr_SetFromErrnoWithFilenameObjects(__0: object, __1: object, __2: object) -> typing.Any: ...
def PyErr_SetImportError(__0: object, __1: object, __2: object) -> typing.Any: ...

if (3, 6, 0, "final", 0) <= sys.version_info:

    def PyErr_SetImportErrorSubclass(__0: object, __1: object, __2: object, __3: object) -> typing.Any: ...

def PyErr_SetInterrupt() -> None: ...
def PyErr_SetNone(__0: object) -> None: ...
def PyErr_SetObject(__0: object, __1: object) -> None: ...
def PyErr_WriteUnraisable(__0: object) -> None: ...

# PyEval

def PyEval_AcquireLock() -> None: ...
def PyEval_EvalCode(__0: object, __1: object, __2: object) -> typing.Any: ...
def PyEval_GetBuiltins() -> typing.Any: ...
def PyEval_GetFuncDesc(__0: object) -> typing.Optional[bytes]: ...
def PyEval_GetFuncName(__0: object) -> typing.Optional[bytes]: ...
def PyEval_GetGlobals() -> typing.Any: ...
def PyEval_GetLocals() -> typing.Any: ...
def PyEval_InitThreads() -> None: ...
def PyEval_ReleaseLock() -> None: ...

# PyException

def PyException_GetCause(__0: object) -> typing.Any: ...
def PyException_GetContext(__0: object) -> typing.Any: ...
def PyException_GetTraceback(__0: object) -> typing.Any: ...
def PyException_SetCause(__0: object, __1: object) -> None: ...
def PyException_SetContext(__0: object, __1: object) -> None: ...
def PyException_SetTraceback(__0: object, __1: object) -> int: ...

# PyFile

def PyFile_FromFd(__0: int, __1: bytes, __2: bytes, __3: int, __4: bytes, __5: bytes, __6: bytes, __7: int) -> typing.Any: ...
def PyFile_GetLine(__0: object, __1: int) -> typing.Any: ...
def PyFile_WriteObject(__0: object, __1: object, __2: int) -> int: ...
def PyFile_WriteString(__0: bytes, __1: object) -> int: ...

# PyFloat

def PyFloat_AS_DOUBLE(__0: object) -> float: ...
def PyFloat_AsDouble(__0: object) -> float: ...
def PyFloat_Check(__0: object) -> int: ...
def PyFloat_CheckExact(__0: object) -> int: ...
def PyFloat_FromDouble(__0: float) -> typing.Any: ...
def PyFloat_FromString(__0: object) -> typing.Any: ...
def PyFloat_GetInfo() -> typing.Any: ...

# PyFrozenSet

def PyFrozenSet_Check(__0: object) -> int: ...
def PyFrozenSet_CheckExact(__0: object) -> int: ...
def PyFrozenSet_New(__0: object) -> typing.Any: ...

# PyFunction

def PyFunction_Check(__0: object) -> int: ...
def PyFunction_GetAnnotations(__0: object) -> typing.Any: ...
def PyFunction_GetClosure(__0: object) -> typing.Any: ...
def PyFunction_GetCode(__0: object) -> typing.Any: ...
def PyFunction_GetDefaults(__0: object) -> typing.Any: ...
def PyFunction_GetGlobals(__0: object) -> typing.Any: ...
def PyFunction_GetModule(__0: object) -> typing.Any: ...
def PyFunction_New(__0: object, __1: object) -> typing.Any: ...
def PyFunction_NewWithQualName(__0: object, __1: object, __2: object) -> typing.Any: ...
def PyFunction_SetAnnotations(__0: object, __1: object) -> int: ...
def PyFunction_SetClosure(__0: object, __1: object) -> int: ...
def PyFunction_SetDefaults(__0: object, __1: object) -> int: ...

# PyGen

def PyGen_Check(__0: object) -> int: ...
def PyGen_CheckExact(__0: object) -> int: ...

# PyImport

def PyImport_AddModule(__0: bytes) -> typing.Any: ...
def PyImport_AddModuleObject(__0: object) -> typing.Any: ...
def PyImport_Cleanup() -> None: ...
def PyImport_ExecCodeModule(__0: bytes, __1: object) -> typing.Any: ...
def PyImport_ExecCodeModuleEx(__0: bytes, __1: object, __2: bytes) -> typing.Any: ...
def PyImport_ExecCodeModuleObject(__0: object, __1: object, __2: object, __3: object) -> typing.Any: ...
def PyImport_ExecCodeModuleWithPathnames(__0: bytes, __1: object, __2: bytes, __3: bytes) -> typing.Any: ...
def PyImport_GetImporter(__0: object) -> typing.Any: ...
def PyImport_GetMagicNumber() -> int: ...

if (3, 7, 0, "final", 0) <= sys.version_info:

    def PyImport_GetModule(__0: object) -> typing.Any: ...

def PyImport_GetModuleDict() -> typing.Any: ...
def PyImport_Import(__0: object) -> typing.Any: ...
def PyImport_ImportFrozenModule(__0: bytes) -> int: ...
def PyImport_ImportFrozenModuleObject(__0: object) -> int: ...
def PyImport_ImportModule(__0: bytes) -> typing.Any: ...
def PyImport_ImportModuleEx(__0: bytes, __1: object, __2: object, __3: object) -> typing.Any: ...
def PyImport_ImportModuleLevel(__0: bytes, __1: object, __2: object, __3: object, __4: int) -> typing.Any: ...
def PyImport_ImportModuleLevelObject(__0: object, __1: object, __2: object, __3: object, __4: int) -> typing.Any: ...
def PyImport_ImportModuleNoBlock(__0: bytes) -> typing.Any: ...
def PyImport_ReloadModule(__0: object) -> typing.Any: ...

# PyIndex

def PyIndex_Check(__0: object) -> int: ...

# PyInstanceMethod

def PyInstanceMethod_Check(__0: object) -> int: ...
def PyInstanceMethod_Function(__0: object) -> typing.Any: ...
def PyInstanceMethod_GET_FUNCTION(__0: object) -> typing.Any: ...
def PyInstanceMethod_New(__0: object) -> typing.Any: ...

# PyIter

def PyIter_Check(__0: object) -> int: ...
def PyIter_Next(__0: object) -> typing.Any: ...

# PyList

def PyList_Append(__0: object, __1: object) -> int: ...
def PyList_AsTuple(__0: object) -> typing.Any: ...
def PyList_Check(__0: object) -> int: ...
def PyList_CheckExact(__0: object) -> int: ...
def PyList_GET_ITEM(__0: object, __1: int) -> typing.Any: ...
def PyList_GET_SIZE(__0: object) -> int: ...
def PyList_GetItem(__0: object, __1: int) -> typing.Any: ...
def PyList_GetSlice(__0: object, __1: int, __2: int) -> typing.Any: ...
def PyList_Insert(__0: object, __1: int, __2: object) -> int: ...
def PyList_New(__0: int) -> typing.Any: ...
def PyList_Reverse(__0: object) -> int: ...
def PyList_SET_ITEM(__0: object, __1: int, __2: object) -> None: ...
def PyList_SetItem(__0: object, __1: int, __2: object) -> int: ...
def PyList_SetSlice(__0: object, __1: int, __2: int, __3: object) -> int: ...
def PyList_Size(__0: object) -> int: ...
def PyList_Sort(__0: object) -> int: ...

# PyLong

def PyLong_AsDouble(__0: object) -> float: ...
def PyLong_AsLong(__0: object) -> int: ...
def PyLong_AsLongLong(__0: object) -> int: ...
def PyLong_AsSsize_t(__0: object) -> int: ...
def PyLong_AsUnsignedLong(__0: object) -> int: ...
def PyLong_AsUnsignedLongLong(__0: object) -> int: ...
def PyLong_AsUnsignedLongLongMask(__0: object) -> int: ...
def PyLong_AsUnsignedLongMask(__0: object) -> int: ...
def PyLong_Check(__0: object) -> int: ...
def PyLong_CheckExact(__0: object) -> int: ...
def PyLong_FromLong(__0: int) -> typing.Any: ...

# PyMapping

def PyMapping_Check(__0: object) -> int: ...
def PyMapping_DelItem(__0: object, __1: object) -> int: ...
def PyMapping_DelItemString(__0: object, __1: bytes) -> int: ...
def PyMapping_GetItemString(__0: object, __1: bytes) -> typing.Any: ...
def PyMapping_HasKey(__0: object, __1: object) -> int: ...
def PyMapping_HasKeyString(__0: object, __1: bytes) -> int: ...
def PyMapping_Items(__0: object) -> typing.Any: ...
def PyMapping_Keys(__0: object) -> typing.Any: ...
def PyMapping_Length(__0: object) -> int: ...
def PyMapping_SetItemString(__0: object, __1: bytes, __2: object) -> int: ...
def PyMapping_Size(__0: object) -> int: ...
def PyMapping_Values(__0: object) -> typing.Any: ...

# PyMemoryView

def PyMemoryView_Check(__0: object) -> int: ...
def PyMemoryView_FromObject(__0: object) -> typing.Any: ...

# PyMethod

def PyMethod_Check(__0: object) -> int: ...
def PyMethod_Function(__0: object) -> typing.Any: ...
def PyMethod_GET_FUNCTION(__0: object) -> typing.Any: ...
def PyMethod_GET_SELF(__0: object) -> typing.Any: ...
def PyMethod_New(__0: object, __1: object) -> typing.Any: ...
def PyMethod_Self(__0: object) -> typing.Any: ...

# PyModule

def PyModule_Check(__0: object) -> int: ...
def PyModule_CheckExact(__0: object) -> int: ...
def PyModule_GetDict(__0: object) -> typing.Any: ...
def PyModule_GetFilename(__0: object) -> typing.Optional[bytes]: ...
def PyModule_GetFilenameObject(__0: object) -> typing.Any: ...
def PyModule_GetName(__0: object) -> typing.Optional[bytes]: ...
def PyModule_GetNameObject(__0: object) -> typing.Any: ...
def PyModule_NewObject(__0: object) -> typing.Any: ...

# PyNumber

def PyNumber_Absolute(__0: object) -> typing.Any: ...
def PyNumber_Add(__0: object, __1: object) -> typing.Any: ...
def PyNumber_And(__0: object, __1: object) -> typing.Any: ...
def PyNumber_AsSsize_t(__0: object, __1: object) -> int: ...
def PyNumber_Check(__0: object) -> int: ...
def PyNumber_Divmod(__0: object, __1: object) -> typing.Any: ...
def PyNumber_Float(__0: object) -> typing.Any: ...
def PyNumber_FloorDivide(__0: object, __1: object) -> typing.Any: ...
def PyNumber_InPlaceAdd(__0: object, __1: object) -> typing.Any: ...
def PyNumber_InPlaceAnd(__0: object, __1: object) -> typing.Any: ...
def PyNumber_InPlaceFloorDivide(__0: object, __1: object) -> typing.Any: ...
def PyNumber_InPlaceLshift(__0: object, __1: object) -> typing.Any: ...

if (3, 5, 0, "final", 0) <= sys.version_info:

    def PyNumber_InPlaceMatrixMultiply(__0: object, __1: object) -> typing.Any: ...

def PyNumber_InPlaceMultiply(__0: object, __1: object) -> typing.Any: ...
def PyNumber_InPlaceOr(__0: object, __1: object) -> typing.Any: ...
def PyNumber_InPlacePower(__0: object, __1: object, __2: object) -> typing.Any: ...
def PyNumber_InPlaceRemainder(__0: object, __1: object) -> typing.Any: ...
def PyNumber_InPlaceRshift(__0: object, __1: object) -> typing.Any: ...
def PyNumber_InPlaceSubtract(__0: object, __1: object) -> typing.Any: ...
def PyNumber_InPlaceTrueDivide(__0: object, __1: object) -> typing.Any: ...
def PyNumber_InPlaceXor(__0: object, __1: object) -> typing.Any: ...
def PyNumber_Index(__0: object) -> typing.Any: ...
def PyNumber_Invert(__0: object) -> typing.Any: ...
def PyNumber_Long(__0: object) -> typing.Any: ...
def PyNumber_Lshift(__0: object, __1: object) -> typing.Any: ...

if (3, 5, 0, "final", 0) <= sys.version_info:

    def PyNumber_MatrixMultiply(__0: object, __1: object) -> typing.Any: ...

def PyNumber_Multiply(__0: object, __1: object) -> typing.Any: ...
def PyNumber_Negative(__0: object) -> typing.Any: ...
def PyNumber_Or(__0: object, __1: object) -> typing.Any: ...
def PyNumber_Positive(__0: object) -> typing.Any: ...
def PyNumber_Power(__0: object, __1: object, __2: object) -> typing.Any: ...
def PyNumber_Remainder(__0: object, __1: object) -> typing.Any: ...
def PyNumber_Rshift(__0: object, __1: object) -> typing.Any: ...
def PyNumber_Subtract(__0: object, __1: object) -> typing.Any: ...
def PyNumber_ToBase(__0: object, __1: int) -> typing.Any: ...
def PyNumber_TrueDivide(__0: object, __1: object) -> typing.Any: ...
def PyNumber_Xor(__0: object, __1: object) -> typing.Any: ...

# PyOS

def PyOS_AfterFork() -> None: ...

if (3, 7, 0, "final", 0) <= sys.version_info:

    def PyOS_AfterFork_Child() -> None: ...
    def PyOS_AfterFork_Parent() -> None: ...
    def PyOS_BeforeFork() -> None: ...

if (3, 6, 0, "final", 0) <= sys.version_info:

    def PyOS_FSPath(__0: object) -> typing.Any: ...

# PyObject

def PyObject_ASCII(__0: object) -> typing.Any: ...
def PyObject_AsFileDescriptor(__0: object) -> int: ...
def PyObject_Bytes(__0: object) -> typing.Any: ...
def PyObject_Call(__0: object, __1: object, __2: object) -> typing.Any: ...
def PyObject_CallObject(__0: object, __1: object) -> typing.Any: ...
def PyObject_CheckBuffer(__0: object) -> int: ...
def PyObject_CheckReadBuffer(__0: object) -> int: ...
def PyObject_DelAttr(__0: object, __1: object) -> int: ...
def PyObject_DelItem(__0: object, __1: object) -> int: ...
def PyObject_Dir(__0: object) -> typing.Any: ...
def PyObject_GC_Track(__0: object) -> None: ...
def PyObject_GenericGetAttr(__0: object, __1: object) -> typing.Any: ...
def PyObject_GenericSetAttr(__0: object, __1: object, __2: object) -> int: ...
def PyObject_GetAttr(__0: object, __1: object) -> typing.Any: ...
def PyObject_GetItem(__0: object, __1: object) -> typing.Any: ...
def PyObject_GetIter(__0: object) -> typing.Any: ...
def PyObject_HasAttr(__0: object, __1: object) -> int: ...
def PyObject_Hash(__0: object) -> int: ...
def PyObject_IsInstance(__0: object, __1: object) -> int: ...
def PyObject_IsSubclass(__0: object, __1: object) -> int: ...
def PyObject_IsTrue(__0: object) -> int: ...
def PyObject_Length(__0: object) -> int: ...
def PyObject_Not(__0: object) -> int: ...
def PyObject_Repr(__0: object) -> typing.Any: ...
def PyObject_SetAttr(__0: object, __1: object, __2: object) -> int: ...
def PyObject_SetItem(__0: object, __1: object, __2: object) -> int: ...
def PyObject_Size(__0: object) -> int: ...
def PyObject_Str(__0: object) -> typing.Any: ...
def PyObject_Type(__0: object) -> typing.Any: ...

# PySeqIter

def PySeqIter_Check(__0: object) -> int: ...
def PySeqIter_New(__0: object) -> typing.Any: ...

# PySequence

def PySequence_Check(__0: object) -> int: ...
def PySequence_Concat(__0: object, __1: object) -> typing.Any: ...
def PySequence_Contains(__0: object, __1: object) -> int: ...
def PySequence_Count(__0: object, __1: object) -> int: ...
def PySequence_Fast_GET_SIZE(__0: object) -> int: ...
def PySequence_In(__0: object, __1: object) -> int: ...
def PySequence_InPlaceConcat(__0: object, __1: object) -> typing.Any: ...
def PySequence_Index(__0: object, __1: object) -> int: ...
def PySequence_List(__0: object) -> typing.Any: ...
def PySequence_Size(__0: object) -> int: ...
def PySequence_Tuple(__0: object) -> typing.Any: ...

# PySet

def PySet_Add(__0: object, __1: object) -> int: ...
def PySet_Check(__0: object) -> int: ...
def PySet_Clear(__0: object) -> int: ...
def PySet_Contains(__0: object, __1: object) -> int: ...
def PySet_Discard(__0: object, __1: object) -> int: ...
def PySet_GET_SIZE(__0: object) -> int: ...
def PySet_New(__0: object) -> typing.Any: ...
def PySet_Pop(__0: object) -> typing.Any: ...
def PySet_Size(__0: object) -> int: ...

# PySignal

def PySignal_SetWakeupFd(__0: int) -> int: ...

# PySlice

def PySlice_Check(__0: object) -> int: ...
def PySlice_New(__0: object, __1: object, __2: object) -> typing.Any: ...

# PySys

def PySys_AddWarnOptionUnicode(__0: object) -> None: ...
def PySys_GetXOptions() -> typing.Any: ...
def PySys_ResetWarnOptions() -> None: ...

# PyThreadState

def PyThreadState_GetDict() -> typing.Any: ...

if (3, 7, 0, "final", 0) <= sys.version_info:

    # PyTimeZone

    def PyTimeZone_FromOffset(__0: object) -> typing.Any: ...
    def PyTimeZone_FromOffsetAndName(__0: object, __1: object) -> typing.Any: ...

# PyTime

def PyTime_Check(__0: object) -> int: ...
def PyTime_CheckExact(__0: object) -> int: ...
def PyTime_FromTime(__0: int, __1: int, __2: int, __3: int) -> typing.Any: ...

# PyTuple

def PyTuple_Check(__0: object) -> int: ...
def PyTuple_CheckExact(__0: object) -> int: ...
def PyTuple_GET_ITEM(__0: object, __1: int) -> typing.Any: ...
def PyTuple_GET_SIZE(__0: object) -> int: ...
def PyTuple_GetItem(__0: object, __1: int) -> typing.Any: ...
def PyTuple_GetSlice(__0: object, __1: int, __2: int) -> typing.Any: ...
def PyTuple_New(__0: int) -> typing.Any: ...
def PyTuple_SET_ITEM(__0: object, __1: int, __2: object) -> None: ...
def PyTuple_SetItem(__0: object, __1: int, __2: object) -> int: ...
def PyTuple_Size(__0: object) -> int: ...

# PyType

def PyType_Check(__0: object) -> int: ...
def PyType_CheckExact(__0: object) -> int: ...

# PyUnicodeDecodeError

def PyUnicodeDecodeError_GetEncoding(__0: object) -> typing.Any: ...
def PyUnicodeDecodeError_GetObject(__0: object) -> typing.Any: ...
def PyUnicodeDecodeError_GetReason(__0: object) -> typing.Any: ...

# PyUnicode

def PyUnicode_AS_DATA(__0: object) -> typing.Optional[bytes]: ...
def PyUnicode_AS_UNICODE(__0: object) -> typing.Optional[str]: ...
def PyUnicode_AsASCIIString(__0: object) -> typing.Any: ...
def PyUnicode_AsCharmapString(__0: object, __1: object) -> typing.Any: ...
def PyUnicode_AsLatin1String(__0: object) -> typing.Any: ...

if sys.platform == "win32":

    def PyUnicode_AsMBCSString(__0: object) -> typing.Any: ...

def PyUnicode_AsRawUnicodeEscapeString(__0: object) -> typing.Any: ...
def PyUnicode_AsUTF16String(__0: object) -> typing.Any: ...
def PyUnicode_AsUTF32String(__0: object) -> typing.Any: ...
def PyUnicode_AsUTF8(__0: object) -> typing.Optional[bytes]: ...
def PyUnicode_AsUTF8String(__0: object) -> typing.Any: ...
def PyUnicode_AsUnicode(__0: object) -> typing.Optional[str]: ...
def PyUnicode_AsUnicodeCopy(__0: object) -> typing.Optional[str]: ...
def PyUnicode_AsUnicodeEscapeString(__0: object) -> typing.Any: ...
def PyUnicode_Check(__0: object) -> int: ...
def PyUnicode_CheckExact(__0: object) -> int: ...
def PyUnicode_Compare(__0: object, __1: object) -> int: ...
def PyUnicode_Concat(__0: object, __1: object) -> typing.Any: ...
def PyUnicode_Contains(__0: object, __1: object) -> int: ...
def PyUnicode_EncodeFSDefault(__0: object) -> typing.Any: ...
def PyUnicode_Format(__0: object, __1: object) -> typing.Any: ...
def PyUnicode_FromObject(__0: object) -> typing.Any: ...
def PyUnicode_GET_DATA_SIZE(__0: object) -> int: ...
def PyUnicode_GET_LENGTH(__0: object) -> int: ...
def PyUnicode_GET_SIZE(__0: object) -> int: ...
def PyUnicode_GetLength(__0: object) -> int: ...
def PyUnicode_GetSize(__0: object) -> int: ...
def PyUnicode_Join(__0: object, __1: object) -> typing.Any: ...
def PyUnicode_KIND(__0: object) -> int: ...
def PyUnicode_READY(__0: object) -> int: ...

# PyWeakref

def PyWeakref_Check(__0: object) -> int: ...
def PyWeakref_CheckProxy(__0: object) -> int: ...
def PyWeakref_CheckRef(__0: object) -> int: ...
def PyWeakref_GET_OBJECT(__0: object) -> typing.Any: ...
def PyWeakref_GetObject(__0: object) -> typing.Any: ...
def PyWeakref_NewProxy(__0: object, __1: object) -> typing.Any: ...
def PyWeakref_NewRef(__0: object, __1: object) -> typing.Any: ...

# PyWrapper

def PyWrapper_New(__0: object, __1: object) -> typing.Any: ...

# Py

def Py_CLEAR(__0: object) -> None: ...
def Py_DECREF(__0: object) -> None: ...
def Py_Finalize() -> None: ...
def Py_GetBuildInfo() -> typing.Optional[bytes]: ...
def Py_GetCompiler() -> typing.Optional[bytes]: ...
def Py_GetCopyright() -> typing.Optional[bytes]: ...
def Py_GetExecPrefix() -> typing.Optional[str]: ...
def Py_GetPath() -> typing.Optional[str]: ...
def Py_GetPlatform() -> typing.Optional[bytes]: ...
def Py_GetPrefix() -> typing.Optional[str]: ...
def Py_GetProgramFullPath() -> typing.Optional[str]: ...
def Py_GetProgramName() -> typing.Optional[str]: ...
def Py_GetVersion() -> typing.Optional[bytes]: ...
def Py_INCREF(__0: object) -> None: ...
def Py_Initialize() -> None: ...
def Py_IsInitialized() -> int: ...
def Py_ReprEnter(__0: object) -> int: ...
def Py_ReprLeave(__0: object) -> None: ...
def Py_XDECREF(__0: object) -> None: ...
def Py_XINCREF(__0: object) -> None: ...
