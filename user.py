user_info = {
    }
exit = False


for i in range(1):
    user_name = input("name: ")
    user_info["name"]=user_name
    print(f"{user_info['name']}")

    user_age = int(input("age: "))
    user_info["age"]=user_age
    print(f"{user_info['age']}")

    user_sex = input("sex: ")
    user_info["sex"]=user_sex
    print(f"{user_info['sex']}")

    user_phone = input("phone: ")
    user_info["phone"]=user_phone
    print(f"{user_info['phone']}")

    user_gmail = input("gmail: ")
    user_info["gmail"]=user_gmail
    print(f"{user_info['gmail']}")



