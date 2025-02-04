import bpy
from bl_ui.properties_paint_common import UnifiedPaintPanel
from bl_ui.space_toolsystem_common import ToolSelectPanelHelper

from ..utils.bbrush_toolbar import BrushTool
from ..utils.log import log
from ..utils.public import PublicOperator


class SwitchProperty(PublicOperator):
    is_esc = False
    _tmp_brush: bpy.types.Brush = None
    """临时储存的笔刷对象"""
    _tmp_tool_name: str = ""
    """临时储存的笔刷工具名称"""

    @property
    def is_smoot_mode(self):
        """`return self.only_shift or self.shift_alt`"""
        return self.only_shift or self.shift_alt

    @property
    def is_mask_mode(self):
        """return self.only_ctrl or self.ctrl_alt"""
        return self.only_ctrl or self.ctrl_alt

    @property
    def is_hide_mode(self):
        """self.ctrl_shift or self.ctrl_shift_alt"""
        return self.ctrl_shift or self.ctrl_shift_alt

    @property
    def is_exit(self):
        """用户输入'ESC', 'SPACE'"""
        return (self.event.type in ("ESC", "SPACE")) or self.not_key or self.is_esc

    @property
    def is_pass(self):
        """可能是输入了空格？"""
        space = self.event_is_space
        return (self.only_ctrl and self.event_is_tab) or (space and self.ctrl_alt) or (space and self.only_alt) or (space and self.only_ctrl)

    @property
    def brushes(self):
        return ToolSelectPanelHelper._tool_class_from_space_type("VIEW_3D")._tools["SCULPT"]

    @brushes.setter
    def _set_brushes(self, value):
        ToolSelectPanelHelper._tool_class_from_space_type("VIEW_3D")._tools["SCULPT"] = value

    @staticmethod
    def B_brushes(key):
        return BrushTool.toolbar_dit[key]

    @property
    def _hide_brushes(self):
        return self.B_brushes("HIDE")

    @property
    def _mask_brushes(self):
        return self.B_brushes("MASK")

    @property
    def _sculpt_brushes(self):
        return self.B_brushes("SCULPT")

    @property
    def active_hide_brush(self):
        return BrushTool.active_brush["HIDE"]

    @staticmethod
    def set_hide_brush(value):
        BrushTool.active_brush["HIDE"] = value

    @property
    def active_mask_brush(self):
        """`BrushTool.active_brush["MASK"]`"""
        return BrushTool.active_brush["MASK"]

    @staticmethod
    def set_mask_brush(value):
        BrushTool.active_brush["MASK"] = value

    @property
    def active_sculpt_brush(self):
        return BrushTool.active_brush["SCULPT"]

    @staticmethod
    def set_sculpt_brush(value):
        """BrushTool.active_brush['SCULPT'] = value"""
        BrushTool.active_brush["SCULPT"] = value

    @property
    def active_not_in_active_brushes(self):  # 活动笔刷没在几个活动项里面
        return self.active_tool_name and self.active_tool_name != self.active_sculpt_brush and (self.active_tool_name not in BrushTool.active_brush.values())

    @property
    def is_change_brush(self):
        return self.active_not_in_active_brushes


