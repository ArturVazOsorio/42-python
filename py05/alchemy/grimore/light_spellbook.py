#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_spellbook.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/14 15:24:38 by aantela-            #+#    #+#            #
#   Updated: 2026/11/14 15:24:39 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    if "VALID" in validation and "INVALID" not in validation:
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"