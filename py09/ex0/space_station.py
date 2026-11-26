#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   space_station.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/23 19:45:24 by aantela-            #+#    #+#            #
#   Updated: 2026/11/26 16:48:21 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("need be used in venv and install via pip install pydantic")
    sys.exit()
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=0, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True, description="Operational")
    notes: str | None = Field(default=None, max_length=200)


def test_station(Station: SpaceStation) -> None:
    print(f"ID: {Station.station_id}")
    print(f"Name: {Station.name}")
    print(f"Crew: {Station.crew_size} people")
    print(f"Power: {Station.power_level}%")
    print(f"Oxygen: {Station.oxygen_level}%")
    # print(f"Last maintenance: {Station.last_maintenance}")
    status = "Operational" if Station.is_operational else "Offline"
    print(f"Status: {status}")
    print("\n========================================")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station_ok = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6, power_level=85.5, oxygen_level=92.3,
            last_maintenance=datetime(2024, 1, 15, 10, 30))
        print("Valid station Created:")
        test_station(station_ok)
        station_ko = SpaceStation(
            station_id="ISS0010000000000000000000000000000",
            name="International Space Station",
            crew_size=21, power_level=85.5, oxygen_level=92.3,
            last_maintenance=datetime(2024, 1, 15, 10, 30))
        test_station(station_ko)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
