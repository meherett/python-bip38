#!/usr/bin/env python3

# Copyright © 2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from cx_Freeze import setup, Executable

from desktop.info import __version__ as version  

app_name  = "BIP38"
icon_path = "desktop/ui/images/icon/icon.ico"

msi_shortcut_table = [
    (
        "DesktopShortcut",             # Shortcut
        "DesktopFolder",               # Directory_
        app_name,                      # Name that will be show on the link
        "TARGETDIR",                   # Component_
        f"[TARGETDIR]{app_name}.exe",  # Target exe to exexute
        None,                          # Arguments
        None,                          # Description
        None,                          # Hotkey
        None,                          # Icon
        None,                          # IconIndex
        None,                          # ShowCmd
        'TARGETDIR'                    # WkDir
    )
]

msi_directory_table = [
    ("ProgramMenuFolder", "TARGETDIR", "."),
    ("BIP38Menu", "ProgramMenuFolder", "BIP38~1|BIP38")
]

msi_data = {
    "Shortcut": msi_shortcut_table,
    "Directory": msi_directory_table
}

bdist_msi_opt = {
    "add_to_path": False,
    "data": msi_data,
    "initial_target_dir": f"[ProgramFiles64Folder]\\{app_name}",
    "install_icon": icon_path,
    "upgrade_code": "{E4A369F6-FC76-3013-A420-3BB9B370711C}"
}

build_exe_opt = {
    "packages": ["_scrypt"],
    "excludes": ["tkinter"],
    "include_msvcr": True
}

executables = [
    Executable(
        "launch.py",
        base="gui",
        icon=icon_path,
        target_name=app_name,
        shortcut_name=app_name,
        shortcut_dir="BIP38Menu",
        copyright=f"Copyright (C) 2024 {app_name}"
    )
]

setup(
    name=app_name,
    version=version,
    executables=executables,
    options={
        "build_exe": build_exe_opt,
        "bdist_msi": bdist_msi_opt
    }
)