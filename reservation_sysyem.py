# ============================================================
#              GRAND HORIZON HOTEL
#              ROOM BOOKING SYSTEM
# ============================================================

import json
from datetime import datetime


# ============================================================
# HOTEL DETAILS
# ============================================================

hotel_name = "Grand Horizon Hotel"

total_floors = 3
rooms_per_floor = 10


# ============================================================
# ROOM TYPES
# ============================================================

room_types = ("Single", "Family")
ac_types = ("AC", "Non-AC")


# ============================================================
# CREATE ROOMS
# ============================================================

rooms = {}

for floor in range(1, total_floors + 1):

    for room_position in range(1, rooms_per_floor + 1):

        room_number = floor * 100 + room_position

        # First 5 rooms = Single
        # Last 5 rooms = Family

        if room_position <= 5:
            room_type = "Single"
        else:
            room_type = "Family"

        # Even rooms = AC
        # Odd rooms = Non-AC

        if room_position % 2 == 0:
            ac_type = "AC"
        else:
            ac_type = "Non-AC"

        # Room prices

        if room_type == "Single" and ac_type == "AC":
            price = 1500

        elif room_type == "Single" and ac_type == "Non-AC":
            price = 1000

        elif room_type == "Family" and ac_type == "AC":
            price = 2500

        else:
            price = 2000

        rooms[room_number] = {
            "floor": floor,
            "type": room_type,
            "ac": ac_type,
            "price": price,
            "status": "Available"
        }


# ============================================================
# CUSTOMER CLASS
# ============================================================

class Customer:

    def __init__(self, name, phone, age):

        self.name = name
        self.phone = phone
        self.age = age

    def display(self):

        print("\nCustomer Details")
        print("-------------------------")

        print("Name  :", self.name)
        print("Phone :", self.phone)
        print("Age   :", self.age)


# ============================================================
# VIP CUSTOMER
# ============================================================

class VIPCustomer(Customer):

    def __init__(self, name, phone, age):

        super().__init__(
            name,
            phone,
            age
        )

        self.discount = 10


# ============================================================
# DISPLAY ALL ROOMS
# ============================================================

def display_rooms():

    print("\n")
    print("=" * 75)
    print("                    ROOM DETAILS")
    print("=" * 75)

    print(
        f"{'Room':<8}"
        f"{'Floor':<8}"
        f"{'Type':<12}"
        f"{'AC':<12}"
        f"{'Price':<12}"
        f"{'Status':<12}"
    )

    print("-" * 75)

    for room_number, details in rooms.items():

        print(
            f"{room_number:<8}"
            f"{details['floor']:<8}"
            f"{details['type']:<12}"
            f"{details['ac']:<12}"
            f"Rs.{details['price']:<9}"
            f"{details['status']:<12}"
        )


# ============================================================
# SEARCH ROOM
# ============================================================

def search_room():

    print("\n")
    print("=" * 55)
    print("                    SEARCH ROOM")
    print("=" * 55)

    room_type_input = input(
        "Enter room type (Single/Family): "
    ).strip().lower()

    ac_type_input = input(
        "Enter AC type (AC/Non-AC): "
    ).strip().lower()

    # Convert room type correctly

    if room_type_input == "single":

        room_type = "Single"

    elif room_type_input == "family":

        room_type = "Family"

    else:

        print("Please enter Single or Family.")
        return


    # Convert AC type correctly

    if ac_type_input == "ac":

        ac_type = "AC"

    elif ac_type_input in ["non-ac", "non ac", "nonac"]:

        ac_type = "Non-AC"

    else:

        print("Please enter AC or Non-AC.")
        return


    print("\nMatching Rooms")
    print("-------------------------")

    # Search rooms

    for room_number, details in rooms.items():

        if (
            details["type"] == room_type
            and details["ac"] == ac_type
            and details["status"] == "Available"
        ):

            print(
                "Room:",
                room_number,
                "| Floor:",
                details["floor"],
                "| Type:",
                details["type"],
                "|",
                details["ac"],
                "| Price: Rs.",
                details["price"]
            )


# ============================================================
# BOOK ROOM
# ============================================================

def book_room():

    print("\n")
    print("=" * 55)
    print("                     BOOK ROOM")
    print("=" * 55)

    try:

        room_number = int(
            input("Enter room number: ")
        )

        # Check room

        if room_number not in rooms:

            print("Invalid room number.")

            return


        # Check status

        if rooms[room_number]["status"] == "Booked":

            print("This room is already booked.")

            return


        # Room information

        print("\nRoom Information")
        print("-------------------------")

        print(
            "Room Number :",
            room_number
        )

        print(
            "Floor       :",
            rooms[room_number]["floor"]
        )

        print(
            "Room Type   :",
            rooms[room_number]["type"]
        )

        print(
            "AC Type     :",
            rooms[room_number]["ac"]
        )

        print(
            "Price/Day   : Rs.",
            rooms[room_number]["price"]
        )


        # Customer details

        name = input(
            "\nEnter customer name: "
        )

        phone = input(
            "Enter phone number: "
        )

        age = int(
            input("Enter age: ")
        )

        days = int(
            input("Enter number of days: ")
        )


        if days <= 0:

            print("Days must be greater than zero.")

            return


        customer_type = input(
            "Customer type (Normal/VIP): "
        ).strip().lower()


        # Create customer object

        if customer_type == "vip":

            customer = VIPCustomer(
                name,
                phone,
                age
            )

            customer_type = "VIP"

        else:

            customer = Customer(
                name,
                phone,
                age
            )

            customer_type = "Normal"


        # Display customer

        customer.display()


        # Calculate bill

        price = rooms[room_number]["price"]

        subtotal = price * days

        discount = 0


        # VIP discount

        if customer_type == "VIP":

            discount = subtotal * 10 / 100


        total = subtotal - discount


        # Change room status

        rooms[room_number]["status"] = "Booked"


        # Store booking information

        rooms[room_number]["customer"] = {

            "name": name,

            "phone": phone,

            "age": age,

            "days": days,

            "customer_type": customer_type,

            "date": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            ),

            "total": total
        }


        # Booking receipt

        print("\n")
        print("=" * 55)
        print("              BOOKING SUCCESSFUL")
        print("=" * 55)

        print(
            "Customer    :",
            name
        )

        print(
            "Room Number :",
            room_number
        )

        print(
            "Floor       :",
            rooms[room_number]["floor"]
        )

        print(
            "Room Type   :",
            rooms[room_number]["type"]
        )

        print(
            "AC Type     :",
            rooms[room_number]["ac"]
        )

        print(
            "Price/Day   : Rs.",
            price
        )

        print(
            "Days        :",
            days
        )

        print(
            "Subtotal    : Rs.",
            subtotal
        )

        print(
            "Discount    : Rs.",
            discount
        )

        print(
            "Total Bill  : Rs.",
            total
        )

        print(
            "Date        :",
            rooms[room_number]
            ["customer"]
            ["date"]
        )

        print("=" * 55)


    except ValueError:

        print(
            "Please enter valid numbers."
        )


