from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    if any(elem in ingredients.lower() for elem in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
