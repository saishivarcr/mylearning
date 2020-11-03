# Dynamic-Link Library
A DLL is a library that contains code and data that can be used by more than one program at the same time. 

Detailed Read: [Microsoft Support](https://support.microsoft.com/en-in/help/815065/what-is-a-dll)

## DLL Search Order
Before system searches for DLL, it checks for these two conditions
1. If DLL with same modules name already loaded in memory, the system uses the loaded DLL no matter which directory it is in. The system does not search for the DLL.
1. If the DLL is on the list of known DLLs. For a list of known DLLs on the current system, see the following registry key: **HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs**

Detailed Read: [Microsoft Support](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order)