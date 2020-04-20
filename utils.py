"""
This module should not depend on anything other than standard modules.
このモジュールは、標準モジュール以外に依存してはいけません。
"""

import importlib
import inspect
import pkgutil
from collections import deque
from typing import List, Type, Optional, Callable


def get_all_classes_from_package(pkg_path: str, filter_func: Optional[Callable[[Type], bool]] = None) -> List[Type]:
    ret = deque()
    module = importlib.import_module(pkg_path)
    for info in pkgutil.iter_modules(module.__path__, f"{module.__name__}."):
        if info.ispkg:
            ret += get_all_classes_from_package(info.name, filter_func)
            continue

        child_module = importlib.import_module(info.name)
        for clazz in map(lambda x: x[1], inspect.getmembers(child_module, inspect.isclass)):
            if filter_func and not filter_func(clazz):
                continue
            ret.append(clazz)
    return list(ret)
