#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_raise_exception.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 03:02:23 by aantela-         #+#    #+#              #
#    Updated: 2026/09/11 03:42:08 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def input_temperature(temp_str) -> int:
    int_temp = int(temp_str)
    if int_temp in range(0, 41):
        return int_temp
    elif int_temp > 40:
        raise ValueError(f"{int_temp}°C is too hot for plants (max 40°C)")
    else:
        raise ValueError(f"{int_temp}°C is too cold for plants (min 0°C)")


def test_temperature(temp) -> None:
    print(f"Input data is '{temp}'")
    try:
        tmp = input_temperature(temp)
        print(f"Temperature is now {tmp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    test_temperature("100")
    print()
    test_temperature("-50")
    print("\nAll tests completed - program didn't crash!")
