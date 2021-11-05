age_year = int(input("Enter your age or date of year:\n"))
current_year = int(input("Enter your current year:\n"))

if len(str(age_year)) == 2 and age_year > 150:
    print("You are oldest living being in the world")
    exit()
elif age_year > current_year:
    print("You are not born yet")
    exit()

if len(str(age_year)) == 4:
    if len(str(age_year)) > 2021:
        print("You are from future")
        exit()
    age_year = age_year + 100
    print(f"you will die in {age_year}")
elif len(str(age_year)) == 2:
    if len(str(age_year)) > 100:
        print("You are oldest person in the world")
        exit()
    age_year2 = 100 - age_year
    print(f"You have only {age_year2} years left")
    age_year_left = age_year2 + 2021
    print(f"you will die in {age_year_left}")


add_option = input("do you know what will be your age in which year? y/n: ")
if add_option == "y":
    age_will_year = int(input("Enter you age: "))
    age_in_year = int(input("Enter the year in which you want to know age: "))
    will_know_age = age_in_year - 2021
    real_age = age_will_year + will_know_age
    print(real_age)
else:
    exit()
