from sales_models import show_items, add_item, delete_item, sort_by_price, sell_score, sell_statistics
phones = [{"id": 2, 'name': "Iphone", "model": '11pro', "price": 27000},
          {"id": 1, 'name': "Samsung", "model": 's9', "price": 7000},
          {"id": 5, 'name': "Meizu", "model": 'me8', "price": 11000},
          {"id": 4, 'name': "OnePlus", "model": 'plus+', "price": 13000},
          {"id": 3, 'name': "Motorola", "model": 'Razer', "price": 700}]

soled = []
while True:
    print("\t\t\tHello Guest\nChoose what to do: \n1: Add item:\n2: Delete Item:\n3: Sort by price:\n4: Look sell scroes:\n5: Look sell statistics: \n6: Show items we have\n 0: Exit: ")
    inputed = input()
    if inputed == "0":
        print("Bye bye")
        break
    elif inputed == "1":
        add_item(phones)
        show_items(phones)
        input("Enter to continue")

    elif inputed == "2":
        delete_item(phones)
        show_items(phones)
    elif inputed == "3":
        phones = sort_by_price(phones)
        
        show_items(phones)
    elif inputed == "4":
        soled.append(sell_score(phones))
        show_items(phones)
        print(soled)
    elif inputed == "5":
        sell_statistics(len(soled))
        show_items(phones)
    elif inputed == "6":
        show_items(phones)
