# Inventories will be defined below


class Inventory:

    size = 30

    def __init__(self):
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.size:
            self.items.append(item)
        else:
            print('Inventory full')

    def remove_item(self, item):
        if self.items[self.items.index(item)]:
            print('Removed ' + item.name + ' from inventory')
            self.items[self.items.index(item)] = None
        else:
            print('No such item found in inventory')

    def __str__(self):
        out = '\t'
        for item in self.items:
            out += '\t' + item.name + ' '
        return out


class Backpack(Inventory):

    size = 6
    items_in = 0

    def __init__(self):
        Inventory.__init__(self)

    def add_item(self, source_inventory):
        for item in source_inventory.items:
            if item.to_backpack:
                if self.items_in < self.size:
                    # source_inventory.remove_item(item)
                    self.items.append(item)
                    print('Added ' + item.name + ' to backpack successfully')
                    self.items_in += 1
                else:
                    print('Attempted to add '
                          + item.name +
                          ' to backpack but the backpack is full')

    def empty_backpack(self, source_inventory):
        for item in self.items:
            # source_inventory.add_item(item)
            self.remove_item(item)
        self.items_in = 0
        print('Emptied the backpack')
