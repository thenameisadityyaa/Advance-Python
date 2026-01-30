days=input("Enter the day of the week:").lower()
match days:
    case "1":
        print("It is monday")
    case "2":
        print("It is tuesday")
    case "3":
        print("It is wednesday")
    case "4":
        print("It is thursday")
    case "5":
        print("It is friday")
    case "6":
        print("It is saturday")
    case "7":
        print("It is sunday")
    case _:
        print("Invalid day")                            