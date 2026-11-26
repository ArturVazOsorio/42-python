#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   alien_contact.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/23 21:29:15 by aantela-            #+#    #+#            #
#   Updated: 2026/11/26 16:45:22 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# from pydantic import BaseModel, Field, ValidationError
# from datetime import datetime


# class AlienContat(BaseModel):
# contact_id: str = Field(min_length=5, max_length=15)
# timestamp: datetime
# location: str =  Field(min_length=3, max_length=100)
# # contact_type: ContactType enum
# signal_strength: float = 0.0-10.0
# duration_minutes: int =  1 #-1440 #(max 24 hours)
# witness_count: int = 100 #1- 100 people
# message_received: Optional str = "", max 500 characters
# is_verified: bool =  defaults to False