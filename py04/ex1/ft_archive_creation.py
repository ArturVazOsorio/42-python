#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/11 18:40:10 by aantela-            #+#    #+#            #
#   Updated: 2026/11/11 19:38:33 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import sys
import typing


def read_archive(filepath: str) -> str | None:
    print(f"Accessing file '{filepath}'")
    try:
        file: typing.IO[str] = open(filepath, "r")
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"Error opening file '{filepath}': {e}")
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


def transform_data(content: str) -> str:
    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = [line + "#" for line in lines]
    return "\n".join(transformed_lines)


def save_archive(filename: str, content: str) -> None:
    print(f"Saving data to '{filename}'")
    try:
        file: typing.IO[str] = open(filename, "w")
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f" Error opening file '{filename}': {e}")
        return
    try:
        file.write(content + "\n")
        print(f"Data Saved in file '{filename}'.")
    finally:
        file.close()


def handle_export(content: str) -> None:
    new_filename: str = input("Enter new file name (or empty):").strip()
    if not new_filename:
        print("Not saving data.")
        return
    save_archive(new_filename, content)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    filepath: str = sys.argv[1]
    content: str | None = read_archive(filepath)
    if content is None:
        return

    display_content(content, filepath)

    print("Transform data:")
    transformed_content: str = transform_data(content)
    print("---\n")
    print(transformed_content)
    print("\n---")
    handle_export(transformed_content)


if __name__ == "__main__":
    main()
