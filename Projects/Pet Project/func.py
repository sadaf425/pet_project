from plyer import notification
import datetime
pets=[]

def add_pet():
    pet_name=input("Enter Pet Name: ")
    for pet in pets:
        if pet["name"].lower() == pet_name.lower():
            print("This pet already exists!")
            return
    pet_age=input("Enter Pet Age: ")
    pet_type=input("Enter Pet Type: ")
    pet_vaccination=input("Vaccinated? (Yes/No): ")

    pet_info={
        "name":pet_name,
        "age":pet_age,
        "type":pet_type,
        "vaccinated":pet_vaccination,
        "feed":"No",
        "added_time":datetime.datetime.now()


    }
    pets.append(pet_info)
    print("Pet added successfully!")

def view_pets():
    print("\n\tAll Pets")

    if len(pets) == 0:
        print("No pets found!")
    else:
        for pet in pets:
            print("Name:", pet["name"])
            print("Age:", pet["age"])
            print("Type:", pet["type"])
            print("Added Time:", pet["added_time"])
            print("\n")


def delete_pets():
    name = input("Enter Pet Name to delete: ")

    for pet in pets:
        if pet["name"] == name:
            pets.remove(pet)
            print("Pet deleted!")
            return

    print("Pet not found!")

def check_vaccination():
    name = input("Enter Pet Name: ")

    for pet in pets:
        if pet["name"] == name:
            print("Vaccination Status:", pet["vaccinated"])
            return

    print("Pet not found!")


def pet_feed():
    name=input("enter pet name to feed: ")
    for pet in pets:
        if pet["name"]==name:
            pet["feed"]= "yes"
            notification.notify(
                title="Pet Care System",
                message=f"{name} has been fed!",
                timeout=1
            )

            print(f"🍖 {name} is now happy and fed!")
            return

    print("Pet not found!")


    

