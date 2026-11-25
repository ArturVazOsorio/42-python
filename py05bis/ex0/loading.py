#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/13 12:24:51 by aantela-            #+#    #+#            #
#   Updated: 2026/11/16 14:15:51 by aantela-          ###   ########.fr       #
#                                                                             #
# ########################################################################### #


import importlib
import importlib.metadata


def validate_import(reagents: list[str]) -> tuple[list[str], list[str]]:
    installed: list[str] = []
    missing: list[str] = []
    for pkg in reagents:
        try:
            importlib.import_module(pkg)
            version: str = importlib.metadata.version(pkg)
            summary: str = importlib.metadata.metadata(pkg)["Summary"]
            installed.append(f"[OK] {pkg} ({version}) - {summary}")
        except ModuleNotFoundError:
            missing.append(pkg)
    return installed, missing


def main() -> None:
    reagents = ["pandas", "numpy"]
    print("\nREAGENT STATUS: Loading reagents...\n")
    print("Cheching dependencies:")

    installed, missing = validate_import(reagents)

    for item in installed:
        print(item)

    if missing:
        for pkg in missing:
            print(f"[MISSING] {pkg}")
        print("\nSome reagents are missing. Install them using:")
        print("  pip install -r ex0/requirements.txt")
        print("  poetry install")

    else:
        print("\npip vs Poetry:")
        print("requirements.txt declares what to install;"
              " pip resolves it at install time.\n"
              "pyproject.toml declares the same constraints,"
              " and Poetry pins the resolved\nversions in poetry.lock"
              " so every install is identical\n"
              )
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
