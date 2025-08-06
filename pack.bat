@echo off
IF NOT EXIST 7z.exe GOTO NO7Z
IF NOT EXIST "TwitchLootBot" mkdir "TwitchLootBot"
rem Prepare files
copy /y /v dist\*.exe "TwitchLootBot"
copy /y /v manual.txt "TwitchLootBot"
IF EXIST "TwitchLootBot.zip" (
    rem Add action
    set action=a
) ELSE (
    rem Update action
    set action=u
)
rem Pack and test
7z %action% "TwitchLootBot.zip" "TwitchLootBot/" -r
7z t "TwitchLootBot.zip" * -r
rem Cleanup
IF EXIST "TwitchLootBot" rmdir /s /q "TwitchLootBot"
GOTO EXIT
:NO7Z
echo No 7z.exe detected, skipping packaging!
GOTO EXIT
:EXIT
exit %errorlevel%
