if __name__ == "__main__":
    add_item()
    delete_item()
    sort_by_price()
    sell_score()
    sell_statistics()
    show_items()


def add_item(phones):
    new_item_name = input('Enter name of item to add: ')
    new_item_model = input('Enter model of item to add: ')
    new_item_price = int(input('Enter price of item to add: '))
    phones.append({"id": len(phones)+1, 'name': new_item_name,
                   "model": new_item_model, "price": new_item_price})


def delete_item(phones):
    for_delete = input("Enter a number of your item to delete: ")
    phones.pop(int(for_delete))
    input("Enter to continue")



def sort_by_price(phones):
    sort_by = int(input("Enter sort by:\nID : 1\nPrice : 2\nName : 3\n=>: "))
    if sort_by == 1:
        sort_by = "id"
    elif sort_by == 2:
        sort_by = "price"
    else:
        sort_by = "name"
    
    sorted_items = sorted(phones, key=lambda item: item[sort_by])
    print(sorted_items)
    input()
    return sorted_items
    

def sell_score(phones):
    print(phones)
    sold = input("Enter a number of item you wont to bye!: ")
    for item in phones:
        return item["id"].pop(int(sold))


def sell_statistics(soled):
    print("[", soled, "]-- Items was sold")
    input("Enter to continue")


def show_items(phones):
    for item in phones:
        print(item["id"], item['name'].join('||'),
              item['model'].join('||'), str(item["price"]).join('[]'))