# ============================================================
# CANCEL BOOKING
# ============================================================

def cancel_booking():

    print("\n")
    print("=" * 55)
    print("                  CANCEL BOOKING")
    print("=" * 55)

    try:

        room_number = int(
            input("Enter room number: ")
        )


        if room_number not in rooms:

            print("Invalid room number.")

            return


        if rooms[room_number]["status"] == "Available":

            print(
                "This room is already available."
            )

            return


        customer_name = rooms[
            room_number
        ]["customer"]["name"]


        print(
            "Booking found for:",
            customer_name
        )


        confirmation = input(
            "Do you want to cancel? (yes/no): "
        ).strip().lower()


        if confirmation == "yes":

            rooms[room_number]["status"] = "Available"

            del rooms[room_number]["customer"]

            print(
                "Booking cancelled successfully."
            )

        else:

            print(
                "Booking was not cancelled."
            )


    except ValueError:

        print(
            "Please enter a valid room number."
        )


# ============================================================
# AVAILABLE ROOMS
# ============================================================

def available_rooms():

    print("\n")
    print("=" * 65)
    print("                   AVAILABLE ROOMS")
    print("=" * 65)

    for room_number, details in rooms.items():

        if details["status"] == "Available":

            print(
                "Room:",
                room_number,
                "| Floor:",
                details["floor"],
                "|",
                details["type"],
                "|",
                details["ac"],
                "| Rs.",
                details["price"]
            )


# ============================================================
# BOOKED ROOMS
# ============================================================

def booked_rooms():

    print("\n")
    print("=" * 65)
    print("                     BOOKED ROOMS")
    print("=" * 65)

    for room_number, details in rooms.items():

        if details["status"] == "Booked":

            customer = details["customer"]

            print(
                "Room:",
                room_number,
                "| Customer:",
                customer["name"],
                "| Phone:",
                customer["phone"],
                "| Total: Rs.",
                customer["total"]
            )


# ============================================================
# ROOMS BY FLOOR
# ============================================================

def rooms_by_floor():

    try:

        floor = int(
            input(
                "\nEnter floor number (1-3): "
            )
        )


        if floor < 1 or floor > 3:

            print("Invalid floor number.")

            return


        print("\nFloor", floor)
        print("------------------------")


        for room_number, details in rooms.items():

            if details["floor"] == floor:

                print(
                    "Room:",
                    room_number,
                    "|",
                    details["type"],
                    "|",
                    details["ac"],
                    "| Rs.",
                    details["price"],
                    "|",
                    details["status"]
                )


    except ValueError:

        print(
            "Please enter a valid floor number."
        )


# ============================================================
# SAVE DATA
# ============================================================

def save_data():

    try:

        with open(
            "hotel_data.json",
            "w"
        ) as file:

            json.dump(
                rooms,
                file,
                indent=4
            )


        print(
            "Data saved successfully."
        )


    except Exception as error:

        print(
            "Error:",
            error
        )


# ============================================================
# MAIN MENU
# ============================================================

def menu():

    while True:

        print("\n")
        print("=" * 55)
        print("             GRAND HORIZON HOTEL")
        print("             ROOM BOOKING SYSTEM")
        print("=" * 55)

        print("1. Display All Rooms")
        print("2. Search Room")
        print("3. Book Room")
        print("4. Cancel Booking")
        print("5. Available Rooms")
        print("6. Booked Rooms")
        print("7. Rooms By Floor")
        print("8. Save Data")
        print("9. Exit")

        print("=" * 55)


        choice = input(
            "Enter your choice: "
        ).strip()


        if choice == "1":

            display_rooms()


        elif choice == "2":

            search_room()


        elif choice == "3":

            book_room()


        elif choice == "4":

            cancel_booking()


        elif choice == "5":

            available_rooms()


        elif choice == "6":

            booked_rooms()


        elif choice == "7":

            rooms_by_floor()


        elif choice == "8":

            save_data()


        elif choice == "9":

            print(
                "\nThank you for using "
                "Grand Horizon Hotel!"
            )

            break


        else:

            print(
                "Invalid choice. "
                "Please select 1-9."
            )


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":

    menu()