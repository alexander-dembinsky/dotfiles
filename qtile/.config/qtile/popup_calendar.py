import gi
import argparse

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk


class CalendarWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Calendar")
        self.set_skip_pager_hint(True)
        self.set_skip_taskbar_hint(True)
        self.set_border_width(10)
        self.set_resizable(False)
        self.set_decorated(False)
        self.set_type_hint(Gdk.WindowTypeHint.NORMAL)

        self.calendar = Gtk.Calendar()
        self.add(self.calendar)

def on_key_pressed(_, e):
    _, key_val = e.get_keyval()
    if key_val == Gdk.KEY_Escape:
        Gtk.main_quit()


parser = argparse.ArgumentParser()
parser.add_argument('--x', type=int)
parser.add_argument('--y', type=int)
parser.add_argument('--width', type=int)
parser.add_argument('--height', type=int)
args = parser.parse_args()

win = CalendarWindow()
win.connect("destroy", Gtk.main_quit)
win.connect("focus-out-event", Gtk.main_quit)
win.connect("key-press-event", on_key_pressed)
win.set_size_request(args.width or 300, args.height or 300)

win.move(args.x or 0, args.y or 0)
win.show_all()
Gtk.main()
