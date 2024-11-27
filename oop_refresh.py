

class Microwave:
    def __init__(self,*,brand:str,power_rating:str) -> None:

        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self)->None:
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on")
        else:
            self.turned_on = True
            print(f"Microwave ({self.brand}) is now turned on")
    
    def turn_off(self)->None:
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave ({self.brand}) is now turned off")
        else:
            print(f"Microwave ({self.brand}) is already turned off")
    def run(self,seconds:int)->None:
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds')
        else:
            print(f'A mystical forcer whispers: "Turn on your microwave first..."')

    def __add__(self,other)-> None:
        return f'{self.brand} + {other.brand}'

    def __str__(self) -> str:
        return f'{self.brand} (Rating: {self.power_rating})'
    def __repr__(self) -> str:
        return f'Microwave(brand="{self.brand}", power_rating="{self.power_rating}")'
m1: Microwave = Microwave(brand="m1",power_rating="A+")

m2: Microwave = Microwave(brand="m2",power_rating="A-")


print(repr(m1))

