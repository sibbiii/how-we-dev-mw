@echo off
for /l %%x in (1, 1, 10) do echo.
echo ---------------------------------------
for /l %%x in (1, 1, 10) do echo.

call make epub
if %errorlevel% neq 0 exit /b %errorlevel%
call make html
if %errorlevel% neq 0 exit /b %errorlevel%

echo.
echo --- all ok ---
