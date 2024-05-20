# this code takes the information of the car brand, model, and purchased_year to
# calculate the depreciation(decrease in value of your assets over a period of time) and vintage(to check whether the car is older than 25 years)

class Car:
    def __init__(self, brand, model, purchased_year):
        self.brand = brand
        self.model = model
        self.purchased_year = purchased_year

    # display the car information
    def car_info(self):
        print(f"The car brand is {self.brand} and model is {self.model}  ,purchased in year {self.purchased_year}")

    age = 0

    # takes initial value of the car and current year ,then first calculates the current_value of the car and depreciation value
    def depreciation(self, initial_value,current_year):
        age = current_year - self.purchased_year
        current_value = initial_value * ((1 - 0.15)**age)
        depreciation_value = initial_value - current_value
        print(f"Current value is : {current_value}")
        print(f"The depreciation of the car is : {depreciation_value}")

    # checks whether car is 25 years older or not
    def vintage(self,current_year):
        car_age = current_year - self.purchased_year
        if car_age > 25:
            print(f"The car is vintage, as it is {car_age} years old (greater than 25 years).")
        else:
            print(f"The car is {car_age} years old, which is not considered vintage.")


car_brand = input("Enter the brand : ")
car_model = input("Enter the model : ")
car_purchased_year = int(input("Enter the purchased_year : "))
car1 = Car(car_brand,car_model,car_purchased_year)

car1.car_info()

# depreciation calculation
value = int(input("Enter the initial value of your car : "))
year = int(input("Enter the current year : "))
car1.depreciation(value, year)

# vintage calculation
car1.vintage(year)


