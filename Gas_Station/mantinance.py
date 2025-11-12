import os



service = ["Motor Check", "Replace Tires", "Add oil to the motor", "Battery recharge", "Brakes check"]

def apply_Man():
    print("We Offer plenty of Mantinance services")
    print(f"""
      
        1- {service[0]}
        2- {service[1]}
        3- {service[2]}
        4- {service[3]} 
        5- {service[4]}
     """)

    ManInput = int(input("What service you are interesting on? please write a number \n"))

    if ManInput == range(1, 5):
        print(f"""
           We will do a {service[ManInput-1]} For Your Car it will cost you
           After Taxes 500 Egp
         """)
    else :
       print("Tha's Not a service provide") 





































