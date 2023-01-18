from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
alt = "mod1"
terminal = "alacritty"

keys = [
    # Switch between windows
    Key([mod],
        "h",
        lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod],
        "l",
        lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod],
        "j",
        lazy.layout.down(),
        desc="Move focus down"),
    Key([mod],
        "k",
        lazy.layout.up(),
        desc="Move focus up"),
    Key([mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.grow(),
        desc="Grow window"),
    Key([mod, "control"],
        "l",
        lazy.layout.shrink(),
        desc="Shrink window"),
    Key([mod],
        "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes

    # Launch Rofi
    Key([alt], "Space", lazy.spawn("rofi -modi drun, run -show drun -font 'CaskaydiaCove Nerd Font' -show-icons"), desc="spawn rofi"),

    # Launch Terminal
    Key([alt], "Return", lazy.spawn(terminal), desc = "Launch terminal"),

    # Launch Web Browser
    Key([alt], "w", lazy.spawn("brave-browser"), desc = "Launch Web Browser"),

    # Launch Visual Studio Code
    Key([alt], "c", lazy.spawn("code"), desc = "Launch Visual Studio Code"),

    # Launch Discord
    Key([alt], "d", lazy.spawn("discord"), desc = "Launch Discord"),

    # Launch Spotify
    Key([alt], "m", lazy.spawn("flatpak run com.spotify.Client"), desc = "Launch Spotify"),

    # Launch File Manager
    Key([alt], "f", lazy.spawn("thunar"), desc = "Launch File Manager"),

    # Launch Telegram
    Key([alt], "t", lazy.spawn("telegram"), desc = "Launch Telegram"),

    # Launch Slack
    Key([alt], "s", lazy.spawn("slack"), desc = "Launch Slack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),

    # Shutdown Qtile
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Control Volume
    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 5%+")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 5%-")),
    Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),

    # Bright Control
    Key([], "XF86MonBrightnessUp",lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown",lazy.spawn("brightnessctl set 10%-")),

    # Playback Control
    Key([], "XF86AudioNext",lazy.spawn("playerctl -p spotify next")),
    Key([], "XF86AudioPrev",lazy.spawn("playerctl -p spotify previous")),
    Key([], "XF86AudioPlay",lazy.spawn("playerctl -p spotify play-pause")),
]
