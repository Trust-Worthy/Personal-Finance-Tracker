

class Microwave:
    def __init__(self,*,brand:str,power_rating:str) -> None:

        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self)->None:
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on")



m1: Microwave = Microwave(brand="yeep",power_rating="A+")

