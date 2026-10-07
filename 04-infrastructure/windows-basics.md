# Windows Basics Lab

## PowerShell commands

```powershell
Get-Process
Get-Service
Get-NetIPAddress
Get-NetTCPConnection
Get-WinEvent -LogName System -MaxEvents 20
```

## Exercise

Choose one listening TCP port and determine:

1. local address and port;
2. owning process;
3. process executable/name;
4. related service, if any;
5. whether the exposure is expected.
