class Course:
    """
    Represents a course
    """

    def __init__(self, name, points, id=None):
        self.name = name
        self.points = points
        self.id = id

    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))
