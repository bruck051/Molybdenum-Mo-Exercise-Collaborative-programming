food_values = {
    "apple": {"hunger": 15, "health": 2},
    "sandwich": {"hunger": 35, "health": 3},
    "soup": {"hunger": 30, "health": 5},
    "ramen": {"hunger": 25, "health": 0},
    "candy": {"hunger": 5, "health": 0}    
}

low_stock_threshold = 2
starving_threshold = 50

def feed_character(character, food, inventory):
    """
    Feeds the character one serving of food from inventory, lowering hunger
    and adjusting health. Hunger and health are on a 0-100 scale.
    
    Args:
        character (dict): stats with "hunger" and "health". updated in place.
        food (str): name of the food to eat. 
        inventory (list[dict]): items shown like {"item":str, "quantity": int}
        
    Returns:
        updated_inventory (list[dict]): inventory with one serving removed.
        warnings (str); messages for the player, i.e. "you don't have any 
        more soup"
        
        Raises:
            ValueError: If food is not known food.  
    """
    
    if food not in food_values:
        raise ValueError(f"Unkown food:{food!r}")
    
    warnings = []
    updated_inventory = []
    found = False
    ate = False
    
    for stack in inventory:
        new_stack = dict(stack)
        if new_stack["item"] == food and not found:
            found = True
            if new_stack["quantity"] > 0:
                new_stack["quantity"] -= 1
                ate = True
                if new_stack["quantity"] == 0:
                    warnings.append(f"You ran out of {food}!")
                elif new_stack["quantity"] <= low_stock_threshold:
                    warnings.append(
                        f"You're running low on {food} "
                        f"({new_stack['quantity']} left).")
        
            if new_stack["quantity"] > 0:
                updated_inventory.append(new_stack)
        
        if not found or not ate:
            warnings.append(f"You don't have any {food}!")
            return updated_inventory, " ".join(warnings)
        
        effects = food_values[food]
        was_starving = character["hunger"] >= starving_threshold
        character["hunger"] = max(0, character["hunger"] - effects["hunger"])
        health_change = effects["health"]
        if was_starving:
            health_change -= 3
            character["health"] = max(0, min(100, character["health"] + health_change))
            
            
        if character["hunger"] >= 50:
            warnings.append("You are still hungry.")
        elif character["hunger"] == 0:
            warnings.append("You are completely full.")

        return updated_inventory, " ".join(warnings)
    
if __name__ == "__main__":
    jamie = {"hunger": 85, "health": 70}
    pantry = [
        {"item": "apple", "quantity": 3},
        {"item": "soup", "quantity": 1},
        {"item": "water", "quantity": 4},
    ]
            
    result = feed_character(jamie, "soup", pantry)
    pantry = result[0]
    msg = result[1]
    print(jamie, pantry, repr(msg))

    result = feed_character(jamie, "soup", pantry)  # none left
    pantry = result[0]
    msg = result[1]
    print(jamie, pantry, repr(msg))