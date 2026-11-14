def determine_cat_behavior(cat_status, environment, recent_behaviors=None):
    """
    This determines the cat's behavior based on its current enviroment, needs
    and behaviors.
    
    Args:
        cat_status (dict): This contains the cat's health, hunger, happiness,
        and cleanliness levels.
        environment (dict): This contains the information about the enviroment
        such as noise level and weather.
        recent_behaviors (list, optional): This contains the cat's recent
        behaviors with a deault value of None.
        
        Returns:
            str: The behavior that is returned for the cat.
        
    """
    
    
    if recent_behaviors is None:
        recent_behaviors = []
    possible_behaviors = [
        "sleep",
        "play",
        "explore",
        "hide",
        "seek_attention",
        "groom"
    ]
    
    for behavior in recent_behaviors[-2:]:
        if behavior in likely_behaviors:
            possible_behaviors.remove(behavior)
            
            
    if cat_status["health"] <= 30:
        likely_behaviors = ["sleep", "hide", "groom"]
    elif cat_status["cleanliness"] <= 30:
        likely_behaviors = ["groom", "sleep", "play"]
    elif cat_status["happiness"] <= 35:
        likely_behaviors = ["seek_attention", "play", "explore"]
    elif cat_status["hunger"] >= 70:
        likely_behaviors = ["sleep", "seek_attention", "hide"]
    elif environment.get("noise_level", 0) >= 70:
        likely_behaviors = ["hide", "sleep", "groom"]
    elif environment.get("weather", "sunny") == "sunny":
            likely_behaviors = ["explore", "play", "seek_attention"]
    else:
        likely_behaviors = ["play","sleep","groom"]
        
    for behavior in likely_behaviors:
        if behavior in likely_behaviors:
            return behavior
        
    return possible_behaviors[0] if possible_behaviors else likely_behaviors[0]

if __name__=="__main__":
    cat_status = {
        "hunger": 40,
        "health": 85,
        "happiness": 30,
        "cleanliness": 70
    }

    environment = {
        "weather": "sunny",
        "noise_level": 20
    }

    recent_behaviors = ["sleep", "explore"]

    result = determine_cat_behavior(
        cat_status,
        environment,
        recent_behaviors
    )

    print("Cat's behavior:", result)