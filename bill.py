import copy

bill_dict = {
}

def command_panel():
    print("""
añadir factura: 1
pagar facura: 2
ver facturas: 3
salir: 4
    """)

exit = False
user_choice = 0

def add_invoice():
    bill_name = input("bill name: ")
    bill_cost = int(input("bill cost: "))
    bill_dict[bill_name]=bill_cost

def pay_bill():
    bill_name = input("bill name: ")
    bill_cost = int(input("bill cost: "))
    for i, j in bill_dict.items():
        if i == bill_name:
            payment = bill_dict[i] - bill_cost
            bill_dict[i]=payment
            print(bill_dict[i])
            bill_dict_copy = copy.copy(bill_dict)
            if bill_dict_copy[i] == 0:
                bill_dict_copy.pop(i)
        else:
            print("bill not found")

def show_dict():
    for i, j in bill_dict_copy.items():
        print(f"""    
| {i} | {j} |
        """)


while not exit:
    command_panel()
    bill_dict_copy = copy.copy(bill_dict)
    user_choice = int(input("accion: "))
    if user_choice == 1:
        add_invoice()
    elif user_choice == 2:
        pay_bill()
    elif user_choice == 3:
        show_dict()

    elif user_choice == 4:
        print("thanks")
        break
    
