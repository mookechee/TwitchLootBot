# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/mookechee/Code/TwitchLootBot/main.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/mookechee/Code/TwitchLootBot/icons', 'icons'), ('/Users/mookechee/Code/TwitchLootBot/lang', 'lang')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='TwitchLootBot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/Users/mookechee/Code/TwitchLootBot/icons/pickaxe.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='TwitchLootBot',
)
app = BUNDLE(
    coll,
    name='TwitchLootBot.app',
    icon='/Users/mookechee/Code/TwitchLootBot/icons/pickaxe.icns',
    bundle_identifier='com.twitch.lootbot',
)
