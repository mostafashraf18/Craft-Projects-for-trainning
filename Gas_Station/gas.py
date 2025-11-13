import random
import os
import mantinance


OCT95 = 21
OCT90 = 19.25
OCT80 = 17.75

def get_gas_type():
    
    while True:
         print("Welcome to WEEEEEE Gas Station")
         print("""
            95-Octane Gasoline: EGP 21.00 per liter
            92-Octane Gasoline: EGP 19.25 per liter
            80-Octane Gasoline: EGP 17.75 per liter
            
            1- Mantinace service
            2- Washing Room
            """)
         user_input = int(input("what's the type of gas? please selcet number"))
         much = int(input("How much liters You need? please type a number"))
         if user_input == 95:
              price = much * OCT95
              print(f"Your Have To pay {price}")
         elif user_input == 90:
              price = much * OCT90
              print(f"Your Have to pay {price}")
         elif user_input == 80:
              price = much * OCT80
              print(f"Your Have to pay {price}")
         elif user_input == 1:
              apply_Man() #add Feature
         else:
              print("that's not A type")

    
    


get_gas_type()
