# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import keys, mod

groups = [Group(i) for i in ["  ", "  ", " ﬏ ", "  ", "  ", " 阮 ", "  ", "  ", "  "]]
group_hotkeys = "123456789"

for g, k in zip(groups, group_hotkeys):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            k,
            lazy.group[g.name].toscreen(),
            desc="Switch to group {g.name}"),

        Key([mod], "Right", lazy.screen.next_group(),
            desc="Switch to next group"),

        Key([mod], "Left", lazy.screen.prev_group(),
            desc="Switch to previous group"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],
            k,
            lazy.window.togroup(g.name, switch_group=False),
            desc="Switch to & move focused window to group {g.name}"),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
