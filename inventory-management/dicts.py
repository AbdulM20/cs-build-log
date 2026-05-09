"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inventory = {} # Create an empty dictionary
    for item in items: # Create a conditional in which:
        if item in inventory:
            inventory[item] += 1 # if item is in dictionary increment the item by 1
        else:
            inventory[item] = 1 # else let the item be added as 1
    return inventory # return the dictionary



def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    # Same loop as previous function copy - pasted in, only difference is :
    # Doesn't begin with an empty Dictionary but rather calls the already created one
    for item in items: # Create a conditional in which:
        if item in inventory:
            inventory[item] += 1 # if item is in dictionary increment the item by 1
        else:
            inventory[item] = 1 # else let the item be added as 1
    return inventory # return the dictionary



def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    # The docstring mentions decrementing using elements from the items list
    # check if the key exists in the dictionary
    # The count of an item needs to be greater than 0
    # if it is greater than 0 then for each item in items
    # Decrement the count by -1

    # return the inventory

    for item in items:
        if item in inventory:
            if inventory[item] > 0:
                inventory[item] -= 1
    return inventory




def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    # check if item exists in the dictionary
    # remove from dictionary if it does

    if item in inventory:
        del inventory[item]
    return inventory




def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    # create an empty list for available items
    # for each key, value in inventory.items()
    # if the value of the key is greater than 0
    # append the empty list with the key and value
    # then return the empty list
    available_items = []
    for key, value in inventory.items():
        if value > 0:
            available_items.append((key, value))
    return available_items