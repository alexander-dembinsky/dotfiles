import configparser
import os


class Theme:

    def __init__(self):
        self.bar_background_1 = "#000000"
        self.bar_background_2 = "#222222"
        self.group_active = "#FFFFFF"
        self.group_inactive = "#CCCCCC"
        self.apps_background = "#505562"
        self.window_name_foreground = "#DDDDDD"
        self.group_icon_background = "#000000"
        self.group_icon_foreground = "#FFFFFF"
        self.widget_default_background = "#505562"
        self.border_focus = "#5294E2"


class ThemeConfigReader:

    @staticmethod
    def read(theme_name):
        config = configparser.ConfigParser()

        themefile = "{home}/.config/qtile/themes/{theme}.theme".format(
                     home=os.path.expanduser("~"),
                     theme=theme_name
                )
        config.read(themefile)

        colors = config["colors"]

        theme = Theme()
        theme.bar_background_1 = colors["bar.background1"]
        theme.bar_background_2 = colors["bar.background2"]
        theme.group_active = colors["group.active"]
        theme.group_inactive = colors["group.inactive"]
        theme.apps_background = colors["apps.background"]
        theme.window_name_foreground = colors["window.name.foreground"]
        theme.group_icon_foreground = colors["group.icon.foreground"]
        theme.group_icon_background = colors["group.icon.background"]
        theme.widget_default_background = colors["widget.default.background"]
        theme.border_focus = colors["border.focus"]

        return theme
