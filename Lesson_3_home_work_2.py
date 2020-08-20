def user_info(name=input("Enter your name: "),
              surename=input("Enter your surename: "),
              age=input("Enter your year of birth: "),
              email=input("Enter your year of email: "),
              phone=input("Enter your year of phone number: ")):
    return " ".join([name, surename, age, email, phone])

print(user_info())
