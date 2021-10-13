import libqtile.widget.base as base
import datetime

class InlineCalendar(base.InLoopPollText):

    defaults = [
            ("interal", 60, "Update interval in seconds"),
            ("prefix", "📅 ", "Widget prefix")
    ]

    def __init__(self, **config):
        super().__init__(**config)
        self.add_defaults(InlineCalendar.defaults)
    
    def poll(self):
        today = datetime.date.today()
        last_monday = today - datetime.timedelta(days=today.weekday())

        week_dates = [last_monday + datetime.timedelta(days=i) for i in range(0, 7)]              
        line = self.prefix 
        for d in week_dates:
            line += self.format_day(d)

        return line

    def format_day(self, d):
        # Current day
        if d == datetime.date.today():
            return "<span color='green'>{day} </span>".format(day=d.day)

        # Weekend
        if d.weekday() >= 5:
            return "<span color='red'>{day} </span>".format(day=d.day)

        # Working day
        return "{day} ".format(day=d.day)
