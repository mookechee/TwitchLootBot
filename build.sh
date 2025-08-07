#!/usr/bin/env bash

dirpath=$(dirname "$(readlink -f "$0")")

# Check if the virtual environment exists
if [ ! -d "$dirpath/env" ]; then
    echo
    echo "No virtual environment found! Run setup_env.sh to set it up first."
    echo
    read -p "Press any key to continue..."
    exit 1
fi

# Check if PyInstaller is installed in the virtual environment
if [ ! -f "$dirpath/env/bin/pyinstaller" ]; then
    echo
    echo "Installing PyInstaller..."
    "$dirpath/env/bin/pip" install pyinstaller
    if [ $? -ne 0 ]; then
        echo
        echo "Failed to install PyInstaller."
        echo
        read -p "Press any key to continue..."
        exit 1
    fi
fi

# Run PyInstaller with the specified build spec file
echo
echo
echo "Building .app for macOS..."
# 生成 .app 文件，假设 main.py 为入口文件，可根据实际情况调整
"$dirpath/env/bin/pyinstaller" --windowed --onefile --name "TwitchLootBot" --osx-bundle-identifier "com.twitch.lootbot" "$dirpath/main.py"
if [ $? -ne 0 ]; then
    echo
    echo "PyInstaller build failed."
    echo
    read -p "Press any key to continue..."
    exit 1
fi


echo "Build completed successfully."
echo
read -p "Press any key to continue..."
