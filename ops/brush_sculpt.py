import bpy
from mathutils import Vector

from .sculpt_operator import normal_brush_handle
from ..utils.log import log
from ..utils.public import PublicOperator, PublicDraw
import time


class OperatorProperty(PublicOperator, PublicDraw):
    alpha = 0.5
    start_mouse: Vector
    draw_in_depth_up: bool
    start_buffer_scale: float

    @property
    def is_builtin_brush(self):
        return self.active_tool_name.split(sep=".")[0] == "builtin_brush"

    @property
    def is_annotate_brush(self):
        return self.active_tool_name in self.annotate_brush

    def mouse_in_area_in(self, event, area):
        return True if self.is_annotate_brush else super().mouse_in_area_in(event, area)

    @property
    def is_hide_mode(self):
        return self.active_tool_name == "builtin.box_hide" and (self.ctrl_shift or self.ctrl_shift_alt)

    @property
    def is_make_mode(self):
        return (not self.mouse_is_in_model_up) and (self.only_ctrl or self.ctrl_alt) and self.is_builtin_brush

    @property
    def is_box_make_brush(self):
        return self.active_tool_name == "builtin.box_mask"

    @property
    def is_draw_2d_box(self):
        return not self.is_click and (self.is_hide_mode or self.is_make_mode or self.is_box_make_brush)

    @property
    def is_exit(self):
        return self.event_is_left or self.event_is_right or self.event_is_esc

    @property
    def use_front_faces_only(self):
        return self.active_tool.operator_properties("bbrush.mask").use_front_faces_only

    @property
    def color(self) -> Vector:
        if self.only_ctrl:
            return Vector((0, 0, 0, self.alpha))
        elif self.ctrl_alt:
            return Vector((0.5, 0.5, 0.5, self.alpha))
        elif self.ctrl_shift_alt:
            return Vector((0.6, 0, 0, self.alpha))
        elif self.ctrl_shift:
            return Vector((0, 0.6, 0, self.alpha))

        return Vector((1, 0, 0, 1))


class DepthUpdate(OperatorProperty):

    def depth_scale_update(self, context, event):
        co = self.mouse_co
        value = self.start_mouse - co
        x = 1 / context.region.width * (-1 * value[0])
        y = 1 / context.region.height * value[1]

        value = self.pref.depth_scale = self.start_buffer_scale + max(x, y) * 2
        context.area.header_text_set(f"Depth map zoom value {value}")

    def init_depth(self):
        from ..ui.draw_depth import DrawDepth

        _buffer = DrawDepth.depth_buffer
        self.draw_in_depth_up = ("wh" in _buffer) and self.mouse_in_area_in(self.event, _buffer["wh"])


class BBrushSculpt(DepthUpdate):
    bl_idname = "bbrush.bbrush_sculpt"
    bl_label = "Bbrush sculpting"
    bl_description = "Sculpting in the style of Zbrush"
    bl_options = {"REGISTER"}

    def __init__(self):
        self.in_modal: bool = None
        """光标在模型对象上, is_hit."""
        self.mouse_move_count = None

    def invoke(self, context, event):
        # self.start_time = time.time()

        log.debug(self.bl_idname)
        self.cache_clear()
        self.init_invoke(context, event)
        self.init_depth()

        self.start_mouse = self.mouse_co
        """开始的初始鼠标位置"""

        self.start_buffer_scale = self.pref.depth_scale
        """开始的左上角剪影视图Scale"""

        if self.is_3d_view:
            # self.in_modal = self.mouse_is_in_model_up
            """光标在模型上, 使用GPU深度检测."""
            # print(f"1 {time.time() - self.start_time}")
            # self.start_time = time.time()
            context.window_manager.modal_handler_add(self)
            return {"RUNNING_MODAL"}
        else:
            self.report({"WARNING"}, "Active space must be a View3d")
            return {"CANCELLED"}

    def modal(self, context: bpy.types.Context, event: bpy.types.Event):
        self.init_modal(context, event)
        self.tag_redraw(context)
        try:
            if self.is_exit:  # 退出模态操作
                context.area.header_text_set(None)
                log.info("ESC Bbrush Sculpt_____ FINISHED")
                return {"FINISHED"}

            elif self.draw_in_depth_up:  # 鼠标放在左上角深度图上操作
                log.debug("draw_in_depth_up")
                self.depth_scale_update(context, event)
                return {"RUNNING_MODAL"}
            else:
                return self.modal_handle(event)
        except Exception as e:
            log.error(e.args)
            return {"FINISHED"}

    def modal_handle(self, event: bpy.types.Event):
        r = bpy.ops.sculpt.brush_stroke("INVOKE_DEFAULT", True, mode="NORMAL")
        print(r)
        return {"FINISHED"}
        print(f"{self.name} -> is_click: {self.is_click}, is_hit: {self.in_modal}")
        if self.in_modal:
            if self.only_alt:
                self.smooth_brush_handle()
            elif event.value_prev == "PRESS":
                normal_brush_handle()
        else:
            if self.only_alt:
                bpy.ops.view3d.move("INVOKE_DEFAULT", True)
            elif not self.is_click:
                bpy.ops.view3d.rotate("INVOKE_DEFAULT", True)
                """
                # 关闭下面这个好像会流畅些, 但不知道会造成什么影响
                if event.value_prev != "RELEASE":
                    # print(f"2 {time.time() - self.start_time}")
                    bpy.ops.view3d.rotate("INVOKE_DEFAULT", True)
                """
        return {"FINISHED"}

    def smooth_brush_handle(self):
        if self.is_builtin_brush_smooth_brush:
            ...
        else:
            bpy.ops.sculpt.brush_stroke("INVOKE_DEFAULT", True, mode="INVERT")
