from functools import cache
import bpy
from bpy.app.translations import pgettext as _
from bpy.props import BoolProperty, EnumProperty, FloatProperty, IntProperty

from . import key
from .public import ADDON_NAME, PublicClass


class BBrushAddonPreferences(bpy.types.AddonPreferences, PublicClass):
    bl_idname = ADDON_NAME
    use_mouse_emulate_3_button: BoolProperty()

    layout: bpy.types.UILayout

    def sculpt_update(self, context):
        from ..ui.replace_ui import update_top_bar

        update_top_bar()
        inputs = context.preferences.inputs
        from .bbrush_toolbar import BrushTool

        if self.sculpt:
            BrushTool.toolbar_switch("SCULPT")
            self.use_mouse_emulate_3_button = inputs.use_mouse_emulate_3_button
            inputs.use_mouse_emulate_3_button = False
            key.register()
        else:
            BrushTool.toolbar_switch("ORIGINAL_TOOLBAR")
            inputs.use_mouse_emulate_3_button = self.use_mouse_emulate_3_button
            key.unregister()
        self.tag_all_redraw(context)

    sculpt: BoolProperty(name="Bbrush", default=False, options={"SKIP_SAVE"}, update=sculpt_update)

    show_text: BoolProperty(name=_("Display top text"), default=False)

    depth_display_items = (
        ("ALWAYS_DISPLAY", "DisplayedAllTheTime", "Keep the silhouette displayed all the time, even when not in sculpting mode"),
        ("ONLY_SCULPT", "SculptModeOnly", "Display silhouette images only in sculpting mode"),
        ("ONLY_BBRUSH", "BbrushModeOnly", "Display silhouette images only in Bbrush mode"),
        ("NOT_DISPLAY", "NotShown", "Never display silhouette images at any time"),
    )

    depth_display_mode: EnumProperty(name=_("Silhouette Display Mode"), default="ONLY_SCULPT", items=depth_display_items)
    depth_scale: FloatProperty(name=_("Silhouette image scaling"), default=0.3, max=2, min=0.1, step=0.1)
    depth_offset_x: IntProperty(name=_("Silhouette image offset X"), default=0, max=114514, min=0)
    depth_offset_y: IntProperty(name=_("Silhouette image offset Y"), default=80, max=114514, min=0)

    always_use_sculpt_mode: BoolProperty(name=_("Always use Bbrush sculpting mode"), description=_("If entering sculpting mode, Bbrush mode will automatically activate; if exiting sculpting mode, Bbrush mode will deactivate"), default=False)

    depth_ray_size: IntProperty(name=_("Depth ray check size(px)"), description=_("Check if the mouse is placed over the model, mouse cursor's range size"), default=5, min=5, max=300)

    show_shortcut_keys: BoolProperty(name=_("Display shortcut keys"), default=False)
    shortcut_offset_x: IntProperty(name=_("Shortcut key offset X"), default=20, max=114514, min=0)
    shortcut_offset_y: IntProperty(name=_("Shortcut key offset Y"), default=20, max=114514, min=0)
    shortcut_show_size: FloatProperty(name=_("Shortcut key display size"), min=0.1, default=1, max=114)

    def update_top(self, context):
        from ..ui.replace_ui import update_top_bar

        update_top_bar()

    replace_top_bar: BoolProperty(name="Replace top bar", default=True, update=update_top)
    alignment: EnumProperty(
        items=[
            ("LEFT", "LIFT", ""),
            ("CENTER", "CENTER", ""),
            ("RIGHT", "RIGHT", ""),
        ],
        default="CENTER",
    )

    def draw(self, context):
        draw_(self.layout, context)


@cache
def get_pref():
    return bpy.context.preferences.addons[ADDON_NAME].preferences


class VIEW3D_PT_editor_menus_bbrush_options(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_editor_menus_bbrush_options"
    bl_label = "BBrush Options"
    bl_space_type = "VIEW_3D"
    bl_region_type = "WINDOW"
    bl_ui_units_x = 20

    def draw(self, context):
        draw_(self.layout, context)


def draw_(layout: bpy.types.UILayout, context=bpy.context):
    """UI"""
    pref = get_pref()
    layout = layout

    box = layout.box()
    box.prop(pref, "always_use_sculpt_mode")
    row = box.row(align=True)
    row.prop(pref, "depth_display_mode")
    row.prop(pref, "depth_ray_size")
    layout.separator()

    layout.label(text="顶部栏")
    row = layout.box().row(align=True)
    row.prop(pref, "show_text")
    # row.prop(pref, "replace_top_bar")
    # row.prop(pref, "alignment")
    layout.separator()

    layout.label(text="Silhouette")
    box = layout.box()
    box.prop(pref, "depth_scale")
    row = box.row(align=True)
    row.prop(pref, "depth_offset_x")
    row.prop(pref, "depth_offset_y")
    layout.separator()

    layout.label(text="Shortcut")
    box = layout.box()
    box.prop(pref, "show_shortcut_keys")
    box.prop(pref, "shortcut_show_size")
    row = box.row(align=True)
    row.prop(pref, "shortcut_offset_x")
    row.prop(pref, "shortcut_offset_y")


def register():
    bpy.utils.register_class(BBrushAddonPreferences)
    bpy.utils.register_class(VIEW3D_PT_editor_menus_bbrush_options)


def unregister():
    bpy.utils.unregister_class(BBrushAddonPreferences)
    bpy.utils.unregister_class(VIEW3D_PT_editor_menus_bbrush_options)
    key.unregister()
