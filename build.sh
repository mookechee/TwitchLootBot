#!/usr/bin/env bash

# 获取脚本所在目录
DIRPATH=$(dirname "$(readlink -f "$0")")

# 检查虚拟环境是否存在
if [ ! -d "$DIRPATH/env" ]; then
    echo "\n[错误] 未找到虚拟环境！请先运行 setup_env.sh 设置环境。\n"
    exit 1
fi

# 检查 PyInstaller 是否已安装
if [ ! -f "$DIRPATH/env/bin/pyinstaller" ]; then
    echo "\n[信息] 正在安装 PyInstaller...\n"
    "$DIRPATH/env/bin/pip" install pyinstaller
    if [ $? -ne 0 ]; then
        echo "\n[错误] PyInstaller 安装失败。\n"
        exit 1
    fi
fi

# 打包 macOS 应用
echo "\n[信息] 正在为 macOS 构建 .app 文件...\n"
"$DIRPATH/env/bin/pyinstaller" \
    --windowed \
    --onedir \
    --noconfirm \
    --name "TwitchLootBot" \
    --osx-bundle-identifier "com.twitch.lootbot" \
    --icon "$DIRPATH/icons/pickaxe.icns" \
    --add-data "$DIRPATH/icons:icons" \
    --add-data "$DIRPATH/lang:lang" \
    "$DIRPATH/main.py"

if [ $? -ne 0 ]; then
    echo "\n[错误] PyInstaller 构建失败。\n"
    exit 1
fi

# 打包完成
echo "\n[成功] 构建完成！生成的 .app 文件位于 dist/ 目录下。\n"
