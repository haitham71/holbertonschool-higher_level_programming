class Food: # Base class

    def __init__(self, name, price):

        self.name = name

        self.price = price
        
        print(f"{self.name} is created from base class")

    def eat (self):
        
        print("eat Metohd from main class")



class Apple(Food): #Derived class

    def __init__(self, name, price):

        # Food.__init__(self, name) # Creat Inctance from base class

        super().__init__(name, price)
        

        print(f"{self.name} is created from Derived class And price is {self.price}")

    def get(self):

        print(f"food from tree from deriver {self.price}")


# food_one = Food("Pizza")
food_tow = Apple("Pizza", 130)
food_tow.eat()
food_tow.get()