from .light_spellbook import light_spell_allowed_ingredients


ELEMENT = {
    "earth": "Earth",
    "air": "wind",
    "fire": "fire",
    "water": "water"
}


def validate_ingredients(ingredients: str) -> tuple[str, str]:
    allowed = light_spell_allowed_ingredients()

    words = ingredients.lower().split()

    transformed = [ELEMENT[w] for w in words if w in allowed]

    if not transformed:
        return (ingredients, "INVALID")

    if len(transformed) == 1:
        formatted = transformed[0]
    else:
        formatted = ", ".join(transformed[:-1]) + f" and {transformed[-1]}"

    return (formatted, "VALID")
