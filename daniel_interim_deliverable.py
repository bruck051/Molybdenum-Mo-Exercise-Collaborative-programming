#These are placeholder classes for testing
class Player:
    pass

class Cat:
    pass

class Plant:
    pass

class Environment:
    pass

def retriever (obj, attr = None):
    """Retrieves attribute values of class instances (Player, Cat, Plant,
    Environment). If user doesn't give specific attributes, then it will return 
    all public attributes in the class. Any lists or dictionaries are returned 
    as copies so the user can't accidentally change the game state.

    Args:
        obj (object): The object that the function is going to get attributes
        from.
        attr (str or str iterable, optional): The names of the attributes being
        retrieved. If a single string, it will bw treated as list with one item.
        Defaults to None.

    Raises:
        ValueError: If obj is not an instance of the game's classes.
        KeyError: If the attribute passed in does not exist for the object.

    Returns:
        dict: A dictionary mapping each of the attributes as keys to their
        current values. 
    """    
    status = {}

    if not isinstance(obj, (Player, Cat, Plant, Environment)):
        raise ValueError (f"{obj} is not a class!")
    elif attr is None:
        attr = vars(obj)
    if isinstance(attr, str):
        attr = [attr]
    for i in attr:
        if i.startswith("_"):
            continue
        elif not hasattr(obj, i): 
            raise KeyError(f"{obj} is not a game object")
        else:
            value = getattr(obj, i)
            if isinstance(value, (list, dict)):
                value = value.copy()
            status[i] = value
    return status
    