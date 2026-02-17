@echo off
setlocal EnableExtensions
cd /d "%~dp0"

if "%~1"=="__anim" goto anim

title ASM Setup
mode con: cols=100 lines=35

if not exist banner.txt (
echo banner.txt missing
pause
exit /b
)

start "" /b cmd /c "%~f0" __anim

start "" /b cmd /c "pip install -r requirements.txt > install.log 2>&1 & echo done>install.done"

:wait
if not exist install.done (
    >nul ping -n 1 -w 200 127.0.0.1
    goto wait
)

taskkill /f /fi "WINDOWTITLE eq ASM_ANIM" >nul 2>&1
del install.done >nul 2>&1

cls
type banner.txt
echo.
echo ASM is fully setup!
echo Check install.log if something failed.
echo.
start main.py
pause
exit /b


:anim
title ASM_ANIM
for /f %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"
set colors=196 202 208 214 220 226 190 154 118 82 46 47 48 49 51 45 39 33 27 21 57 93 129 165
set shift=0

for /f "usebackq delims=" %%L in ("banner.txt") do echo.

:loop
<nul set /p ="%ESC%[H"
setlocal DisableDelayedExpansion
set lineIndex=0
for /f "usebackq delims=" %%L in ("banner.txt") do (
    set /a pick=lineIndex+shift
    set /a pick=pick%%24
    call set "line=%%L"
    setlocal EnableDelayedExpansion
    set i=0
    for %%C in (%colors%) do (
        if !i! EQU !pick! (
            <nul set /p ="!ESC![38;5;%%Cm!line!!ESC![0m"
            echo.
        )
        set /a i+=1
    )
    endlocal
    set /a lineIndex+=1
)
endlocal
set /a shift+=1

if exist install.done exit
>nul ping -n 1 -w 75 127.0.0.1
goto loop