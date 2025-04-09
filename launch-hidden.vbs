Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File ""{app}\watch-msfs.ps1"" -ExecutablePath ""{app}\msfs-state-modifier.exe""", 0
