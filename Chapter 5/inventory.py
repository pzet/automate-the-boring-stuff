def displayInventory(inventory):
    print("Your inventory:")
    item_total = 0

    for k, v in inventory.items():
        print('{} {}'.format(v, k))
        item_total += v

    print('Total number of items: {}'.format(item_total))

def addInventory(loot_list):
    for item in loot_list:
        if item in inv.keys():
            inv[item] += 1
        else:
            inv[item] = 1

stuff = {'rope': 1,
        'torch': 6,
        'gold coin': 42,
        'dagger': 1,
        'arrow': 12}

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(stuff)
addInventory(dragonLoot)
displayInventory(inv)
