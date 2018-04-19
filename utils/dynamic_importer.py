from importlib import import_module
import os, sys
import pkgutil


class DynamicImporter:
    """
    References:
        01. importlib:
            https://stackoverflow.com/questions/44492803/python-dynamic-import-how-to-import-from-module-name-from-variable
        02. pkgutil:
            https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder
            https://www.bnmetrics.com/blog/dynamic-import-in-python3
    """
    @staticmethod
    def module(module_path):
        module = import_module(module_path)

        globals().update(
            {n: getattr(module, n) for n in module.__all__} if hasattr(module, '__all__')
            else
            {k: v for (k, v) in module.__dict__.items() if not k.startswith('_')})

    @staticmethod
    def package(package_file_path):
        root = os.path.dirname(sys.modules['__main__'].__file__) + "/"
        try:
            prefix = package_file_path.replace(".", "").replace("/", ".")
            for module_info in pkgutil.iter_modules([root + package_file_path]):
                DynamicImporter.module(prefix + "." + module_info.name)
        except Exception as ex:
            raise ex

