class LowInventoryError(Exception):
    """Raised when there isn't enough of an item to use."""
    pass


def low_stock_amt():
    """
    Mock function. The real game would search in a file what is considered low
    stock of an item but this is to just test update inventory.

    Returns:
        int: quantity greater than or equal to what counts as running low.
    """
    return 2


def update_inventory(inventory, item, quantity, entity, action):
    """
    An inventory class responsible for tracking the items you have in the
    house. This will be complex because it will involve inheritance and be
    connected to our character, cat, and plant classes. The inventory is also
    always changing depending on the actions of the character so there will be
    meaningful side effects.

    Args:
        item (str): type of item in inventory.
        quantity (int): number of an item in inventory.
        entity (str): identifies if the inventory is for the character, plant,
        or cats.
        inventory(list[dict]): list of items available for character.

    Returns:
        updated_inventory: updated/new version of list items available for
        your character.
        warnings (str): flagging for the user that their running low or ran out
        of certain items.

    Raises:
        LowInventoryError: not enough of a certain item available for  use.
    """
    low_stock_amt = list(inventory)
    warnings = ""
    found = False

    for entry in low_stock_amt:
        if entry["item"] == item and entry["entity"] == entity:
            found = True

            if action == "use":
                if quantity > entry["quantity"]:
                    raise LowInventoryError(
                        f"Not enough {item} to {action} for {entity}."
                    )
                entry["quantity"] -= quantity
            elif action == "add":
                entry["quantity"] += quantity

            # meaningful side effect per entity type
            if entry["quantity"] == 0:
                warnings = f"{entity} is out of {item}!"
            elif entry["quantity"] <= low_stock_amt():
                warnings = f"{entity} is running low on {item}."

    if not found and action == "add":
        low_stock_amt.append({"item": item, "quantity": quantity, 
                              "entity": entity})
    elif not found and action == "use":
        raise LowInventoryError(f"{entity} has no {item} to use.")

    return low_stock_amt, warnings


if __name__ == "__main__":
    # fake data standing in for the real game's starting inventory
    inventory = [
        {"item": "cat food", "quantity": 4, "entity": "cat"},
        {"item": "water", "quantity": 3, "entity": "plant"},
    ]

    # feed the cat
    inventory, warnings = update_inventory(inventory, "cat food", 3, "cat", 
                                           "use")
    print(inventory, "|", warnings)

    # water the plant down to empty
    inventory, warnings = update_inventory(inventory, "water", 3, "plant", 
                                           "use")
    print(inventory, "|", warnings)

    # triggers an error: nothing left to water with
    try:
        update_inventory(inventory, "water", 1, "plant", "use")
    except LowInventoryError as e:
        print("Caught expected error:", e)
