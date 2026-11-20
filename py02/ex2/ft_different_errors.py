#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_different_errors.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 03:46:35 by aantela-         #+#    #+#              #
#    Updated: 2026/09/15 09:24:03 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 10 / 0
    elif operation_number == 2:
        open("42.txt", "r")
    elif operation_number == 3:
        _ = "hello" + 42  # type: ignore[operator]


def test_error_types() -> None:
    for i in range(5):
        print(f"testing operation{i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
