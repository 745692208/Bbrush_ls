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

    alignment: EnumProperty(
        items=[
            ("LEFT", "LIFT", ""),
            ("CENTER", "CENTER", ""),
            ("RIGHT", "RIGHT", ""),
        ],
        default="CENTER",
    )


@cache
def get_pref():
    return bpy.context.preferences.addons[ADDON_NAME].preferences


def register():
    bpy.utils.register_class(BBrushAddonPreferences)


def unregister():
    bpy.utils.unregister_class(BBrushAddonPreferences)
    key.unregister()
