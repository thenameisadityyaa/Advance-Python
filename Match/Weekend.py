day=input("Enter the day of the week:").lower()
match day:
    case "sunday":
        print("It is sunday")
    case "monday":
        print("It is monday")
    case "tuesday":
        print("It is tuesday")
    case "wednesday":
        print("It is wednesday")
    case "thursday":
        print("It is thursday")
    case "friday":
        print("It is friday")   
    case "saturday":
        print("It is saturday")                 
    case _:
        print("Invalid day")
