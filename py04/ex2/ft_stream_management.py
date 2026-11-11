#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_stream_management.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/11 18:38:51 by aantela-            #+#    #+#            #
#   Updated: 2026/11/11 19:40:11 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import typing


def read_archive(filepath: str) -> str | None:
    sys.stdout.write(f"Accessing file '{filepath}'\n")
    try:
        file: typing.IO[str] = open(filepath, "r")
    except (FileNotFoundError, PermissionError, OSError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filepath}': {e}\n")
        return None
    try:
        content: str = file.read()
        return content
    finally:
        file.close()


def display_content(content: str, filepath: str) -> None:
    if content:
        sys.stdout.write("---\n\n")
        sys.stdout.write(content.strip("\n"))
        sys.stdout.write("\n---\n")
    sys.stdout.write(f"File '{filepath}' closed.\n")


def transform_data(content: str) -> str:
    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = [line + "#" for line in lines]
    return "\n".join(transformed_lines)


def save_archive(filename: str, content: str) -> None:
    sys.stdout.write(f"Saving data to '{filename}'\n")
    try:
        file: typing.IO[str] = open(filename, "w")
    except (FileNotFoundError, PermissionError, OSError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stdout.write("Data not saved.\n")
        return
    try:
        file.write(content + "\n")
        sys.stdout.write(f"Data Saved in file '{filename}'.\n")
    finally:
        file.close()


def handle_export(content: str) -> None:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    raw_input: str = sys.stdin.readline()
    new_filename: str = raw_input.strip()
    if not new_filename:
        sys.stdout.write("Not saving data.\n")
        return
    save_archive(new_filename, content)


def main() -> None:
    if len(sys.argv) != 2:
        sys.stdout.write("Usage: ft_ancient_creation.py <file>\n")
        return

    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    filepath: str = sys.argv[1]
    content: str | None = read_archive(filepath)
    if content is None:
        return

    display_content(content, filepath)

    sys.stdout.write("Transform data:\n")
    transformed_content: str = transform_data(content)
    sys.stdout.write("---\n\n")
    sys.stdout.write(transformed_content)
    sys.stdout.write("\n---\n")
    handle_export(transformed_content)


if __name__ == "__main__":
    main()
