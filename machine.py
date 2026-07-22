def book_room(bookings):
    Room_number = int(input("enter the room number"))
    bookings ={}
    if Room_number in bookings:
        return "room number already booked"
    else:
        guest_name = input("enter your name :")
        Room_type = input("enter type of room(Delux/standard/suite) :") 
        Number_of_days = int(input("enter the number of days :"))
        Total_price = int(input("enter the total price :"))
        bookings[Room_number] = {"Room number": Room_number,
                                  "guest name" : guest_name,
                                  "room type": Room_type,
                                  "number of days": Number_of_days,
                                  "total price" :Total_price}
        print("room booked successfully")
def view_bookings(bookings):
    if len(bookings) == 0:
        print("No booking records found")
    else:
        for Room_number,details in bookings.item():
            print("booking details : ")
            print("Room number : " ,details[Room_number])
            print("guest name : " ,guest_name)
            print("room type : " ,Room_type)
            print("number of days : " , Number_of_days)
            print("total price : " , Total_price)
def search_booking(bookings):
    Room_number = int(input("enter the room number"))
    if Room_number in bookings:
        print("booking details : ")
        print("Room number : " ,Room_number)
        print("guest name : " ,guest_name)
        print("room type : " ,Room_type)
        print("number of days : " , Number_of_days)
        print("total price : " , Total_price)
    else:
        print("booking not found")
def update_days(bookings):
    Room_number = int(input("enter the room number"))
    if Room_number in bookings:
        days = int(input("enter new number of days : "))
        if days > 0:
            bookings[Room_number][Number_of_days] = days
            print("Booking days updated successfully")
        else:
            print("enter correct no of days")
    else:
        print("booking not found")

def cancel_booking(bookings):
    Room_number = int(input("enter the room number"))
    if Room_number in bookings:
        del bookings[Room_number]
        print("Booking cancelled successfully")
    else:
        print("Booking not found")
while True:
    print("HOTEL ROOM BOOKING SYSTEM")
    print("1 . Book room ")
    print("2. View all bookings ")
    print("3. search booking ")
    print("4. update booking days")
    print("5. cancel booking")
    print("Exit")

    choice =int(input("enter your choice : "))
    if choice == 1:
        book_room(bookings)
    elif choice == 2:
        view_bookings(bookings)
    elif choice == 3:
        search_booking(bookings)
    elif choice == 4:
        update_days(bookings)
    elif choice == 5:
        cancel_booking(bookings)
    elif choice == 6:
        print("Thankyou")
        break
    else:
        print("invalid choice")



    
