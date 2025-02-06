# 魔改说明 - 2025年2月4日
1. 使用Blender原生功能命令替换掉BBrush雕刻工具，优点是效率高、流畅不卡顿，缺点是少功能：
   1. 不能Alt+左键切换对象，只能老老实实用Alt+Q。
   2. 无法通过左键+拖拽调整左上角的剪影图大小。
2. 改了开启BBrush功能的UI的位置和表现形式。
3. 删除了Switch的Alt键，不太清楚有什么用，且和我的笔刷快捷键冲突（Alt+1/2/3/4/5/...）。
4. 切换开启与关闭BBrush功能，会遗留3个雕刻快捷键，测试没啥影响，那就能用就行。（It’s not a bug, it’s a feature!）

# Bbrush

This is an addon for Blender that simulates the way ZBrush sculpts.

Also can display silhouette, much convenient for tablets.

![981b5107_9588511](https://github.com/user-attachments/assets/f02b0b50-e4ad-4e7b-9817-fec10ade2e6a)


## Features

### Silhouette

When enable the silhouette, you can modify it in preferences or at the tool settings.

#### Disaply mode

- **Always**: Keep silhouette on toop even not in sculpt mode
- **Only Sculpt**: Disaply in sculpt mode
- **Only Bbrush**: Disply in Bbrush mode
- **Disable**: Don't display

#### Scale

![c275d79d_9588511](https://github.com/user-attachments/assets/3485e5d1-ce2f-4214-9483-db4c2d65b9aa)


### Bbrush mode

When enter sculpt mode, top bar will have a Bbrush mode button.
Bbrush mode has many shorcuts:
#### Normal Mode.
Shows frequently used brushes

    View Manipulation
        Panning ALT+Right or ALT+Center
        Panning ALT+Left Drag on blank space
        Panning view SHIFT+Middle key
        Rotate view Right click
        Rotate view Left-click Drag in blank area
        Zoom View CTRL+Middle or CTRL+Right
        Skew View SHIFT+Left Drag in empty space
    Sculpting
        Sculpt Left click Draw on the model
        Reverse Sculpt ALT+Left click Draw on model
        Smooth SHIFT+Left click Draw on model
    Other
        Toggle engraved objects ALT+Left click on other models

#### Mask mode (Ctrl or Ctrl Alt).
When in mask mode, the brush will be switched to a mask brush.

    Draw Mask CTRL+Left click to draw on the model.
    Erase Mask CTRL+ALT+Left to draw on the model.
    Invert Mask CTRL+Left Click on blank area
    Frame Mask CTRL+Left click Drag from blank area to model
    Box Erase Mask CTRL+ALT+left click Drag from blank area to model
    Fade Mask CTRL+left click on model
    Clear Mask CTRL+Left click Draw box on blank area
    Sharpen Mask CTRL+ALT+left click on model
    Fill Mask CTRL+ALT+Left Click to draw a box in a blank area.
    Growth Mask CTRL+Keypad+Sign Click
    Shrink Mask CTRL+Keypad - Sign Click
    Increase Mask Contrast CTRL+Up Arrow or CTRL+Keypad* Click
    Decrease Mask Contrast CTRL+Down Arrow or CTRL+Keypad/ Click

#### Hidden Mode.
Brushes will switch to hidden mode.

    Hide Outside Paint Box CTRL+SHIFT+Left click Paint on Model
    Inside the hidden drawing box CTRL+SHIFT+ALT+Left click Draw on the model.
    Unhide CTRL+SHIFT+Left click in blank area (will not work if you add multi-level subdivision modifier, this is Bl's own problem)
    Reverse hide CTRL+SHIFT+Left click or CTRL+SHIFT+ALT+Left click Draw on the blank area.

## Notice

- Switch hidden faces will cause multiresolution disabled
- Blender 3.0 + smooth brushes + invert sculpt = crash
