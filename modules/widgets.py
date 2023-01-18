from libqtile import widget
from .colors import materialDarker


# def triangle(fg, bg):
#     return widget.TextBox(
#         text=" ",
#         padding=-5,
#         fontsize=35,
#         foreground=materialDarker[fg],
#         backgroud=materialDarker[bg],
#     )


widgets = [
    widget.GroupBox(
        # font="Symbols Nerd Font",
        fontsize=16,
        margin_y=2,
        margin_x=0,
        padding_y=8,
        padding_x=6,
        border_width=1,
        active=materialDarker["active"],
        inactive=materialDarker["inactive"],
        rounded=False,
        highlight_method="block",
        urgent_alert_method="block",
        urgent_border=materialDarker["urgent"],
        this_current_screen_border=materialDarker["grey"],
        this_screen_border=materialDarker["grey"],
        disable_drag=True,
    ),

    widget.WindowName(
        font="CaskaydiaCove Nerd Font Semibold",
        fontsize=14,
        padding=8,
        foreground=materialDarker["focus"],
        max_chars=35,
    ),

    widget.TextBox(
        text=" ",
        padding=-5,
        fontsize=35,
        foreground=materialDarker["color4"],
        backgroud=materialDarker["dark"],
    ),

    widget.CheckUpdates(
        background=materialDarker["color4"],
        colour_have_updates=materialDarker["text"],
        colour_no_updates=materialDarker["text"],
        display_format=" {updates}",
        no_update_string=" 0",
        update_interval=1800,
        distro="Fedora",
        fontsize=16,
    ),

    widget.TextBox(
        text=" ",
        padding=-5,
        fontsize=35,
        foreground=materialDarker["color2"],
        background=materialDarker["color4"],
    ),

    widget.CurrentLayoutIcon(
        scale=0.7,
        background=materialDarker["color2"],
    ),

    widget.TextBox(
        text=" ",
        padding=-5,
        fontsize=35,
        foreground=materialDarker["color3"],
        background=materialDarker["color2"],
    ),

    widget.Volume(
        fmt="墳 {}",
        background=materialDarker["color3"],
        foreground=materialDarker["text"],
        fontsize=16,
    ),

    widget.TextBox(
        text=" ",
        padding=-5,
        fontsize=35,
        foreground=materialDarker["color1"],
        background=materialDarker["color3"],
    ),

    widget.Clock(
        format="%d/%m/%y %H:%M",
        fmt=" {} ",
        foreground=materialDarker["text"],
        background=materialDarker["color1"],
        # font="CaskaydiaCove Nerd Font Semibold",
        fontsize=16,
    ),

    widget.TextBox(
        text=" ",
        padding=-5,
        fontsize=35,
        foreground=materialDarker["dark"],
        background=materialDarker["color1"]
    ),

    widget.Systray(
        background=materialDarker["dark"],
        icon_size=20,
        padding=8,
    ),
]
