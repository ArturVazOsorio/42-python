#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/09 20:15:58 by aantela-         #+#    #+#              #
#    Updated: 2026/11/10 22:45:25 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys
import typing


def read_archive(filepath: str) -> str | None:
    print(f"Accessing file '{filepath}'")
    try:
        file: typing.IO[str] = open(filepath, "r")
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"{e.__class__.__name__}: {e}")
        return None
    try:
        content: str = file.read()
        return content
    finally:
        file.close()


def display_content(content: str, filepath: str) -> None:
    if content:
        print("---\n")
        print(content.strip("\n"))
        print("\n---")
    print(f"File '{filepath}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    filepath: str = sys.argv[1]
    content: str | None = read_archive(filepath)
    if content is None:
        return

    display_content(content, filepath)


if __name__ == "__main__":
    main()
