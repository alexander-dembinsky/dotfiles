# Qtile configuration file

import os
import subprocess
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal, logger

mod = "mod4"
terminal = guess_terminal()
home = os.path.expanduser('~')

def disable_floating_for_group(qtile):
    for w in qtile.current_group.windows:
        w.cmd_disable_floating()

def run_script(script_path):
    script = os.path.expanduser(script_path)
    subprocess.call([script])

colors = {
        "sep": "#505050",
        "bar_background": "#333333",
        "float_border_normal": "#222222",
        "float_border_focus": "#008080",
        "monadtall_border_normal": "#222222",
        "monadtall_border_focus": "#8080ff",
        "groupbox_sel": "#505050",
        "groupbox_active": "#8080ff",
        "groupbox_inactive": "#ffffff",
        "tasklist_sel": "#505050",
}

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

	# MonadTall
	Key([mod], "h", lazy.layout.left()),
	Key([mod], "l", lazy.layout.right()),
	Key([mod], "j", lazy.layout.down()),
	Key([mod], "k", lazy.layout.up()),
	Key([mod, "shift"], "h", lazy.layout.swap_left()),
	Key([mod, "shift"], "l", lazy.layout.swap_right()),
	Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
	Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
	Key([mod], "i", lazy.layout.grow()),
	Key([mod], "m", lazy.layout.shrink()),
	Key([mod], "n", lazy.layout.normalize()),
	Key([mod], "o", lazy.layout.maximize()),
	Key([mod, "shift"], "space", lazy.layout.flip()),

    Key([mod, "control"], "j", lazy.group.next_window(), desc="Focus next window"),
    Key([mod, "control"], "k", lazy.group.prev_window(), desc="Focus prev window"),

    Key(["mod1"], "Tab", lazy.screen.next_group(), desc="Next group"),
    Key(["mod1", "shift"], "Tab", lazy.screen.prev_group(), desc="Prev group"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("{home}/.config/qtile/scripts/app_menu.sh".format(home=home)),
        desc="Spawn a command using a prompt widget"),

    # Keyboard Layout Switch
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),

    # Toggle floating
    Key([mod, "control"], "f", lazy.window.toggle_floating(), desc="Toggle floating layout"),
    Key([mod, "control"], "t", lazy.function(disable_floating_for_group), desc="Disable floating for all windows in the current group"),
]

groups = [
        Group("1"),
        Group("2", matches=[Match(wm_class=["microsoft teams - preview"])]),
        Group("3", matches=[Match(wm_class=["Wfica"])]),
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
    ])

floating_layout = layout.Floating(border_width=2, border_normal=colors["float_border_normal"], border_focus=colors["float_border_focus"], float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='Steam'),  # Steam
    Match(wm_class='Skype'),  # Skype
    Match(title='Variety Images'),  # Steam
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

    
layouts = [
    layout.MonadTall(
        margin=6,
        border_width=2, 
        border_normal=colors["monadtall_border_normal"],
        border_focus=colors["monadtall_border_focus"]
    ),
    layout.Max(),
]

widget_defaults = dict(
    font='Noto Sans',
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(margin_x=10, margin_y=2, filename="{home}/.config/qtile/img/launcher.png".format(home=home), 
                    mouse_callbacks={"Button1": lambda: run_script("~/.config/qtile/scripts/app_menu.sh") }
                ),
                widget.Image(margin_x=10, margin_y=2, filename="{home}/.config/qtile/img/places.png".format(home=home), 
                    mouse_callbacks={"Button1": lambda: run_script("~/.config/qtile/scripts/places_menu.sh") }
                ),
                widget.LaunchBar(padding=10, progs=[
                    ("firefox","firefox","Firefix web browser"),
                    ("gvim","alacritty -e vim","Text Editor"),
                    ("teams","teams","MS Teams"),
                    ("steam","steam","Steam"),
                ]),
                widget.Sep(foreground=colors["sep"], padding=10),
                widget.GroupBox(highlight_method='block',
                    this_current_screen_border=colors["groupbox_sel"],
                    active=colors["groupbox_active"],
                    inactive=colors["groupbox_inactive"],
                    rounded=False
                ),
                widget.Sep(foreground=colors["sep"], padding=10),
                widget.TaskList(highlight_method='block', 
                    border=colors["tasklist_sel"],
                    rounded=False, 
                    icon_size=24, 
                    padding_x=6,
                    spacing=6,
                    txt_floating="🗗 ",
                    txt_minimized="🗕 ",
                    txt_maximized="🗖 ",
                ),
                widget.Sep(foreground=colors["sep"], padding=10),
                widget.CurrentLayoutIcon(scale=0.8),
                widget.Image(margin_y=3, filename="{home}/.config/qtile/img/tile.svg".format(home=home), 
                    mouse_callbacks={"Button1": lambda: disable_floating_for_group(qtile) }
                ),
                widget.Sep(foreground=colors["sep"], padding=10),
                widget.KeyboardLayout(configured_keyboards=["us","ru","ua"], fontsize=20),
                widget.Systray(icon_size=26),
                widget.Clock(format='%d/%m/%Y %H:%M', fontsize=18),
                widget.Image(margin_x=10, margin_y=6, filename="{home}/.config/qtile/img/shutdown.png".format(home=home), 
                    mouse_callbacks={"Button1": lambda: run_script("~/.config/qtile/scripts/shutdown_menu.sh") }
                ),
            ],
            30,
            background=colors["bar_background"]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([], "Button9", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Drag([], "Button8", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.call([script])

