
setlocal enabledelayedexpansion
dir /b /ad > list

mkdir files
set FILESPATH=%cd%\files
set numfiles=0

for /f "delims=" %%i in (list) do (
  for /f "delims=" %%j in (checklist.txt) do (
    cd %%i
    dir /s /b | find /i "%%j" > dircheck
    dir /s
    set numfiles=0
    for /f "delims=" %%k in (check) do (
      set /a numfiles+=1
      cd %FILESPATH%
      copy %%k %FILESPATH%
      ren %%j "%%i!numfiles!-%%j"
    )
    @cd "%cd%\%%i"
    @del check
    @cd %cd%
  )
)
del list
pause
endlocal