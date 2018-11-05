# Inventories will be defined below
import Player


class Inventory:

    size = 30
    items = []

    @staticmethod
    def add_item(item):
        if len(Inventory.items) < Inventory.size:
            Inventory.items.append(item)
        else:
            print('Inventory full')

    def remove_item(self, item):
        if Inventory.items[Inventory.items.index(item)]:
            print('Removed ' + item.name + ' from inventory')
            Inventory.items[Inventory.items.index(item)] = None
        else:
            print('No such item found in inventory')

    def __str__(self):
        out = '\t'
        for item in Inventory.items:
            out += '\t' + item.name + ' '
        return out


class Backpack(Inventory):

    size = 6
    items_in = 0
    items = []

    @staticmethod
    def add_item(source_inventory):
        for item in source_inventory.items:
            if item.to_backpack:
                if Backpack.items_in < Backpack.size:
                    # source_inventory.remove_item(item)
                    Backpack.items.append(item)
                    print('Added ' + item.name + ' to backpack successfully')
                    Backpack.items_in += 1
                else:
                    print('Attempted to add '
                          + item.name +
                          ' to backpack but the backpack is full')

    @staticmethod
    def switch_item(item_to_remove, item_to_add):

        if not item_to_add:
            Backpack.items_in -= 1

        index = Backpack.items.index(item_to_remove)
        Player.Player.weaponEquipped = item_to_remove
        Backpack.items[index] = item_to_add

    def empty_backpack(self, source_inventory):
        for item in self.items:
            # source_inventory.add_item(item)
            self.remove_item(item)
        self.items_in = 0
        print('Emptied the backpack')
