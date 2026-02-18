from ..utils.public import register_submodule_factory
from . import replace_ui

module_tuple = (
    replace_ui,
)

register_module, unregister_module = register_submodule_factory(module_tuple)


def register():
    register_module()


def unregister():
    unregister_module()
