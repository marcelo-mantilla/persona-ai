import datetime


class DateService:
    def __init__(self, location=None):
        now = datetime.datetime.now()
        self.now = now
        self.time_of_day = now.strftime("%H:%M")
        self.day_of_week = now.strftime("%A")
        self.time_of_year = now.strftime("%B")
        self.year = now.strftime("%Y")

    def date_as_prompt(self) -> str:
        return f"It is currently {self.time_of_day} on a {self.day_of_week} in {self.time_of_year}, in the year {self.year}."
