import os
from pathlib import Path


def get_resource(name: str) -> Path:
    module_path = Path(os.path.dirname(__file__))
    resource_path = Path(module_path.parent.parent, 'resources')
    return Path(resource_path, name)
