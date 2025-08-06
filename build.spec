# -*- mode: python ; coding: utf-8 -*-
from __future__ import annotations

import sys
import platform
import fnmatch
from pathlib import Path
from typing import Any, TYPE_CHECKING

SELF_PATH = str(Path(".").resolve())
if SELF_PATH not in sys.path:
    sys.path.insert(0, SELF_PATH)

from constants import WORKING_DIR, SITE_PACKAGES_PATH, DEFAULT_LANG

if TYPE_CHECKING:
    from PyInstaller.building.api import PYZ, EXE
    from PyInstaller.building.build_main import Analysis


# (source_path, dest_path, required)
to_add: list[tuple[Path, str, bool]] = [
    # icon files
    (Path("icons/pickaxe.ico"), "./icons", True),
    (Path("icons/active.ico"), "./icons", True),
    (Path("icons/idle.ico"), "./icons", True),
    (Path("icons/error.ico"), "./icons", True),
    (Path("icons/maint.ico"), "./icons", True),
    # SeleniumWire HTTPS/SSL cert file and key
    (Path(SITE_PACKAGES_PATH, "seleniumwire/ca.crt"), "./seleniumwire", False),
    (Path(SITE_PACKAGES_PATH, "seleniumwire/ca.key"), "./seleniumwire", False),
]
for lang_filepath in WORKING_DIR.joinpath("lang").glob("*.json"):
    if lang_filepath.stem != DEFAULT_LANG:
        to_add.append((lang_filepath, "lang", True))

# Ensure the required to-be-added data exists
datas: list[tuple[Path, str]] = []
for source_path, dest_path, required in to_add:
    if source_path.exists():
        datas.append((source_path, dest_path))
    elif required:
        raise FileNotFoundError(str(source_path))

hooksconfig: dict[str, Any] = {}
binaries: list[tuple[Path, str]] = []
hiddenimports: list[str] = [
    "PIL._tkinter_finder",
    "setuptools._distutils.log",
    "setuptools._distutils.dir_util",
    "setuptools._distutils.file_util",
    "setuptools._distutils.archive_util",
]

if sys.platform == "linux":
    # Needed files for better system tray support on Linux via pystray (AppIndicator backend).
    arch: str = platform.machine()
    libraries_path: Path = Path(f"/usr/lib/{arch}-linux-gnu")
    if not libraries_path.exists():
        libraries_path = Path("/usr/lib64")
    datas.append(
        (libraries_path / "girepository-1.0/AyatanaAppIndicator3-0.1.typelib", "gi_typelibs")
    )
    binaries.append((libraries_path / "libayatana-appindicator3.so.1", "."))

    hiddenimports.extend([
        "gi.repository.Gtk",
        "gi.repository.GObject",
    ])
    hooksconfig = {
        "gi": {
            "icons": [],
            "themes": [],
            "languages": ["en_US"]
        }
    }
elif sys.platform == "darwin":
    app_name = "Twitch Drops Miner (by DevilXD).app"
    app_dir = Path("dist") / app_name

    # Create .app structure manually
    app_dir.mkdir(parents=True, exist_ok=True)
    (app_dir / "Contents").mkdir(exist_ok=True)
    (app_dir / "Contents" / "MacOS").mkdir(exist_ok=True)
    (app_dir / "Contents" / "Resources").mkdir(exist_ok=True)

    # Debug: Print the contents of the 'dist' directory
    print("Contents of 'dist' directory:", list(Path("dist").iterdir()))

    # Dynamically check the generated executable file name, excluding .app files
    exe_path = next((p for p in Path("dist").glob("Twitch Drops Miner (by DevilXD)*") if not p.suffix == ".app"), None)
    if exe_path is None:
        raise FileNotFoundError("Generated executable not found in 'dist' directory.")

    # Debug: Print the matched executable path
    print("Matched executable path:", exe_path)

    # Move the executable to the .app bundle
    exe_path.rename(app_dir / "Contents" / "MacOS" / "Twitch Drops Miner (by DevilXD)")

    # Add Info.plist for macOS app metadata
    plist_content = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">
<plist version=\"1.0\">
<dict>
    <key>CFBundleName</key>
    <string>Twitch Drops Miner (by DevilXD)</string>
    <key>CFBundleExecutable</key>
    <string>Twitch Drops Miner (by DevilXD)</string>
    <key>CFBundleIconFile</key>
    <string>pickaxe.icns</string>
    <key>CFBundleIdentifier</key>
    <string>com.devilxd.twitchdropsminer</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
</dict>
</plist>
"""
    (app_dir / "Contents" / "Info.plist").write_text(plist_content)

    # Copy the icon to the Resources folder
    icon_path = Path("icons") / "pickaxe.icns"
    if icon_path.exists():
        (app_dir / "Contents" / "Resources" / "pickaxe.icns").write_bytes(icon_path.read_bytes())

    hiddenimports.extend([
        "PyObjCTools",  # Example macOS-specific hidden import
    ])

    hooksconfig = {
        "gi": {
            "icons": [],
            "themes": [],
            "languages": ["en_US"]
        }
    }

block_cipher = None
a = Analysis(
    ["main.py"],
    pathex=[],
    datas=datas,
    excludes=[],
    hookspath=[],
    noarchive=False,
    runtime_hooks=[],
    binaries=binaries,
    cipher=block_cipher,
    hooksconfig=hooksconfig,
    hiddenimports=hiddenimports,
    win_private_assemblies=False,
    win_no_prefer_redirects=False,
)

# Exclude unneeded Linux libraries (supports globbing)
excluded_binaries = [
    "libicudata.so.*",
    "libicuuc.so.*",
    "librsvg-*.so.*"
]
a.binaries = [
    b for b in a.binaries
    if not any(fnmatch.fnmatch(b[0], pattern) for pattern in excluded_binaries)
]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    upx=True,
    debug=False,
    strip=False,
    console=False,  # Disable console for GUI application
    upx_exclude=[],
    target_arch=None,
    runtime_tmpdir=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(icon_path) if sys.platform == "darwin" else "icons/pickaxe.ico",
    bootloader_ignore_signals=False,
    disable_windowed_traceback=False,
    name="Twitch Drops Miner (by DevilXD)",
)
