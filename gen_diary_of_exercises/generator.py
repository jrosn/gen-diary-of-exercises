import random
from abc import abstractmethod


class ExerciseType(object):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_property_range(self):
        pass

    @abstractmethod
    def get_property_suffix(self):
        pass


class JumpingOnPlaceExerciseType(ExerciseType):
    def get_name(self):
        return "Прыжки на месте"

    def get_property_range(self):
        return [5, 50]

    def get_property_suffix(self):
        return "раз"


class PushUpsExerciseType(ExerciseType):
    def get_name(self):
        return "Отжимания"

    def get_property_range(self):
        return [5, 25]

    def get_property_suffix(self):
        return "раз"


class SquattingExerciseType(ExerciseType):
    def get_name(self):
        return "Приседания"

    def get_property_range(self):
        return [5, 50]

    def get_property_suffix(self):
        return "раз"


class PullUpExerciseType(ExerciseType):
    def get_name(self):
        return ""

    def get_property_range(self):
        pass

    def get_property_suffix(self):
        pass


# Все возможные типы упражнений
EXERCISE_TYPES = [
    JumpingOnPlaceExerciseType(),
    PushUpsExerciseType(),
    SquattingExerciseType()
]


class Exercise:
    def __init__(self, exercise_type, property):
        self.exercise_type = exercise_type
        self.property = property

    def __str__(self):
        return "{}: {} {}".format(
            self.exercise_type.get_name(),
            str(self.property),
            self.exercise_type.get_property_suffix()
        )

    @staticmethod
    def random():
        ex_type = random.choice(EXERCISE_TYPES)
        return Exercise(exercise_type=ex_type,
                        property=random.randint(*ex_type.get_property_range()))
