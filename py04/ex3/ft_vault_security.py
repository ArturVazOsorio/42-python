#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/11 19:36:49 by aantela-            #+#    #+#            #
#   Updated: 2026/11/11 21:51:26 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                data: str = file.read()
                return (True, data)
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, f"Unsupported action: '{action}'")
    except (FileNotFoundError, PermissionError, OSError) as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    result_nonexistent: tuple[bool, str] = secure_archive("/not/existing/file")
    print(result_nonexistent, end="\n\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    result_inaccessible: tuple[bool, str] = secure_archive(
        "/etc/master.passwd")
    print(result_inaccessible, end="\n\n")

    print("Using 'secure_archive' to read from a regular file:")
    result_regular: tuple[bool, str] = secure_archive("ancient_fragment.txt")
    print(result_regular, end="\n\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    content_to_save: str = (
        result_regular[1] if result_regular[0] else "Default backup data\n"
    )
    result_write: tuple[bool, str] = secure_archive(
        "new_vault_file.txt", action="write", content=content_to_save)
    print(result_write, end="\n\n")


if __name__ == "__main__":
    main()
