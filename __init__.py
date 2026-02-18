import bpy
from . import zh_CN

# =================
from importlib import reload
from .ops import brush_switch
from .ops import brush_sculpt
from .ops import brush_mask
from .utils import key
from .utils import reg
from .utils import public

module_list = [
    brush_switch,
    brush_sculpt,
    brush_mask,
    key,
    reg,
    public,
]
[reload(i) for i in module_list]


bl_info = {
    "name": "Bbrush_ls-2025年2月4日",
    "author": "AIGODLIKE Community: 小萌新, levosaber",
    "version": (1, 2, 7),
    "blender": (4, 3, 0),
    "location": "Entering the sculpt mode will be displayed in the top bar",
    "description": "在原版1.2.7的基础上修魔改成可支持4.3, 不支持向下兼容。",
    "category": "AIGODLIKE",
}


class TranslationHelper:
    def __init__(self, name: str, data: dict, lang="zh_CN"):
        self.name = name
        self.translations_dict = dict()

        for src, src_trans in data.items():
            key = ("Operator", src)
            self.translations_dict.setdefault(lang, {})[key] = src_trans
            key = ("*", src)
            self.translations_dict.setdefault(lang, {})[key] = src_trans

    def register(self):
        try:
            bpy.app.translations.register(self.name, self.translations_dict)
        except ValueError:
            pass

    def unregister(self):
        bpy.app.translations.unregister(self.name)


Bbrush_zh_CN = TranslationHelper("Bbrush_zh_CN", zh_CN.data)
Bbrush_zh_HANS = TranslationHelper("Bbrush_zh_HANS", zh_CN.data, lang="zh_HANS")


def debug_test():
    return
    bpy.ops.wm.console_toggle()
    kc = bpy.context.window_manager.keyconfigs.user
    for _ in range(20):
        for km in kc.keymaps:
            km.restore_to_default()


def register():
    bpy.app.timers.register(debug_test, first_interval=1)
    reg.register()

    if bpy.app.version < (4, 0, 0):
        Bbrush_zh_CN.register()
    else:
        Bbrush_zh_CN.register()
        Bbrush_zh_HANS.register()


def unregister():
    reg.unregister()

    if bpy.app.version < (4, 0, 0):
        Bbrush_zh_CN.unregister()
    else:
        Bbrush_zh_CN.unregister()
        Bbrush_zh_HANS.unregister()
