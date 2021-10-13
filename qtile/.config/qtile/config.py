from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal, logger
import os
import subprocess
from inline_calendar import InlineCalendar

mod = "mod4"
terminal = guess_terminal()

# Keyboard
keyboards=["us","ru"]
keyboard_layout = widget.KeyboardLayout(configured_keyboards=keyboards)

def show_popup_calendar(_=None):
    qtile.cmd_spawn(["python", os.path.expanduser("~/.config/qtile/popup_calendar.py")])

keys = [
    Key([mod], "space", lazy.function(lambda qtile: keyboard_layout.next_keyboard()), desc="Switch keyboard layout"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
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
    Key([mod], "Tab", lazy.next_layout(), desc="Move window focus to other window"),

    Key([mod], "b", lazy.hide_show_bar("top")),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),

    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),


    # Programs
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "Return", lazy.spawn("pcmanfm"), desc="File manager"),
    Key([mod, "shift"], "f", lazy.spawn("firefox"), desc="Web browser"),
    Key([mod], "p", lazy.spawn("rofi -show-icons -show drun"), desc="Launcher"),
    Key([mod, "shift"], "p", lazy.spawn("rofi -show-icons -show run"), desc="Launcher"),
    Key([mod, "shift"], "w", lazy.spawn("rofi -show window"), desc="Window switcher"),
    Key([mod, "shift"], "n", lazy.spawn("alacritty -e newsboat"), desc="News"),
    Key([mod, "shift"], "x", lazy.spawn("arcolinux-logout"), desc="Logout"),
    Key([mod, "shift"], "v", lazy.spawn("pavucontrol"), desc="Volume mixer"),
    Key([mod, "shift"], "c", lazy.function(show_popup_calendar), desc="Popup calendar"),
    Key([mod, "shift"], "Print", lazy.spawn(os.path.expanduser("~/.config/qtile/screenshot")), desc="Screenshot"),
    Key([mod], "F5", lazy.spawn(os.path.expanduser("~/.bin/tv")), desc="TV script"),
    Key([mod, "shift"], "a", lazy.spawn("arandr"), desc="Screen configuration"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.MonadTall(border_focus=['#4e94e2'], border_width=1, margin=4),
    layout.Max()
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
                widget.Image(filename='~/.config/qtile/launcher.svg', mouse_callbacks={
                    'Button1': lambda: qtile.cmd_spawn("xfce4-appfinder")
                }),
                widget.GroupBox(inactive="#aaaaaa"),
                widget.Sep(size_percent=60),
                widget.Prompt(prompt='> ', fmt='<span color="green"><b>{}</b></span>'),
                widget.TaskList(),
                widget.Image(margin=5, filename='~/.config/qtile/close.svg', mouse_callbacks={
                    'Button1': lambda: qtile.current_window.cmd_kill()
                }),
                widget.Sep(size_percent=60),
                widget.CurrentLayoutIcon(scale=0.6),
                keyboard_layout,
                widget.Sep(size_percent=60),
                widget.Systray(),
                widget.Sep(size_percent=60),
                InlineCalendar(mouse_callbacks={'Button1': show_popup_calendar}),
                widget.Sep(size_percent=60),
                widget.TextBox(text="🕑"),
                widget.Clock(format='<span size="xx-small"><tt>%m-%d-%y</tt></span>\n<span size="medium"><tt>%H:%M</tt></span>'),
            ],
            32,
            background="#2B2E3F"
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Drag([], "Button8", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([], "Button9", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = "floating_only"
cursor_warp = False
floating_layout = layout.Floating(border_focus='#aaaaaa', float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='steam'),  # Steam
    Match(wm_class='pavucontrol'),  # Volume mixer
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='popup_calendar.py'), # popup_calendar
    Match(wm_class='arandr'), # ARandr
    Match(wm_class="xfce4-appfinder"),
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"



@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


@hook.subscribe.client_focus
def func(c):
    info = c.cmd_inspect()
    if "popup_calendar.py" in info['wm_class']:
        (x, y) = c.cmd_get_position()
        (width, height) = c.cmd_get_size()
        c.cmd_place(x, y, width, height, 0, "#ffffff")

