#Function of the store title
def display_store_name():
    print("Spacecraft Rental")
# Spacecraft Selection Details
spacecrafts = {
    "Rocket Lab Photon": {"price": 10000, "available": 1},
    "SpaceX Falcon 9": {"price": 5000, "available": 2},
    "Blue Origin New Shepard": {"price": 8000, "available": 3}
    }
while True:
    display_Spacecraft_store

    print("Welcome to Spacecraft Rental!")
    print("The available spacecraft for hire are as follows:")

    # Filter available spacecraft
    available_spacecrafts ={Key: valitation for key, validation in spacecrafts.items() if value["available"] >0} 

    # Display available spacecraft 
    for index, spacecraft in enumerate(available_spacecrafts, start=1):
      print(f"{index}. {spacecraft} - ${available_spacecrafts[spacecraft]['price']} - Available: {available_spacecrafts[spacecraft]['available']}") 

    
# User# User Selects spacecraft '
user_selection +""
while True:

     user_selection = input("Please select a spacecraft(1,2 or 3):")

     if user_selection.isdigit():
         user_selection = int(user_selection) - 1
         if 0<=user_selection <len(available_spacecrafts):
            selected_spacecraft=list(available_spacecrafts.keys())[user_selection]
            break
         else:
           print("Invalid Entry. Please select correct spacecraft.")
     else:
           print("Invalid Entry. please select 1,2, or 3.")

spacecrafts[selected_spacecraft]["available"] -= 1
                                                 

    # Gather rental details
hire_period = int(input("Enter the hire period in days: "))
requires_pilot = input("Do you require a pilot (yes/no)? ")
requires_pilot = 'yes' if requires_pilot == 'yes' else 'no'
passengers = int(input("Enter the number of passengers: ")) 

    #Calculate the total cost
daily_rate = spacecrafts[selected_spacecraft]["price"]
pilot_cost = 500 if requires_pilot =='yes' else 0
passenger_cost = passengers *500
total_cost = (hire_period * daily_rate) + pilot_cost + passenger_cost

    # Display rental
print("Rental Summary")
print(f"spacecraft Model:{selected_spacecraft}")
print("hire Period:{hire_period} days")
print("Pilot Required:{requires_pilot}")
print("Number of Passengers:{passengers}")
print("Total Hire Charge:${total_cost}")

    #Ask if the user wants to restart the Spacecraft selection process
restart_choice = input("Would you like to start over(yes/no)")
if restart_choice =='no':
    print("Thank you for using Spacecrafts Rentals!")
break
                                    


            
        
