"""放置雕刻操作符
统一各版本操作符不同带来的bug
"""

import bpy

is_3_6_up_version = bpy.app.version >= (3, 6, 0)
is_4_1_up_version = bpy.app.version >= (4, 1, 0)
is_4_4_up_version = bpy.app.version >= (4, 4, 0)


# 反转可见面
def sculpt_invert_hide_face():
    if is_4_1_up_version:
        bpy.ops.paint.visibility_invert()
    elif is_3_6_up_version:
        bpy.ops.sculpt.face_set_invert_visibility()
    else:
        bpy.ops.sculpt.face_set_change_visibility("EXEC_DEFAULT", True, mode="INVERT")


def normal_brush_handle():
    bpy.ops.sculpt.brush_stroke("INVOKE_DEFAULT", True, mode="NORMAL")


def set_active_brush(brush: bpy.types.Brush):
    """`bpy.context.tool_settings.sculpt.brush = brush`"""
    print(is_4_4_up_version)
    if is_4_4_up_version:
        path = f"brushes\\essentials_brushes-mesh_sculpt.blend\\Brush\\{brush.name}"
        bpy.ops.brush.asset_activate(
            asset_library_type="ESSENTIALS",
            asset_library_identifier="",
            relative_asset_identifier=path,
        )
    else:
        bpy.context.tool_settings.sculpt.brush = brush
