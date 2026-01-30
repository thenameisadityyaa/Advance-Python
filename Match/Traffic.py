signal=input("Enter the traffic signal color:").lower()
match signal:
    case "red":
        print("Stop")
    case "yellow"| "orange":
        print("Get Ready for go!!")   
    case "green":
        print("Go")
    case _:
        print("Invalid Signal Color")        