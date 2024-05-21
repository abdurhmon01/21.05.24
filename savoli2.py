class Velik:
    def __init__(self,color,name,year):
        self.name=name
        self.color=color
        self.year=year

car=Velik(name="Toyota",color="Red",year=2008)
print(f"Car name: {car.name}")
print(f"Car color: {car.color}")
print(f"Car year{car.year}")