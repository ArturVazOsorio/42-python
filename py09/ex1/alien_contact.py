#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   alien_contact.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/23 21:29:15 by aantela-            #+#    #+#            #
#   Updated: 2026/11/27 16:10:23 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from typing import Any
from datetime import datetime


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(gt=0, le=1440)
    witness_count: int = Field(gt=0, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False, description="Operational")

    @model_validator(mode="after")
    def validate_business_rules(self: Any) -> Any:
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC' (Alien Contact).")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified.")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses.")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages.")

        return self


if __name__ == "__main__":
    print("alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    try:
        valid_contact = AlienContact(
                        contact_id="AC_2024_001",
                        contact_type=ContactType.RADIO,
                        location="Area 51, Nevada",
                        signal_strength=8.5,
                        duration_minutes=45,
                        witness_count=5,
                        timestamp=datetime.now(),
                        message_received="Greetings from Zeta Reticuli",
                        is_verified=True
                        )
        print(f"ID: {valid_contact.contact_id}")
        print(f"type: {valid_contact.contact_type}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: {valid_contact.message_received}")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])
