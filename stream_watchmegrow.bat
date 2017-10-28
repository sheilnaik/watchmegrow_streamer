@ECHO OFF
SETLOCAL

REM load environment (username, password, media_dir)
IF NOT EXIST load_credentials.bat (
	ECHO bat: missing load_credentials.bat FILE.
	EXIT /B 2
)

CALL load_credentials.bat

REM execute streamer. We are assuming Python is in the user's PATH environ variable.
ECHO bat: calling  ^=^=^> stream_watchmegrow.py %1
python stream_watchmegrow.py %1

if %ERRORLEVEL% NEQ 0 (
	ECHO bat: stream_watchmegrow.py failed with non-zero code.
	ENDLOCAL
	EXIT /B 2
)

ECHO bat: stream_watchmegrow.py succeeded.

ENDLOCAL

