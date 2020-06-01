
setlocal enabledelayedexpansion
dir /b /ad > list.txt

mkdir files
set FILESPATH=%cd%\files
set numfiles=0

for /f "delims=" %%i in (list.txt) do (
  for /f "delims=" %%j in (checklist.txt) do (
    cd %%i
    dir /s /b | find /i "%%j" > check.txt
    set numfiles=0
    for /f "delims=" %%k in (check.txt) do (
      set /a numfiles+=1
      cd %FILESPATH%
      copy %%k %FILESPATH%
      ren %%~nk%%~xk "%%i!numfiles!-%%~nk%%~xk"
    )
    cd "%cd%\%%i"
    del check.txt
    cd %cd%
  )
)
del list.txt
pause
endlocal