@ECHO OFF

stream_watchmegrow.bat  %1 >> E:\Projects\Downloads\watchmegrow\log_cam%1.txt 2>&1

if %ERRORLEVEL% NEQ 0 (
	ECHO bat: stream_watchmegrow failed with non-zero code
	EXIT /B 2
)

ECHO bat: stream_watchmegrow terminated successfully.