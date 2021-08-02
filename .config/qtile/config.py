# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

# Theming ##########################################
import theme

theme_name = "default"
theme_config_reader = theme.ThemeConfigReader()
theme = theme_config_reader.read(theme_name)

####################################################
mod = "mod4"
alt = "mod1"
terminal = guess_terminal()
widget_font_big = 18

keyboard_layouts = ["us", "ru", "ua"]
keyboard_layout_widget = widget.KeyboardLayout(
        configured_keyboards=keyboard_layouts,
        fontsize=widget_font_big, background=theme.widget_default_background
)

volume_widget = widget.Volume(volume_app="pavucontrol")


def run_script(scriptAndArgs):
    home = os.path.expanduser("~")
    qtile.cmd_spawn("sh " + home + "/.config/qtile/scripts/" + scriptAndArgs)


def generate_arrows(color):
    args = ("000000 " +
            color.lstrip('#'))
    run_script("generate_arrows.sh " + args)


def switch_keyboard_layout(qtile):
    keyboard_layout_widget.next_keyboard()


def show_calendar():
    run_script("show_calendar.sh")


generate_arrows(theme.widget_default_background)

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Switch keyboard layout TODO: Move to xshkd
    Key([mod], "space", lazy.function(switch_keyboard_layout),
        desc="Switch Keyboard Layout"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "t", lazy.window.toggle_floating(),
        desc="Toggle floating layout"),

    # Moving between groups
    Key([alt, "shift"], "Tab", lazy.screen.prev_group(), desc="Prev Group"),
    Key([alt], "Tab", lazy.screen.next_group(), desc="Next Group"),

    # App menu
    Key([mod], "r", lazy.function(lambda qtile: run_script("app_menu.sh")),
        desc="Launcher"),

    # Shutdown
    Key([mod, "control"], "F12", lazy.function(
        lambda qtile: run_script("shutdown.sh")),
        desc="Shutdown menu"),

    # Resize windows

    Key(["control", alt], "g", lazy.layout.grow(), desc="Grow"),
    Key(["control", alt], "s", lazy.layout.shrink(), desc="Shrink"),
    Key(["control", alt], "n", lazy.layout.normalize(), desc="Normalize"),
    Key(["control", alt], "m", lazy.layout.maximize(), desc="Maximize"),

    # Fn keys TODO: Check if it will work only with xshkd
    Key([], "XF86AudioRaiseVolume", lazy.function(
        lambda qtile: volume_widget.cmd_increase_vol())),
    Key([], "XF86AudioLowerVolume", lazy.function(
        lambda qtile: volume_widget.cmd_decrease_vol())),
    Key([], "XF86AudioMute", lazy.function(
        lambda qtile: volume_widget.cmd_mute())),
]

groups = [
        Group("1", init=True, matches=Match(title="Firefox")),
        Group("2", matches=Match(wm_class="Microsoft Teams - Preview")),
        Group("3", matches=Match(wm_class="Wfica"), layout="max"),
        Group("4"),
        Group("5"),
        Group("6"),
        Group("7"),
        Group("8"),
        Group("9"),
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name,
            switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

layouts = [
    # layout.Columns(border_focus_stack='#d75f5f'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_focus=theme.border_focus, margin=6),
    layout.Max(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Sans',
    fontsize=14,
    padding=6,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename="~/.config/qtile/img/apps.svg",
                    mouse_callbacks={
                        "Button1": lambda: run_script("app_menu.sh")
                    },
                    margin=4,
                    background=theme.apps_background,
                ),
                widget.GroupBox(
                    inactive=theme.group_inactive,
                    active=theme.group_active,
                    background=theme.widget_default_background
                ),
                widget.Image(
                    filename="~/.config/qtile/img/arrow_right_secondary.svg"
                ),
                widget.WindowName(
                    foreground=theme.window_name_foreground,
                    fontsize=16,
                ),
                widget.Image(
                    filename="~/.config/qtile/img/arrow_left_secondary.svg"
                ),
                widget.CurrentLayoutIcon(
                    scale=0.6,
                    background=theme.group_icon_background,
                    foreground=theme.group_icon_foreground,
                ),
                keyboard_layout_widget,
                widget.Systray(
                    icon_size=22,
                    padding=6,
                    background=theme.widget_default_background
                ),
                widget.Sep(
                    linewidth=8,
                    foreground=theme.widget_default_background,
                    background=theme.widget_default_background
                ),
                widget.Clock(
                    format="%m/%d %H:%M",
                    fontsize=widget_font_big,
                    mouse_callbacks={"Button1": show_calendar},
                    background=theme.widget_default_background
                ),
                widget.Image(
                    filename="~/.config/qtile/img/shutdown.svg",
                    mouse_callbacks={
                        "Button1": lambda: run_script("shutdown.sh")
                    },
                    margin=4,
                    background=theme.widget_default_background
                ),
            ],
            32,
            opacity=1,
            background=[theme.bar_background_1, theme.bar_background_2]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_width=0, float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='Steam'),
    Match(title='Calendar'),
    Match(wm_class='arcologout.py'),
    Match(wm_class='Variety'),
    Match(title='plank'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


# Autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen([home + "/.config/qtile/scripts/autostart.sh"])
