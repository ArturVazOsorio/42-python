#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_first_exception.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/09 14:53:19 by aantela-         #+#    #+#              #
#    Updated: 2026/09/09 15:22:09 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def input_temperature(temp_str) -> int:
    return int(temp_str)


def test_temperature(temp) -> None:
    print(f"Input data is '{temp}'")
    try:
        tmp = input_temperature(temp)
        print(f"Temperature is now {tmp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===", end="\n\n")
    test_temperature("25")
    print()
    test_temperature("abc")
    print("\nAll tests Completed - program didn't crash!")
