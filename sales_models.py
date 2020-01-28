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
    new_item_price = input('Enter price of item to add: ')
    phones.append({"id": len(phones)+1, 'name': new_item_name,
                   "model": new_item_model, "price": new_item_price})


def delete_item(phones):
    for_delete = input("Enter a number of your item to delete: ")
    phones.pop(int(for_delete))


def sort_by_price(phones):
    pass


def sell_score(phones):
    print(phones)
    sold = input("Enter a number of item you wont to bye!: ")
    return phones.pop(int(sold))


def sell_statistics(phones):
    pass


def show_items(phones):
    for item in phones:
        print(item["id"], item['name'].join('||'),
              item['model'].join('||'), str(item["price"]).join('[]'))
