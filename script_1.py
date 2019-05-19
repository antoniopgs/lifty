import time
import datetime


class Exercise:

    def __init__(self, name, weight=0, sets=4, reps=12, rest=90, progression=2.5):
        self.name = name
        self.weight = weight  # kilograms
        self.sets = sets
        self.reps = reps
        self.rest = rest  # seconds
        self.progression = progression  # kilograms

    def train(self):
        with open("data.txt", "a") as file:
            file.write(f"{self.name} | {self.weight}kg\n")
        for i in range(1, self.sets + 1):
            print(f"{self.name} | {self.weight}kg | {self.sets} sets | {self.reps} reps")
            print(f"Set {i}: GO")
            performance = input("Completed Reps: ")
            with open("data.txt", "a") as file:
                file.write(f"Set {i} | {performance} reps\n")
            rest_time = self.rest
            while rest_time != 0:
                print(f"Time Left: {rest_time}")
                rest_time -= 1
                time.sleep(1)
            print()


def train(workout):
    now = datetime.datetime.now()
    timestamp = now.strftime("%A, %d %B %Y")
    print(f"\n----- START {chosen_workout} -----")
    with open("data.txt", "a") as file:
        file.write(f"{timestamp} | {chosen_workout}\n")
    for exercise in workout:
        exercise.train()
    print(f"----- {chosen_workout} WORKOUT DONE! -----\n")
    with open("data.txt", "a") as file:
        file.write("\n")

workouts = dict()

workouts["day_a"] = [Exercise("Squat", 80, rest=3), Exercise("Bench Press", 70, rest=3),
                     Exercise("Chin Ups", rest=3)]
workouts["day_b"] = [Exercise("Dumbell Curls", 10, rest=3), Exercise("Military Press", 30, rest=3)]

# ---------- MAIN CYCLE ----------
cycle = True
while cycle:
    try:
        user_input = int(input("""----- MENU -----
1 - Start Workout
2 - View History
3 - Settings
4 - Quit
    
Insert Command: """))
        if user_input == 1:
            workout_exists = False
            while not workout_exists:
                print("\n----- CHOOSE WORKOUT -----")
                for workout in workouts:
                    print(f"- {workout}")
                chosen_workout = input("\nInsert Workout: ")
                try:
                    train(workouts[chosen_workout])
                    workout_exists = True
                except KeyError:
                    print("Invalid Workout.")
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            cycle = False
        else:
            print("Invalid Command.\n")
    except ValueError:
        print("Invalid Command.\n")
