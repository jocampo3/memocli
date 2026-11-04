from datetime import date, timedelta

class Date:
    def __init__(self) -> None:
        self.valid_days : dict[str, int] = {
            "monday" : 0,
            "tuesday" : 1,
            "wednesday" : 2,
            "thursday" : 3,
            "friday" : 4,
            "saturday" : 5,
            "sunday" : 6,
            "today": -1,
            "tomorrow": -1
        }

        self.is_valid : bool = False
        self.day = None

    def update_date_string(self, day) -> None:
        today = date.today()
        days_ahead = (self.valid_days[day] - today.weekday()) % 7

        if days_ahead == 0:
            days_ahead = 7
        elif day == "today":
            days_ahead = 0
        elif day == "tomorrow":
            days_ahead = 1

        self.day = (today + timedelta(days=days_ahead)).strftime("%m-%d-%y")


    def validate(self, day : str) -> None:
        if day.lower() in self.valid_days:
            self.is_valid = True
            self.update_date_string(day.lower())
