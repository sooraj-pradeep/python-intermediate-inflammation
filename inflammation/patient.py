class Doctor:
    def __init__(self, name: str, patients: list):
        self.name = name
        self.patients = patients

    def __str__(self):
        return "Doctor's name is " + self.name 


Sruthy = Doctor("Sruthy Pradeep", ["Sooraj", "Pradeep"])

print(Sruthy.patients)