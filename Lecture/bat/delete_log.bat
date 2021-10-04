forfiles /P "%~dp0..\log" /S /M *.log* /D -15 /C "cmd /c del @file"
timeout 5