from libqtile import bar
from libqtile.config import Screen
from .widgets import widgets
from .colors import materialDarker

import os

screens = [
    Screen(
        top=bar.Bar(
            widgets,
            24,
            background=materialDarker["dark"],
            margin=0,
            opacity=0.85,
            font="CaskaydiaCove Nerd Font",
        ),
    ),
]
