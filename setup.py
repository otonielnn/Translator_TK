from sys import platform
from cx_Freeze import setup, Executable

base = None
if platform == 'win32':
    base = 'Win32Gui'

setup(
    name='Translator',
    version='1.0',
    description='A simple translator made with TkInter',
    options={
        'build_exe': {
            'includes': ['tkinter', 'ttkbootstrap'],
            'packages': ['tkinter', 'ttkbootstrap'],
        }
    },
    executables=[
        Executable('translator.py', base=base)
    ]
)