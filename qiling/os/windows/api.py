#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

from qiling.os.const import *

LOCALE_T = INT
ULONG = PARAM_INTN
CCHAR = PARAM_INT8
CHAR = PARAM_INT8
UCHAR = PARAM_INT16
USHORT = PARAM_INT16
SHORT = PARAM_INT16

# ntoskrnl workarounds:
BOOLEAN = INT
PANSI_STRING = STRING
PCANSI_STRING = STRING
PCSZ = STRING
PCWSTR = WSTRING
PCUNICODE_STRING = WSTRING
PUNICODE_STRING = WSTRING
WCHAR = PARAM_INT16

# a lookup table used by winapisdk to substitute certain type names with others
reptypedict = {
    "BSTR"                          : POINTER,
    "DLGPROC"                       : POINTER,
    "DWORDLONG"                     : ULONGLONG,
    "DWORD_PTR"                     : POINTER,
    "GROUP"                         : INT,
    "HBITMAP"                       : HANDLE,
    "HDC"                           : POINTER,
    "HEAP_INFORMATION_CLASS"        : UINT,
    "HGLOBAL"                       : POINTER,
    "HIMAGELIST"                    : HANDLE,
    "HHOOK"                         : POINTER,
    "HINSTANCE"                     : HANDLE,
    "HINTERNET"                     : POINTER,
    "HKEY"                          : HANDLE,
    "HLOCAL"                        : POINTER,
    "HMODULE"                       : HANDLE,
    "HOOKPROC"                      : POINTER,
    "HRSRC"                         : POINTER,
    "HWND"                          : HANDLE,
    "INSTALLSTATE"                  : POINTER,
    "INTERNET_PORT"                 : DWORD,
    "INT_PTR"                       : POINTER,
    "LARGE_INTEGER"                 : POINTER,
    "LCID"                          : POINTER,
    "LONG"                          : ULONGLONG,
    "LPARAM"                        : POINTER,
    "LPBOOL"                        : POINTER,
    "LPBYTE"                        : POINTER,
    "LPCCH"                         : POINTER,
    "LPCONTEXT"                     : POINTER,
    "LPCPINFO"                      : POINTER,
    "LPCRITICAL_SECTION"            : POINTER,
    "LPCSTR"                        : STRING,
    "LPCVOID"                       : POINTER,
    "LPCWCH"                        : POINTER,
    "LPCWSTR"                       : WSTRING,
    "LPDWORD"                       : POINTER,
    "LPFILETIME"                    : POINTER,
    "LPINTERNET_BUFFERSA"           : POINTER,
    "LPMESSAGEFILTER"               : POINTER,
    "LPMODULEINFO"                  : POINTER,
    "LPNLSVERSIONINFO"              : POINTER,
    "LPOSVERSIONINFOA"              : STRING,
    "LPOSVERSIONINFOEXW"            : POINTER,
    "LPOSVERSIONINFOW"              : WSTRING,
    "LPOVERLAPPED"                  : POINTER,
    "LPPOINT"                       : POINTER,
    "LPPROCESSENTRY32W"             : POINTER,
    "LPSECURITY_ATTRIBUTES"         : POINTER,
    "LPSTARTUPINFOA"                : POINTER,
    "LPSTARTUPINFOW"                : POINTER,
    "LPSTR"                         : POINTER,
    "LPSTREAM"                      : POINTER,
    "LPSYSTEMTIME"                  : POINTER,
    "LPSYSTEM_INFO"                 : POINTER,
    "LPTHREAD_START_ROUTINE"        : POINTER,
    "LPTOP_LEVEL_EXCEPTION_FILTER"  : DWORD,
    "LPUNKNOWN"                     : POINTER,
    "LPVOID"                        : POINTER,
    "LPWCH"                         : POINTER,
    "LPWIN32_FIND_DATAA"            : POINTER,
    "LPWORD"                        : POINTER,
    "LPWSADATA"                     : STRING,
    "LPWSAPROTOCOL_INFOA"           : POINTER,
    "LPWSTR"                        : POINTER,
    "MSIHANDLE"                     : POINTER,
    "OBJECT_INFORMATION_CLASS"      : INT,
    "OLECHAR"                       : WSTRING,
    "PANSI_STRING"                  : STRING,
    "PBOOL"                         : POINTER,
    "PCACTCTXW"                     : POINTER,
    "PCANSI_STRING"                 : STRING,
    "PCNZCH"                        : STRING,
    "PCSZ"                          : STRING,
    "PCWSTR"                        : WSTRING,
    "PDWORD"                        : POINTER,
    "PFLS_CALLBACK_FUNCTION"        : POINTER,
    "PHKEY"                         : POINTER,
    "PMEMORY_BASIC_INFORMATION"     : POINTER,
    "PROCESSINFOCLASS"              : INT,
    "PSECURITY_DESCRIPTOR"          : POINTER,
    "PSID"                          : HANDLE,
    "PSID_IDENTIFIER_AUTHORITY"     : POINTER,
    "PSLIST_HEADER"                 : POINTER,
    "PSRWLOCK"                      : POINTER,
    "PTP_POOL"                      : POINTER,
    "PULONG"                        : POINTER,
    "PVECTORED_EXCEPTION_HANDLER"   : HANDLE,
    "PVOID"                         : POINTER,
    "PWSTR"                         : WSTRING,
    "REFCLSID"                      : POINTER,
    "REFIID"                        : POINTER,
    "REGSAM"                        : POINTER,
    "SC_HANDLE"                     : HANDLE,
    "SHELLEXECUTEINFOA"             : POINTER,
    "SHELLEXECUTEINFOW"             : POINTER,
    "SHFILEINFOW"                   : POINTER,
    "SOCKET"                        : INT,
    "SOLE_AUTHENTICATION_SERVICE"   : POINTER,
    "TOKEN_INFORMATION_CLASS"       : DWORD,
    "UINT_PTR"                      : POINTER,
    "ULONG"                         : UINT,
    "ULONG_PTR"                     : POINTER,
    "WER_REGISTER_FILE_TYPE"        : INT,
    "WORD"                          : DWORD,
    "WPARAM"                        : UINT,
    "_EXCEPTION_POINTERS"           : POINTER,
    "int"                           : INT,
    "size_t"                        : SIZE_T,
    "sockaddr"                      : POINTER,
    "unsigned int"                  : UINT,
    "void"                          : POINTER,

    # work around the need of "eval"
    "POINTER" : POINTER,
    "BOOL"    : BOOL,
    "BYTE"    : BYTE,
    "DWORD"   : DWORD,
    "HANDLE"  : HANDLE,
    "SIZE_T"  : SIZE_T,
    "UINT"    : UINT,
    "WSTRING" : WSTRING
}
