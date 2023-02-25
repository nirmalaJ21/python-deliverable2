fruit_options = ["Apple", "Grape", "Orange"]
fruit_price = [2, 1, 3]
fruit_type = []
Apple_Count = 0
Grapes_Count= 0
Orange_Count = 0
option = "False"
SubTotal = 0

print(f"Welcome to Nirmala fruit Market!")
name = input(f"What is your name?")


while option == "False":
    print(f"Welcome {name} which fruit would like to buy ?")
    print(f"1.) {fruit_options[0]} {fruit_price[0]} $")
    print(f"2.) {fruit_options[1]} {fruit_price[1]} $")
    print(f"3.) {fruit_options[2]} {fruit_price[2]} $")
    type = input(f"Which type of fruit you want")

    if type == "1":  # For Apple
        Apple_Count = Apple_Count + 1
        SubTotal = SubTotal + 2
        if (Apple_Count > 1):
           Total_Count_Price= Apple_Count * 2
           print(f"you bought{Apple_Count} apple at {Total_Count_Price=} $")
        else:
            print(f"you bought {Apple_Count} apple at {fruit_price[0]} $")

    elif type == "2":  # For Grapes
        SubTotal = SubTotal + 1
        Grapes_Count = Grapes_Count + 1
        if (Grapes_Count > 1):
            Total_Count_Price == Grapes_Count * 1
            print(f"you bought{Grapes_Count} Grapes at {Total_Count_Price=} $")
        else:
            print(f"you bought{Grapes_Count} Grapes at {fruit_price[1]} $")

    else:  # For Orange
        SubTotal = SubTotal + 3;
        Orange_Count = Orange_Count + 1
        if (Orange_Count  > 1):
            Total_Count_Price == Orange_Count * 3
            print(f"you bought,{Orange_Count } Oranges at {Total_Count_Price=} $")
        else:
            print(f"you bought,{Orange_Count } Oranges at {fruit_price[2]} $")

    more = input(f"Would like to  buy more y/n")

    if more == "n":
         print(f"Order for {name}")
         print(f"{Apple_Count} apple(s) at $2 apiece")
         print(f"{Grapes_Count} grape(s) at $1 apiece")
         print(f"{Orange_Count } orange(s) at $3 apiece")
         print(f"Sub Total: ${SubTotal}")

         ## Calculate Tax

         Tax = (5* SubTotal)/100
         Total = SubTotal + Tax;
         print(f"Tax: ${Tax}")
         print(f"Total: ${Total}")
         option = "True"
