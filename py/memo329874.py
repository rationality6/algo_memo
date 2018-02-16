class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge >= 0:
            self.age = initialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        my_age = self.age
        if my_age < 13:
            print("You are young.")
        elif my_age >= 13 and my_age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
