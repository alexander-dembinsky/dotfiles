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
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger

import os
import subprocess
import sys
import psutil

mod = "mod4"
alt = "mod1"
terminal = guess_terminal()
fileman = "thunar"
browser = "firefox"
widget_font_big=18

colors = {
        "primary": "#5677fc",
        "secondary": "#505562",
        "group_active": "#ffffff",
        "group_inactive": "#a9a9a9",
        "window_name": "#dddddd",
        "group_icon": "#ff0000",

        "primary_focus": "#5294e2",
        "secondary_focus": "#000080ff",
        "bar_background": "#353945",
        "bar_text": "#dddddd",
}


keyboard_layouts = ["us","ru","ua"]
keyboard_layout_widget = widget.KeyboardLayout(configured_keyboards=keyboard_layouts, fontsize=widget_font_big, background=colors["secondary"])

volume_widget = widget.Volume(volume_app="pavucontrol", padding=0, step=10, background=colors["primary"])

def generate_arrows(primary_color, secondary_color):
    home = os.path.expanduser("~")
    qtile.cmd_spawn("sh " + home + "/.config/qtile/generate_arrows.sh {primary_color} {secondary_color}".format(primary_color=primary_color.lstrip('#'), secondary_color=secondary_color.lstrip('#')))

def switch_keyboard_layout(qtile):
    keyboard_layout_widget.next_keyboard()

def shutdown():
    home = os.path.expanduser("~")
    qtile.cmd_spawn("sh " + home + "/.config/qtile/shutdown.sh")

def show_calendar():
    home = os.path.expanduser("~")
    qtile.cmd_spawn("sh " + home + "/.config/qtile/show_calendar.sh")


def run_launcher():
    home = os.path.expanduser("~")
    qtile.cmd_spawn("sh " + home + "/.config/qtile/app_menu.sh")


generate_arrows(colors["primary"], colors["secondary"])

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "space", lazy.layout.next(),
        #desc="Move window focus to other window"),

        
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

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod, "shift"], "t", lazy.window.toggle_floating(), desc="Toggle floating layout"),

    # Screenshot
    Key([mod, "shift"], "Print", lazy.spawn("spectacle -r"), desc="Area screenshot"),
    Key([], "Print", lazy.spawn("spectacle"), desc="Screenshot"),
    # File Manager
    Key([mod], "e", lazy.spawn(fileman), desc="File Manager"),
    # Browser
    Key([mod], "f", lazy.spawn(browser), desc="Web Browser"),
 
    # Vim
    Key([mod], "v", lazy.spawn(terminal + " -e vim"), desc="Vim"),

    # Rofi
    Key([mod], "r", lazy.function(lambda qtile: run_launcher()), desc="Launcher"),
    # Shutdown
    Key([mod, "control"], "F12", lazy.function(lambda qtile: shutdown()), desc="Shutdown menu"),
    # Lock screen
    Key([mod, "control"], "l", lazy.spawn("dm-tool lock"), desc="Lock screen"),
    # Task list
    Key([alt], "Tab", lazy.spawn("rofi -show window"), desc="Show current tasks"),

    # Moving between groups
    Key(["control", alt], "Left", lazy.screen.prev_group(), desc="Prev Group"),
    Key(["control", alt], "Right", lazy.screen.next_group(), desc="Next Group"),

    # Resize windows

    Key(["control", alt], "g", lazy.layout.grow(), desc="Grow"),
    Key(["control", alt], "s", lazy.layout.shrink(), desc="Shrink"),
    Key(["control", alt], "n", lazy.layout.normalize(), desc="Normalize"),
    Key(["control", alt], "m", lazy.layout.maximize(), desc="Maximize"),

    # Fn keys
    Key([], "XF86AudioRaiseVolume", lazy.function(lambda qtile: volume_widget.cmd_increase_vol())),
    Key([], "XF86AudioLowerVolume", lazy.function(lambda qtile: volume_widget.cmd_decrease_vol())),
    Key([], "XF86AudioMute", lazy.function(lambda qtile: volume_widget.cmd_mute())),
]

#groups = [Group(i) for i in "123456789"]
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
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    #layout.Columns(border_focus_stack='#d75f5f'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_focus=colors["primary_focus"], margin=6),
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
                    mouse_callbacks={"Button1": run_launcher},
                    margin=4, background=colors["secondary"]
                ),
                widget.GroupBox(
                    background=colors["secondary"],
                    inactive=colors["group_inactive"],
                    active=colors["group_active"]
                ),
                widget.Image(
                    filename="~/.config/qtile/img/arrow_right_secondary.svg"
                ),
                widget.WindowName(
                    foreground=colors["window_name"],
                    fontsize=16
                ),
                widget.Image(
                    filename="~/.config/qtile/img/arrow_left_secondary.svg"
                ),
                widget.CurrentLayoutIcon(
                    scale=0.6,
                    background=colors["secondary"],
                    foreground=colors["group_icon"]
                ),
                keyboard_layout_widget,
                widget.Systray(
                    icon_size=22,
                    padding=6,
                    background=colors["secondary"]
                ),
                widget.Sep(
                    background=colors["secondary"],
                    linewidth=8,
                    foreground=colors["secondary"]
                ),
                widget.Clock(
                    format="%m/%d %H:%M",
                    fontsize=widget_font_big,
                    background=colors["secondary"],
                    mouse_callbacks={"Button1": show_calendar}
                ),
                widget.Image(
                    filename="~/.config/qtile/img/shutdown.svg",
                    mouse_callbacks={"Button1": shutdown},
                    margin=4,
                    background=colors["secondary"]
                ),
            ],
            32,
            opacity=1,
            background=colors["bar_background"],
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
])
auto_fullscreen = False
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
    subprocess.Popen([home + "/.config/qtile/autostart.sh"])

