import random

# Mock classes to run function on
class Player:
    """
    Stores information about the player.
    """
    def __init__(self):
        self.health = 100
        self.health_points = 0
        self.energy_points = 0
        self.level = 1
        self.inventory = []

class Cat:
    """
    Stores information about the cat.
    """
    def __init__(self):
        self.mood = 75
        self.friendship_points = 0
        self.trust_level = 1

class Plant:
    """
    Stores information about the plant.
    """
    def __init__(self):
        self.health = 100
        self.condition = "healthy"
        self.growth_points = 0
        self.growth_stage = 1

class Environment:
    """
    Stores environmental conditions.
    """
    def __init__(self):
        self.day = 1
        self.weather = "sunny"

# Main function
def weighted_random_event(player, cat, plant, environment):
    """
    Generate a context-dependent random event using a structured selection process.

    The function evaluates the current game state—including player traits, cat
    behavior, plant condition, and environmental factors—to construct a weighted
    set of possible events. It then adjusts event weights, generates a random
    threshold, and selects the first event whose cumulative weight exceeds that
    threshold.

    Selected events may influence player progression, cat friendship,
    plant growth, inventory contents, and health values.

    Args:
        player (Player): Stores player-related information.
        cat (Cat): Stores cat-related information.
        plant (Plant): Stores plant-related information.
        environment (Environment): Stores environmental information.

    Returns:
        str: Description of the event that occurred.
    """

    events = {
        "cat_finds_item": 15,
        "plant_growth_spurt": 15,
        "rainy_day_gloom": 10,
        "sunny_energy_boost": 10,
        "cat_knocks_over_plant": 5,
        "peaceful_day": 20
    }

    # Adjust event weights
    if player.health < 50:
        events["peaceful_day"] += 10

    if cat.mood > 70:
        events["cat_finds_item"] += 10

    if plant.condition == "healthy":
        events["plant_growth_spurt"] += 10

    if plant.condition == "wilted":
        events["cat_knocks_over_plant"] += 10

    if environment.weather == "sunny":
        events["sunny_energy_boost"] += 15

    elif environment.weather == "rainy":
        events["rainy_day_gloom"] += 15

    # Calculate total weight
    total_weight = 0

    for weight in events.values():
        total_weight += weight

    # Generate random threshold
    threshold = random.randint(1, total_weight)

    # Select weighted event
        # (None of these events are set in stone-
        # theyre moreso just ideas we've had)
    cumulative_weight = 0
    selected_event = None

    for event, weight in events.items():
        cumulative_weight += weight

        if threshold <= cumulative_weight:
            selected_event = event
            break

    # Apply selected event
    if selected_event == "cat_finds_item":

        friendship_gain = random.randint(5, 15)

        cat.friendship_points += friendship_gain

        while cat.friendship_points >= 50:
            cat.trust_level += 1
            cat.friendship_points -= 50

        player.inventory.append("Mysterious Trinket")

        return (
            f"Cat found a Mysterious Trinket! "
            f"+{friendship_gain} friendship points. "
            f"Trust Level: {cat.trust_level}"
        )

    elif selected_event == "plant_growth_spurt":

        growth_gain = random.randint(5, 15)

        plant.growth_points += growth_gain

        while plant.growth_points >= 30:
            plant.growth_stage += 1
            plant.growth_points -= 30

        return (
            f"Plant gained {growth_gain} growth points. "
            f"Growth Stage: {plant.growth_stage}"
        )

    elif selected_event == "rainy_day_gloom":

        player.energy_points = max(0, player.energy_points - 5)

        return (
            "Rainy weather reduced player energy by 5 points."
        )

    elif selected_event == "sunny_energy_boost":

        energy_gain = random.randint(10, 20)

        player.energy_points += energy_gain

        while player.energy_points >= 100:
            player.level += 1
            player.energy_points -= 100

        return (
            f"Player gained {energy_gain} energy points. "
            f"Level: {player.level}"
        )

    elif selected_event == "cat_knocks_over_plant":

        plant.health -= 10

        if plant.health < 50:
            plant.condition = "wilted"

        return (
            f"Cat knocked over the plant. "
            f"Plant health is now {plant.health}."
        )

    else:

        player.health_points += 5

        while player.health_points >= 50:
            player.health += 10
            player.health_points -= 50

        return (
            "Peaceful day. "
            "+5 health points earned."
        )

# Test runs for code
if __name__ == "__main__":

    player = Player()
    cat = Cat()
    plant = Plant()
    environment = Environment()

    weather_options = ["sunny", "rainy"]

    while True:

        print(f"\n===== DAY {environment.day} =====")

        # New weather each day
        environment.weather = random.choice(weather_options)

        print(f"Weather: {environment.weather}")

        event_result = weighted_random_event(
            player,
            cat,
            plant,
            environment
        )

        print("\nEVENT")
        print(event_result)

        print("\nPLAYER")
        print(f"Level: {player.level}")
        print(f"Health: {player.health}")
        print(f"Health Points: {player.health_points}")
        print(f"Energy Points: {player.energy_points}")

        print("\nCAT")
        print(f"Trust Level: {cat.trust_level}")
        print(f"Friendship Points: {cat.friendship_points}")

        print("\nPLANT")
        print(f"Growth Stage: {plant.growth_stage}")
        print(f"Growth Points: {plant.growth_points}")
        print(f"Health: {plant.health}")
        print(f"Condition: {plant.condition}")

        print("\nINVENTORY")
        print(player.inventory)

        choice = input(
            "\nPress ENTER to advance to the next day or type 'quit': "
        )

        if choice.lower() == "quit":
            break

        environment.day += 1

    print("\n=== FINAL GAME STATE ===")

    print(f"Days Survived: {environment.day}")
    print(f"Player Level: {player.level}")
    print(f"Cat Trust Level: {cat.trust_level}")
    print(f"Plant Growth Stage: {plant.growth_stage}")
    print(f"Inventory: {player.inventory}")
    print("Final Inventory:")
    print(player.inventory)