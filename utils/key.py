# ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
# Base
brush_stroke = "sculpt.brush_stroke"
mask_lasso_gesture = "paint.mask_lasso_gesture"
hide_show = "paint.hide_show"
select_lasso = "view3d.select_lasso"
f_active = {"active": False}
empty_window = {"space_type": "EMPTY", "region_type": "WINDOW"}
view_3d_window = {"space_type": "VIEW_3D", "region_type": "WINDOW"}
empty_window_modal = {**empty_window, "modal": True}
l_any = {"type": "LEFTMOUSE", "value": "ANY", "any": True}
bbrush_mask = "bbrush.mask"
bbrush_sculpt = "bbrush.bbrush_sculpt"
bbrush_switch = "bbrush.bbrush_switch"
view = "3D View Tool"

# ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
# Keymaps
sculpt_modify_keymaps = {
    "Sculpt": {
        # ("wm.call_panel", (("name", "VIEW3D_PT_sculpt_context_menu"),)): {"value": "RELEASE"},
        (brush_stroke, ()): f_active,
        (brush_stroke, (("mode", 0),)): f_active,
        (brush_stroke, (("mode", 1),)): f_active,
        (brush_stroke, (("mode", 2),)): f_active,
        (mask_lasso_gesture, ()): f_active,
        (mask_lasso_gesture, (("value", 1.0),)): {"ctrl": True},
        (mask_lasso_gesture, (("value", 0.0),)): {"alt": True},
    },
    f"{view}: Sculpt, Box Mask": {
        ("paint.mask_box_gesture", (("value", 1.0),)): {"ctrl": True, "active": False},
        ("paint.mask_box_gesture", (("value", 0.0),)): {"alt": True, "active": False},
    },
    f"{view}: Sculpt, Lasso Mask": {
        (mask_lasso_gesture, (("value", 1.0),)): {"ctrl": True},
        (mask_lasso_gesture, (("value", 0.0),)): {"alt": True},
    },
    f"{view}: Sculpt, Line Mask": {
        ("paint.mask_line_gesture", (("value", 1.0),)): {"ctrl": True},
        ("paint.mask_line_gesture", (("value", 0.0),)): {"alt": True},
    },
    f"{view}: Sculpt, Box Hide": {
        (hide_show, (("action", 1),)): f_active,
        (hide_show, (("action", 0),)): f_active,
        (hide_show, (("action", 1), ("area", 2))): f_active,
    },
    f"{view}: Sculpt, Lasso Trim": {
        ("sculpt.trim_lasso_gesture", ()): {"ctrl": True, "shift": True},
    },
    f"{view}: Sculpt, Box Trim": {
        ("sculpt.trim_box_gesture", ()): {"ctrl": True, "shift": True},
    },
    f"{view}: Sculpt, Line Project": {
        ("sculpt.project_line_gesture", ()): {"ctrl": True, "shift": True},
    },
    "Screen": {
        ("sculpt.project_line_gesture", ()): {"ctrl": True, "shift": True},
    },
    "3D View": {
        (select_lasso, (("mode", 1),)): f_active,
        (select_lasso, (("mode", 2),)): f_active,
        (select_lasso, ()): f_active,
        ("view3d.cursor3d", ()): f_active,
        ("transform.translate", ()): f_active,
        ("emm.hdr_rotation", ()): f_active,
        ("view3d.select", ()): f_active,
    },
}
sculpt_keys_items = (
    (
        "View3D Rotate Modal",
        empty_window_modal,
        {
            "items": [
                ("CONFIRM", {"type": "RIGHTMOUSE", "value": "ANY"}, None),
                ("CONFIRM", {"type": "LEFTMOUSE", "value": "ANY"}, None),
                # ("SWITCH_TO_ZOOM", {"type": "LEFT_CTRL", "value": "ANY"}, None),
                ("AXIS_SNAP_ENABLE", {"type": "LEFT_SHIFT", "value": "PRESS"}, None),
                ("AXIS_SNAP_DISABLE", {"type": "LEFT_SHIFT", "value": "RELEASE"}, None),
            ]
        },
    ),
    (
        "View3D Move Modal",
        empty_window_modal,
        {
            "items": [
                ("CONFIRM", {"type": "RIGHTMOUSE", "value": "ANY"}, None),
                ("CONFIRM", {"type": "LEFTMOUSE", "value": "ANY"}, None),
                ("SWITCH_TO_ZOOM", {"type": "LEFT_ALT", "value": "ANY"}, None),
                ("SWITCH_TO_ZOOM", {"type": "LEFT_CTRL", "value": "ANY"}, None),
            ]
        },
    ),
    (
        "View3D Zoom Modal",
        empty_window_modal,
        {
            "items": [
                ("CONFIRM", {"type": "RIGHTMOUSE", "value": "ANY"}, None),
                ("CONFIRM", {"type": "LEFTMOUSE", "value": "ANY"}, None),
                ("SWITCH_TO_ROTATE", {"type": "LEFT_CTRL", "value": "RELEASE"}, None),
                ("SWITCH_TO_MOVE", {"type": "LEFT_CTRL", "value": "PRESS"}, None),
                ("SWITCH_TO_MOVE", {"type": "LEFT_ALT", "value": "ANY"}, None),
            ]
        },
    ),
    (
        "Sculpt",
        empty_window,
        {
            "items": [
                # ("雕刻", "LEFTMOUSE", "sculpt.brush_stroke", (("mode", "NORMAL"), ("ignore_background_click", True))),
                ("sculpt.brush_stroke", {"type": "LEFTMOUSE", "value": "PRESS"}, {"properties": [("mode", "NORMAL"), ("ignore_background_click", True)]}),
                # ("反转雕刻", "alt+LEFTMOUSE", "sculpt.brush_stroke", (("mode", "INVERT"), ("ignore_background_click", True))),
                ("sculpt.brush_stroke", {"type": "LEFTMOUSE", "value": "PRESS", "alt": True}, {"properties": [("mode", "INVERT"), ("ignore_background_click", True)]}),
                # ("雕刻 平滑", "shift+LEFTMOUSE", "sculpt.brush_stroke", (("mode", "SMOOTH"), ("ignore_background_click", True))),
                ("sculpt.brush_stroke", {"type": "LEFTMOUSE", "value": "PRESS", "shift": True}, {"properties": [("mode", "NORMAL"), ("ignore_background_click", True)]}),
                ("sculpt.brush_stroke", {"type": "LEFTMOUSE", "value": "PRESS", "shift": True, "alt": True}, {"properties": [("mode", "INVERT"), ("ignore_background_click", True)]}),
                # ("sculpt.brush_stroke", {"type": "LEFTMOUSE", "value": "PRESS", "shift": True}, {"properties": [("mode", "SMOOTH"), ("ignore_background_click", True)]}),
                # ("视图 操控 旋转", "LEFTMOUSE", "view3d.rotate", None),
                ("view3d.rotate", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                ("view3d.rotate", {"type": "RIGHTMOUSE", "value": "PRESS"}, None),
                # ("视图 操控 平移", "alt+LEFTMOUSE", "view3d.move", None),
                ("view3d.move", {"type": "LEFTMOUSE", "value": "PRESS", "alt": True}, None),
                ("view3d.move", {"type": "RIGHTMOUSE", "value": "PRESS", "alt": True}, None),
                # 传递雕刻对象
                # ("object.transfer_mode", {"type": "LEFTMOUSE", "value": "CLICK", "alt": True}, None),  # 冲突用不了, 用alt+q好了
                # Mask 和 Switch
                (bbrush_mask, {"type": "LEFTMOUSE", "value": "CLICK", "any": True, "ctrl": True}, {"properties": [("is_click", True)]}),
                (bbrush_mask, {"type": "LEFTMOUSE", "value": "CLICK_DRAG", "any": True, "ctrl": True}, {"properties": [("is_click", False)]}),
                (bbrush_switch, {"type": "LEFT_SHIFT", "value": "ANY"}, None),
                (bbrush_switch, {"type": "LEFT_CTRL", "value": "ANY"}, None),
                # # (bbrush_switch, {"type": "LEFT_ALT", "value": "ANY"}, None),  # 避免`alt+数字键`切换笔刷快捷键冲突. 也没发现有其它作用, 直接屏蔽.
                # ============ 原本 ============
                # (bbrush_sculpt, {"type": "LEFTMOUSE", "value": "CLICK", "any": False}, {"properties": [("is_click", True)]}),
                # (bbrush_sculpt, {"type": "LEFTMOUSE", "value": "CLICK_DRAG", "any": False}, {"properties": [("is_click", False)]}),
                # (bbrush_sculpt, {"type": "LEFTMOUSE", "value": "CLICK", "alt": False}, {"properties": [("is_click", True)]}),
                # (bbrush_sculpt, {"type": "LEFTMOUSE", "value": "CLICK_DRAG", "alt": False}, {"properties": [("is_click", False)]}),
                # (bbrush_sculpt, {"type": "LEFTMOUSE", "value": "CLICK_DRAG", "any": False, "alt": True}, {"properties": [("is_click", False)]}),
                # (bbrush_mask, {"type": "LEFTMOUSE", "value": "CLICK", "any": True, "ctrl": True}, {"properties": [("is_click", True)]}),
                # (bbrush_mask, {"type": "LEFTMOUSE", "value": "CLICK_DRAG", "any": True, "ctrl": True}, {"properties": [("is_click", False)]}),
                # (bbrush_switch, {"type": "LEFT_CTRL", "value": "ANY"}, None),
                # # (bbrush_switch, {"type": "LEFT_ALT", "value": "ANY"}, None),  # 避免`alt+数字键`切换笔刷快捷键冲突. 也没发现有其它作用, 直接屏蔽.
                # (bbrush_switch, {"type": "LEFT_SHIFT", "value": "ANY"}, None),
                # ("object.transfer_mode", {"type": "LEFTMOUSE", "value": "CLICK", "alt": True}, None),
                # ("view3d.rotate", {"type": "RIGHTMOUSE", "value": "CLICK_DRAG"}, None),
                # ("view3d.move", {"type": "RIGHTMOUSE", "value": "PRESS", "alt": True}, None),
                # ("view3d.move", {"type": "MIDDLEMOUSE", "value": "PRESS", "alt": True}, None),
                # ("view3d.zoom", {"type": "RIGHTMOUSE", "value": "PRESS", "ctrl": True}, None),
                # ("view3d.zoom", {"type": "RIGHTMOUSE", "value": "PRESS", "alt": True}, None),
            ]
        },
    ),
)


def keymap_register(keymap_data):
    import bpy

    wm = bpy.context.window_manager
    config = wm.keyconfigs.user

    from bl_keymap_utils.io import keymap_init_from_data

    if config:  # happens in background mode...
        for km_name, km_args, km_content in keymap_data:
            km_space_type = km_args["space_type"]
            km_region_type = km_args["region_type"]
            km_modal = km_args.get("modal", False)
            kmap = next(iter(k for k in config.keymaps if k.name == km_name and k.region_type == km_region_type and k.space_type == km_space_type and k.is_modal == km_modal), None)
            if kmap is None:
                kmap = config.keymaps.new(km_name, **km_args)
            keymap_init_from_data(kmap, km_content["items"], is_modal=km_modal)


def __get_key_data(item):
    ke_type = item.get("type")
    ke_value = item.get("value")
    ke_any = item.get("any", False)
    ke_alt = item.get("alt", False)
    ke_ctrl = item.get("ctrl", False)
    ke_shift = item.get("shift", False)
    ke_os = item.get("oskey", False)
    ke_repeat = item.get("repeat", False)
    ke_key_modifier = item.get("key_modifier", "NONE")

    key_ = (ke_any, ke_alt, ke_ctrl, ke_shift, ke_os) if not ke_any else (True, True, True, True, True)
    return (
        ke_type,
        ke_value,
        *key_,
        ke_repeat,
        ke_key_modifier,
    )


def __get_keydata_item(items):
    items_data = {}
    for idname, keyset, prop in items:
        prop = tuple(sorted(prop["properties"])) if prop else ()
        data_key = (idname, __get_key_data(keyset), prop)
        items_data[data_key] = None
    return items_data


def __key_to_hash_table(keymap_data):
    hash_table = {"km_name": []}
    for km_name, km_args, km_content in keymap_data:
        km_space_type = km_args["space_type"]
        km_region_type = km_args["region_type"]
        km_modal = km_args.get("modal", False)
        hash_key = (km_name, km_space_type, km_region_type, km_modal)
        hash_table[hash_key] = __get_keydata_item(km_content["items"])
        hash_table["km_name"].append(km_name)
    return hash_table


def __un_key(keymap, hash_table):
    for kmi in keymap.keymap_items:
        key_ = (kmi.any, kmi.alt, kmi.ctrl, kmi.shift, kmi.oskey) if not kmi.any else (True, True, True, True, True)
        km_modal = keymap.is_modal
        idname = kmi.propvalue if km_modal else kmi.idname
        it_key = (kmi.type, kmi.value, *key_, kmi.repeat, kmi.key_modifier)
        prop = tuple(sorted(kmi.properties.items())) if kmi.properties else ()
        hash_ky = (idname, it_key, prop)
        if hash_ky in hash_table:
            keymap.keymap_items.remove(kmi)


def keymap_unregister(keymap_data):
    import bpy

    wm = bpy.context.window_manager
    configs = wm.keyconfigs
    keymap_hash_table = __key_to_hash_table(keymap_data)

    for config in (configs.user, configs.addon):
        for keymap in config.keymaps:
            name = keymap.name
            space = keymap.space_type
            region = keymap.region_type
            modal = keymap.is_modal
            kc_key = (name, space, region, modal)
            if kc_key in keymap_hash_table:
                __un_key(keymap, keymap_hash_table[kc_key])
    del keymap_hash_table


def __set_keymap(modify, kmi):
    for key in (
        "shift",
        "alt",
        "ctrl",
        "value",
        "active",
        "repeat",
        "oskey",
        "type",
    ):
        if key in modify:
            setattr(kmi, key, modify.get(key))


def __modify_set_key(keymaps, keymap_hash_table, modify_bool):
    for kmi in keymaps.keymap_items:
        prop = tuple(sorted(kmi.properties.items())) if kmi.properties else ()
        hash_key = (kmi.idname, prop)
        if hash_key in keymap_hash_table:
            modify = keymap_hash_table[hash_key]
            if modify_bool:
                __set_keymap(modify, kmi)
            else:  # kmi.is_user_modified
                item = keymaps.keymap_items.from_id(kmi.id)
                keymaps.restore_item_to_default(item)
                if ("active" in modify) and (not modify.get("active")):
                    kmi.active = True


def modify_keymap(keymap_hash_table, modify_bool):
    import bpy

    wm = bpy.context.window_manager
    configs = wm.keyconfigs
    if configs:  # happens in background mode...
        for config in (configs.user, configs.addon):
            for keymap in config.keymaps:
                if keymap.name in keymap_hash_table:
                    __modify_set_key(keymap, keymap_hash_table[keymap.name], modify_bool)


def close_conflict_keys1(kmis_state=None, un=False):
    """My 遍历所有kmi, 关闭视图操作, 避免与Maya系视图操控冲突, 如那套`行业标准`快捷键"""
    import bpy

    a = [
        "view3d.rotate",
        "view3d.move",
        "view3d.zoom",
    ]
    if kmis_state:
        for kmi, active in kmis_state:
            kmi.active = active
    else:
        kmis_state = []
        wm = bpy.context.window_manager
        kc = wm.keyconfigs.user
        km = kc.keymaps.get("3D View")
        for kmi in km.keymap_items:
            if kmi.idname in a:
                kmis_state.append((kmi, kmi.active))
                kmi.active = False
        return kmis_state


def close_conflict_keys(is_unregister=False):
    """My 遍历所有kmi, 关闭视图操作, 避免与Maya系视图操控冲突, 如那套`行业标准`快捷键"""
    import bpy

    a = [
        "view3d.rotate",
        "view3d.move",
        "view3d.zoom",
    ]
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.user
    km = kc.keymaps.get("3D View")
    for kmi in km.keymap_items:
        if kmi.idname in a and kmi.type not in ["WHEELUPMOUSE", "WHEELDOWNMOUSE", "WHEELINMOUSE", "WHEELOUTMOUSE"]:
            kmi.active = True if is_unregister else False


def set_brushes_setting():
    import bpy

    def set_brush(name: str):
        path = f"brushes\\essentials_brushes-mesh_sculpt.blend\\Brush\\{name}"
        bpy.ops.brush.asset_activate(
            asset_library_type="ESSENTIALS",
            asset_library_identifier="",
            relative_asset_identifier=path,
        )
        return bpy.context.tool_settings.sculpt.brush

    """对常用笔刷, 启用压力大小."""
    print("set_brushes_setting")

    brush_data = [
        ("Draw", True, True, 0.5, 10),
        ("Draw Sharp", True, True, 0.5, 10),
        ("Clay", True, False, 0.9, 75),
        ("Clay Strips", True, True, 0.5, 10),
        ("Scrape/Fill", True, False, 0.9, 75),
        ("Trim", True, False, 0.9, 75),
        ("Inflate/Deflate", True, False, 0.9, 75),
    ]
    current_brush = bpy.context.tool_settings.sculpt.brush
    for item in brush_data:
        brush = set_brush(item[0])
        brush.use_pressure_size = item[1]
        # 防抖
        brush.use_smooth_stroke = item[2]
        brush.smooth_stroke_factor = item[3]
        brush.smooth_stroke_radius = item[4]
    """
    brush_names = [
        "Draw",  # 2
        "Draw Sharp",  # alt+2
        "Clay",  # 3
        "Clay Strips",  # alt+3
        "Scrape/Fill",  # 4
        "Trim",  # alt+4
        "Inflate/Deflate",  # 6
    ]
    for name in brush_names:
        brush = set_brush(name)
        brush.use_pressure_size = True
    """
    set_brush(current_brush.name)


def change_keymap(is_modify: bool):
    modify_keymap(sculpt_modify_keymaps, is_modify)


def register():
    set_brushes_setting()
    close_conflict_keys()
    change_keymap(True)
    keymap_register(sculpt_keys_items)


def unregister():
    close_conflict_keys(True)
    change_keymap(False)
    keymap_unregister(sculpt_keys_items)