class BBrushSwitch(SwitchProperty):
    bl_idname = "bbrush.bbrush_switch"
    bl_label = "Brush mode switch"
    bl_description = "Switch brush content, with a list of options for each key, including [sculpt, mask, hide]"

    bl_options = {"REGISTER"}

    def invoke(self, context, event):
        print("BBrushSwitch")
        self.init_invoke(context, event)
        log.debug(self.bl_idname)

        if self.is_3d_view:
            if self.is_change_brush:
                self.set_sculpt_brush(self.active_tool_name)
            self._tmp_brush = self.active_brush
            self._tmp_tool_name = self.active_tool_name
            context.window_manager.modal_handler_add(self)
            return {"RUNNING_MODAL"}
        else:
            self.report({"WARNING"}, "Active space must be a View3d")
            return {"CANCELLED"}

    def modal(self, context, event):
        self.init_modal(context, event)
        self.update_shortcut_keys()

        if self.is_exit:
            self.set_shortcut_keys("NORMAL")
            return self.exit(context, event)
        elif self.is_pass:  # ctrl tab切换模式
            self.is_esc = True
            return {"PASS_THROUGH"}
        elif self.is_hide_mode:  # self.ctrl_shift or self.ctrl_shift_alt
            self.hide_mode()
        elif self.is_mask_mode:  # self.only_ctrl or self.ctrl_alt
            self.mask_mode()
        else:
            self.set_shortcut_keys("NORMAL")
        self.tag_redraw(context)  # 进行重绘，避免更改工具栏后内容还是旧的
        return self.event_ops(event)

    def event_ops(self, event):
        press = self.event_is_press
        # print(f"    {press}, {self.only_shift}")

        if self.only_shift and self.active_brush.name != "Smooth":  # 切换到Smooth Brush
            self.set_active_brush(bpy.data.brushes.get("Smooth"))
        """
        if self.only_shift:  # 切换到Smooth Brush
            # if self.active_brush.name != "Smooth":
            if not self._tmp_tool_name and not self._tmp_brush:
                self._tmp_brush = self.active_brush
                self._tmp_tool_name = self.active_tool_name
            self.analysis_switch_brush("builtin_brush.Smooth")
        elif self._tmp_tool_name and self._tmp_brush:
            bpy.ops.wm.tool_set_by_id(name=self._tmp_tool_name)
            self.set_active_brush(self._tmp_brush)
            self._tmp_tool_name = ""
            self._tmp_brush = None
        """

        """
        tmp = getattr(self, "_tmp_tool_name", False)
        tmp_brush = getattr(self, "_tmp_brush", None)
        print(tmp, tmp_brush)

        # if self.only_shift and event.type == "LEFTMOUSE" and event.value == "PRESS":
        # if self.only_shift and event.value == "PRESS":
        if self.only_shift:
            setattr(self, "_tmp_tool_name", self.active_tool_name)
            setattr(self, "_tmp_brush", self.active_brush)

            print(f"当前活动工具名：{self.active_tool_name}, {self.active_brush} !!!!!!!!!!!!!!!!!!!!")
            self.analysis_switch_brush("builtin_brush.Smooth")
            if 0:
                if bpy.app.version >= (4, 3, 0):
                    if self.active_brush.name != "Smooth":
                        self.analysis_switch_brush("builtin_brush.Smooth")
                else:  # 旧版
                    if self.active_tool_name != "builtin_brush.Smooth":
                        self.analysis_switch_brush("builtin_brush.Smooth")
            self.tag_redraw(bpy.context)

        elif tmp:
            # 有temp对象就改回去然后删除temp对象。
            bpy.ops.wm.tool_set_by_id(name=self._tmp_tool_name)
            delattr(self, "_tmp_tool_name")
            # self.tag_redraw(bpy.context)

            if tmp_brush:
                self.set_active_brush = self._tmp_brush
                delattr(self, "_tmp_brush")
                # self.tag_redraw(bpy.context)

            self.tag_redraw(bpy.context)

        """
        if press:
            if event.type == "NUMPAD_PLUS":
                bpy.ops.sculpt.mask_filter("EXEC_DEFAULT", True, filter_type="GROW", auto_iteration_count=True)
            elif event.type == "NUMPAD_MINUS":
                bpy.ops.sculpt.mask_filter("EXEC_DEFAULT", True, filter_type="SHRINK", auto_iteration_count=True)
            elif event.type in ("UP_ARROW", "NUMPAD_ASTERIX"):
                bpy.ops.sculpt.mask_filter("EXEC_DEFAULT", True, filter_type="CONTRAST_INCREASE", auto_iteration_count=False)
            elif event.type in ("DOWN_ARROW", "NUMPAD_SLASH"):
                bpy.ops.sculpt.mask_filter("EXEC_DEFAULT", True, filter_type="CONTRAST_DECREASE", auto_iteration_count=False)

        # print(f'event_ops -> {self.only_shift and event.type == "LEFTMOUSE" and event.value == "PRESS"}, {tmp}, {press}')
        if self.is_smoot_mode:  # self.only_shift or self.shift_alt
            return self.smoot_mode()
        elif self.event_is_w and self.only_ctrl and press:
            bpy.ops.sculpt.face_sets_create("EXEC_DEFAULT", True, mode="MASKED")
            bpy.ops.paint.mask_flood_fill("EXEC_DEFAULT", True, mode="VALUE", value=0)
            return {"RUNNING_MODAL"}
        return {"PASS_THROUGH"}

    def exit(self, context, event):
        BrushTool.toolbar_switch("SCULPT")
        if self.is_sculpt_mode:
            if 0:
                bpy.ops.wm.tool_set_by_id(name=BrushTool.active_brush["SCULPT"])
            else:  # My 我有一个笔刷的快捷键需要按住alt，切换成功后松开按键会跳回原本的笔刷, https://gitee.com/AIGODLIKE/Bbrush/issues/I8QFWM
                if self._tmp_tool_name and self._tmp_brush:
                    bpy.ops.wm.tool_set_by_id(name=self._tmp_tool_name)
                    self.set_active_brush(self._tmp_brush)
                    self._tmp_tool_name = ""
                    self._tmp_brush = None
                else:
                    bpy.ops.wm.tool_set_by_id(name=BrushTool.active_brush["SCULPT"])

                """
                current_brush_name = bpy.context.tool_settings.sculpt.brush.name.lower()
                name = BrushTool.active_brush["SCULPT"]
                # 防止类似box_mask这类不知道怎么获取的笔刷
                if current_brush_name == name.split(".", 1)[1].lower():
                    bpy.ops.wm.tool_set_by_id(name=name)
                else:
                    keys = ["mask", "hide", "project", "trim", "smooth"]
                    for i in keys:
                        if i in current_brush_name:
                            bpy.ops.wm.tool_set_by_id(name=name)
                            break
                """

        if not self.active_tool:
            BrushTool.init_active_brush()

        # 闪退，原因未知
        self.tag_redraw(context)
        self.handler_remove()
        log.debug(BrushTool.active_brush)
        log.debug("exit BBrushSwitch \n")
        return {"FINISHED"}

    def hide_mode(self):
        if self.brushes != self._hide_brushes:
            BrushTool.toolbar_switch("HIDE")
            bpy.ops.wm.tool_set_by_id(name=BrushTool.active_brush["HIDE"])
        elif self.is_change_brush:
            self.set_hide_brush(self.active_tool_name)

    def mask_mode(self):
        if self.brushes != self._mask_brushes:
            BrushTool.toolbar_switch("MASK")
            bpy.ops.wm.tool_set_by_id(name=self.active_mask_brush)
        elif self.is_change_brush:
            self.set_mask_brush(self.active_tool_name)

    def smoot_mode(self):
        shift_ops = self.only_shift and not self.event_is_left

        if self.event_is_left and not self.mouse_is_in_model_up:
            bpy.ops.view3d.view_roll("INVOKE_DEFAULT", type="ANGLE")
            return {"PASS_THROUGH"}
        elif self.event_is_f or self.event_is_r or shift_ops:
            return {"PASS_THROUGH"}
        elif self.event_left_mouse_press:
            return self.switch_shift()
        elif self.event_key_middlemouse:
            bpy.ops.view3d.move("INVOKE_DEFAULT")
        return {"RUNNING_MODAL"}

    def switch_shift(self):
        """针对按住`shift`或`shift&alt`和雕刻的操作行为. 使用Blender雕刻命令就行了."""
        print("switch_shift")
        bpy.context.area.tag_redraw()
        return {"PASS_THROUGH"}
        settings = UnifiedPaintPanel.paint_settings(bpy.context)
        log.debug(f"event_left_mouse_press,{self.shift_alt}")
        try:
            brush = settings.brush
            if self.shift_alt:
                direction = "ENHANCE_DETAILS" if brush.direction == "SMOOTH" else "SMOOTH"
                setattr(self, "or_dir", brush.direction)
                brush.direction = direction
            bpy.ops.sculpt.brush_stroke("INVOKE_DEFAULT", mode="NORMAL")
            if getattr(self, "or_dir", False):
                brush.direction = self.or_dir
                delattr(self, "or_dir")
        except Exception as e:
            log.debug(e)
        return {"PASS_THROUGH"}

    def update_shortcut_keys(self):
        """切换左下角的快捷键提示文本"""
        if self.is_exit or self.is_pass:
            self.set_shortcut_keys("NORMAL")
        if self.is_hide_mode:
            self.set_shortcut_keys("HIDE")
        elif self.is_mask_mode:
            self.set_shortcut_keys("MASK")
        else:
            self.set_shortcut_keys("NORMAL")
