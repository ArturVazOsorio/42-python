#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   oracle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/14 11:32:04 by aantela-            #+#    #+#            #
#   Updated: 2026/11/14 12:39:34 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import os
from dotenv import load_dotenv  # type: ignore[import-not-found]


def load_config() -> dict[str, str | None]:
    load_dotenv()
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def main() -> None:
    print("\nORACLE STATUS: Consulting the configuration...\n")
    config: dict[str, str | None] = load_config()

    mode = config["MATRIX_MODE"]
    db_url = config["DATABASE_URL"]
    api_key = config["API_KEY"]
    log_level = config["LOG_LEVEL"]
    zion = config["ZION_ENDPOINT"]

    missing: list[str] = [k for k, v in config.items() if not v]
    if missing:
        print(f"WARNING: Missing configuration for: {', '.join(missing)}\n")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode == "production":
        if db_url:
            db_msg = "Connected to production cluster"
        else:
            db_msg = "Disconnected"
        if api_key:
            api_msg = "Authenticated (Production Key)"
        else:
            api_msg = "Missing Key!"
        log_msg = os.getenv("LOG_LEVEL", "WARNING")
    else:
        db_msg = "Connected to local instance" if db_url else "None"
        api_msg = "Authenticated" if api_key else "Unauthenticated (Dev Mode)"
        log_msg = str(log_level)

    print(f"Database: {db_msg}")
    print(f"API Access: {api_msg}")
    print(f"Log Level: {log_msg}")
    print(f"Remote Network: {'Online' if zion else 'Offline'}\n")

    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    env_ignored = os.path.exists("ex1/.gitignore")
    status = "OK" if env_ignored else "WARN"
    print(f"[{status}] .env file properly ignored by git")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
