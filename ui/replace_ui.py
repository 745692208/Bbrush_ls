from functools import cache

import bpy

from ..utils.public import all_operator_listen, PublicClass

UiReplaceFunc = None


@cache
def restart_blender():
    return "wm.restart_blender" in all_operator_listen()


def draw_restart_button(layout):
    if restart_blender():
        ops = layout.row()
        ops.alert = True
        ops.operator(operator="wm.restart_blender", text="", emboss=False, icon="QUIT")


def append_top_editor_menus2(self, context):
    """View3D -> 顶部 -> 菜单栏 -> 可见性选项."""
    pref = PublicClass.pref_()

    sculpt = pref.sculpt or pref.is_sculpt_mode
    if sculpt:
        layout = self.layout
        layout.separator()
        sub_row = layout.row(align=1)

        if not pref.sculpt:
            sub_row.prop(pref, "sculpt", text="", icon="SCULPTMODE_HLT")
        elif pref.always_use_sculpt_mode:
            sub_row.prop(pref, "always_use_sculpt_mode", emboss=True, icon="AUTO", text="")
        else:
            sub_row.prop(pref, "sculpt", text="", icon="SCULPTMODE_HLT")
            sub_row.prop(pref, "always_use_sculpt_mode", emboss=True, icon="AUTO", text="")


def register():
    bpy.types.VIEW3D_MT_editor_menus.append(append_top_editor_menus2)


def unregister():
    bpy.types.VIEW3D_MT_editor_menus.remove(append_top_editor_menus2)
