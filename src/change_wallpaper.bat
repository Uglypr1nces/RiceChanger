@echo off
setlocal

rem Set the path to wallpaper_id.txt
set "filename=%~dp0wallpaper_id.txt"

rem Read the content of wallpaper_id.txt and store it in wallpaper_id
for /f "usebackq delims=" %%i in ("%filename%") do (
    set "wallpaper_id=%%i"
)

rem Verify the wallpaper_id value
echo Wallpaper ID: %wallpaper_id%
echo Wallpaper Path: C:\Program Files (x86)\Steam\steamapps\workshop\content\431960\%wallpaper_id%\project.json

rem Construct the wallpaper path
set "wallpaper_path=C:\Program Files (x86)\Steam\steamapps\workshop\content\431960\%wallpaper_id%\project.json"

rem Run Wallpaper Engine with the constructed path
"C:\Program Files (x86)\Steam\steamapps\common\wallpaper_engine\wallpaper64.exe" -control openWallpaper -file "%wallpaper_path%"

endlocal
