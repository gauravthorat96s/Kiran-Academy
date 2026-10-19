import random


while True:
    print("\n==== CAB BOOKING ====")

    print("1: Book Ride")
    print("2: Exit")

    choise=input("Enter Your Choise: ")

    if choise == "1":
        print("\n1. Auto -Rs.12/km")
        print("2. Sedan -Rs.18/km")
        print("3. SUV -Rs.15/km")

        cab =input("choise cab: ")

        if cab=="1":
            cab_name="Auto"
            rate=12

        elif cab=="2":
            cab_name="Sedan"
            rate=18

        elif cab=="3":
            cab_name="SUV"
            rate=25

        else:
            print("Invalid cab choise !!")

        print("\n1. Pune to Shivajinagar -5km")
        print("2. Swarget ti Kothrud -8km")
        print("3. Hinjawadi to Wakad -10km")


        rout=input("Choose Route: ")

        if rout=="1":
            source="Pune"
            destination="Shivajinagar"
            distance=5

        elif rout=="2":
            source="Swarget"
            destination="Kothrud"
            distance=8

        elif rout=="3":
            source="Hinjawadi"
            destination="Wakad"
            diistance=10

        else:
            print("Choose Correct route")


        fare =distance*rate

        print("\n==== RIDE DETAILS ====")

        
        print("Cab :",cab_name)
        print("1. Source: ",source)
        print("2. Destination: ",destination)
        print("3. Distance: ",distance)
        print("Rate Rs:",rate)

        print("\n1. Confirm & Share OTP")
        print("2. Cancle Ride")

        confirm=input("Enter your choise: ")

        if confirm =="1":
            otp=random.randint(1000,9999)
            print("Booking Confirmd !!")
            print("Your OTP is: ",otp)
            print("Ride is loked now!")
            print("Cancellation is not allowed..")

        elif confirm=="2":
            print("Ride Cancle Successfully !")

        else:
            print("Invalid choise")

    elif choise=="2":
        print("Thank You for using cab booking chat bot !")
        break

    else:
        print("Invalid Choise! Please try again.")
            