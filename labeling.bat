
setlocal enabledelayedexpansion
dir /b /ad > list.txt

mkdir files
set FILESPATH=%cd%\files

findstr /r "\." checklist.txt > fullist.txt
findstr /r "^[^\.]*$" checklist.txt > explist.txt

for /f "delims=" %%i in (list.txt) do (
  cd %%i
  for /f "delims= " %%j in (%cd%\fullist.txt) do (
    if exist check (
      dir /s /b | find /i "\%%j" >> check
    ) else (
      dir /s /b | find /i "\%%j" > check
    )
  )
  for /f "delims= " %%j in (%cd%\explist.txt) do (
    if exist check (
      dir /s /b | find /i ".%%j" >> check
    ) else (
      dir /s /b | find /i ".%%j" > check
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
del fullist.txt
del explist.txt
pause
endlocal