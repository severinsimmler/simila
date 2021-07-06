from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError, DistutilsExecError, DistutilsPlatformError

from setuptools import Extension


class Builder(build_ext):
    def run(self):
        try:
            build_ext.run(self)
        except (DistutilsPlatformError, FileNotFoundError):
            raise OSError("File not found. Could not compile C extension.")

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (CCompilerError, DistutilsExecError, DistutilsPlatformError, ValueError):
            raise OSError("Could not compile C extension.")


ext_modules = [
    Extension(
        "simila.Levenshtein", include_dirs=["simila"], sources=["simila/Levenshtein.c"]
    )
]


def build(setup_kwargs: dict):
    setup_kwargs.update(
        {"ext_modules": ext_modules, "cmdclass": {"build_ext": Builder}}
    )
