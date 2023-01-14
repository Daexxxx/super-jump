import sys
from xml.etree.ElementInclude import include
from cx_Freeze import setup, Executable

includefiles = ['./levels/', './graphics/']
build_exe_options = {"packages": ["pygame"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="main.py",
    base="Win32GUI",
)

setup(
    name="Super Jumper",
    version="2.0",
    options={"build_exe": build_exe_options},
    executables=[target]
)
