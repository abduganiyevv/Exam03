class Car:
    def __init__(self,brend,model,year,):
        self.brand = brend
        self.model = model
        self.year = year
    
    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model
    

    def get_year(self):
        return self.year
        
    def get_fullname(self):
        return f"{self.brand} {self.model} {self.year}"    
    
    def tanishtir(self):
        print(f" {self.brand} {self.model}. {self.year} ")    

        
car = Car("BMW", "X5", 2020)
print(car.tanishtir())