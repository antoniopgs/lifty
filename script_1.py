import time
import sqlite3

class Exercise:

    def __init__(self, name, weight=0, sets=3, reps=12, rest=90, progression=2.5):
        self.name = name
        self.weight = weight  # kilograms
        self.sets = sets
        self.reps = reps
        self.rest = rest  # seconds
        self.progression = progression  # kilograms

    def train(self):
        for i in range(1, self.sets + 1):
            print(f"{self.sets} sets of {self.name} - {self.weight} kg")
            print(f"Set {i}: GO")
            done = input("Type \"done\" when completed: ")
            rest_time = self.rest
            while rest_time != 0:
                print(f"Time Left: {rest_time}")
                rest_time -= 1
                time.sleep(1)
            print()


def train(workout):
    for exercise in workout:
        exercise.train()
    print("Workout Done!")


day_a = [Exercise("Squat", 80, rest=10), Exercise("Bench Press", 70, rest=10), Exercise("Chin Ups", rest=10)]
