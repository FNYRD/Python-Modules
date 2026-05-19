def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = ["earth", "air", "fire", "water"]
    if any(elem in ingredients.lower() for elem in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
