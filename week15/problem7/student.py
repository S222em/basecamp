import datetime


class Student:
    """
    Represents a student
    """

    def __init__(self, first_name, last_name, date_of_birth, class_code, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.class_code = class_code
        self.id = id

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = datetime.date.today()
        birth = datetime.datetime.strptime(self.date_of_birth, "%Y-%m-%d")

        correction = 1 if today.month < birth.month or (today.month == birth.month and today.day < birth.day) else 0

        return today.year - birth.year - correction

    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))
