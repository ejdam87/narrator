Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Docs\Git\narrator\intro_runner.bat" & Chr(34), 0
Set WshShell = Nothing