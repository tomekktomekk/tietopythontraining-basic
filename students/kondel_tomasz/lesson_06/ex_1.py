
def displayInventory(dict_stuff):
    print("Inventory:")
    item_total = 0
    for k, v in dict_stuff.items():
        item_total = item_total + v
        print('{k:s} : {v:d}'.format(k=k, v=v))
    print("Total number of items: " + str(item_total))



def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(stuff)


if __name__ == '__main__':
    main()