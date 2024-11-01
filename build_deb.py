#!/usr/bin/env python3

from pathlib import Path
from glob import glob

import sys
import shutil
import platform
import subprocess

from bip38.info import __author__ as maintainer, __description__, __name__
from desktop.info import __version__ as app_version

arch_map = {
    "x86_64": "amd64",
    "aarch64": "arm64",
    "armv7l": "armhf",
    "i386": "i386",
}
machine_arch = arch_map.get(platform.machine(), platform.machine()) 

if platform.system() != "Linux":
    print("Unable to create a .deb package on a non-Linux system!")
    sys.exit(1)


app_version = app_version.lstrip("v") # normalized version
app_name = __name__.upper()
app_description = __description__

icon_path = "desktop/ui/images/svg/logo.svg"  

build_root = Path("./dist")
build_root.mkdir(exist_ok=True)

appimage_output_path = None

try:
    subprocess.run(["python3", "build.py", "bdist_appimage"], check=True)
    dist_appimage_files = glob(f"dist/{app_name}-{app_version}*.AppImage")
    if dist_appimage_files:
        appimage_output_path = dist_appimage_files[0]
    else:
        print("Failed to find the AppImage in 'dist' after build.")
        sys.exit(1)
except subprocess.CalledProcessError as e:
    print("Failed to build the AppImage:", e)
    sys.exit(1)

package_dir = build_root / app_name
deb_dir = package_dir / "DEBIAN"
applications_dir = package_dir / "usr/share/applications"
opt_dir = package_dir / f"opt/{app_name}"
icon_dir = package_dir / "usr/share/icons/hicolor/scalable/apps"

for dir_path in [deb_dir, applications_dir, opt_dir, icon_dir]:
    dir_path.mkdir(parents=True, exist_ok=True)

appimage_target_path = opt_dir / f"{app_name}.AppImage"
shutil.copy2(appimage_output_path, appimage_target_path)

appimage_target_path.chmod(0o755)

icon_target_path = icon_dir / f"{app_name}.svg"
shutil.copy2(icon_path, icon_target_path)

desktop_entry_content = f"""[Desktop Entry]
Name={app_name}
Exec=/opt/{app_name}/{app_name}.AppImage
Icon={app_name}
Type=Application
Categories=Utility;
"""
desktop_entry_path = applications_dir / f"{app_name}.desktop"
desktop_entry_path.write_text(desktop_entry_content)

def calculate_installed_size_kb(directory):
    total_size = sum(f.stat().st_size for f in directory.rglob('*') if f.is_file())
    return (total_size + 1023) // 1024  # Round

installed_size_kb = calculate_installed_size_kb(package_dir)

control_content = f"""Package: {app_name}
Version: {app_version}
Section: utils
Priority: optional
Architecture: {machine_arch}
Maintainer: {maintainer}
Installed-Size: {installed_size_kb}
Description: {app_description}
"""
control_file_path = deb_dir / "control"
control_file_path.write_text(control_content)

try:
    subprocess.run(["dpkg-deb", "--build", str(package_dir)], check=True)
    final_deb = f"{build_root}/{app_name}-{app_version}-{machine_arch}.deb"
    shutil.move(f"{build_root}/{app_name}.deb", final_deb)
    print(f"The .deb package has been created as {final_deb}")
    print(f"You can now install it with: sudo dpkg -i {final_deb}")
finally:
    shutil.rmtree(package_dir) # Clean up
