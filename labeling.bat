
setlocal enabledelayedexpansion
dir /b /ad > list.txt

mkdir files
set FILESPATH=%cd%\files

for /f "delims=" %%i in (list.txt) do (
  for /f "delims= " %%j in (checklist.txt) do (
    cd %%i
    if exist check (
      dir /s /b | find /i "%%j" >> check
    ) else (
      dir /s /b | find /i "%%j" > check
    )
  )
  set numfiles=0
  for /f "delims=" %%k in (check) do (
    cd %FILESPATH%
    copy %%k %FILESPATH%
    if exist %%~nk%%~xk (
      set /a numfiles+=1
    )
    ren %%~nk%%~xk "%%i!numfiles!-%%~nk%%~xk"
  )
  cd "%cd%\%%i"
  del check
  cd %cd%
)
del list.txt
pause
endlocal