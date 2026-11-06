#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/06 18:28:31 by aantela-         #+#    #+#              #
#    Updated: 2026/11/06 18:28:31 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


def main() -> None:

    inventory: dict[str, int] = {}

    print("=== Inventory System Analysis ===")

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Erro invalid parameter '{arg}'")
            continue

        parts = arg.split(":", 1)
        item_name = parts[0]
        quantity_str = parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' discarding")
            continue

        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
            continue

        inventory[item_name] = quantity

    if not inventory:
        print("Inventory is empty.")
        return

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of tem {len(inventory)} items: {total_quantity}")

    for item, qty in inventory.items():
        percentage = round((qty / total_quantity) * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most_abundant = max(inventory, key=inventory.get)
    print(f"Item most abundant: {most_abundant} with"
          f" quantity {inventory[most_abundant]}")

    least_abundant = min(inventory, key=inventory.get)
    print(f"Item least abundant: {least_abundant} with"
          f" quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
