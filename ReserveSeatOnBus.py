Fname = input("Enter your first name: ")
Lname = input("Enter your last name: ")
Id = int(input("Enter your Id number: "))
phone_num = int(input("Enter your phone number: "))
print("Welcome,,,",Fname,Lname,",Id =",Id,",phone_num =",phone_num)
print("Choose number of these buses:")
print("1: From Rafa to KhanYounes , 2: From KhanYounes to Dair AlBalah , 3: From Gaza to Bethanon")
Bus = int(input("Number of Your Bus Is :"))
if Bus==1:
    print("This is the list of seats in your bus:")
    user= print("1 : 'reserved seat' , 2 : 'reserved seat' , 3 : 'empty' , 4 : 'empty' , 5 : 'empty' " )
    seat_num = int(input("Choose Your seat number:"))
    if seat_num == 1 or seat_num == 2:
        print("Sorry, this seat is taken,try again..")
    elif seat_num == 3 or seat_num== 4 or seat_num== 5:
        print(Fname, Lname, ",Id =", Id, ",phone_num =", phone_num,
              ",Your reservation has been successful, Your bus number is", Bus, "and your seat number", seat_num)
    else :
        print("There's no onther seats")
elif Bus==2:
    print("This is the list of seats in your bus:")
    print("1 : 'reserved seat' , 2 : 'empty' , 3 : 'empty' , 4 : 'empty' , 5 : 'reserved seat' ")
    seat_num = int(input("Choose Your seat number:"))
    if seat_num == 1 or seat_num == 5:
        print("Sorry, this seat is taken,try again..")
    elif seat_num == 2 or seat_num== 3 or seat_num== 4:
        print(Fname, Lname, ",Id =", Id, ",phone_num =", phone_num,
              ",Your reservation has been successful, Your bus number is", Bus, "and your seat number", seat_num)
    else:
        print("There's no onther seats")
elif Bus==3:
    print("This is the list of seats in your bus:")
    print("1 : 'reserved seat' , 2 : 'empty' , 3 : 'reserved seat' , 4 : 'empty' , 5 : 'reserved seat' ")
    seat_num = int(input("Choose Your seat number:"))
    if seat_num == 1 or seat_num== 3 or seat_num == 5:
        print("Sorry, this seat is taken,try again..")
    elif seat_num == 2 or seat_num== 4:
        print(Fname, Lname, ",Id =", Id, ",phone_num =", phone_num,
              ",Your reservation has been successful, Your bus number is", Bus, "and your seat number", seat_num)
    else:
        print("There's no onther seats")
else :
    print("The Bus is not available")