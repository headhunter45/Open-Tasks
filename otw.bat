@echo off
set "PROJ_ROOT=%~dp0"
set "BIN=%PROJ_ROOT%.ot\bin\ot.zipapp"

if exist "%BIN%" (
    python "%BIN%" %*
) else (
    ot %*
)
