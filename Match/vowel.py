vowel=input("Enter a character: ").lower()
match vowel:
    case "a | e | i | o | u":
        print(f"{vowel} is a vowel")
    case _:
        print(f"{vowel} is not a vowel")    