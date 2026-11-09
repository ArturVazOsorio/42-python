#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: aantela- <aantela-@student.42porto.com>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/09 08:59:14 by aantela-         #+#    #+#              #
#    Updated: 2026/11/09 09:20:02 by aantela-        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from typing import Generator, Tuple, List
import random


def gen_event() -> Generator[Tuple[str, str], None, None]:
    players: List[str] = ["Alice", "bob", "charlie", "dylan"]
    actions: List[str] = ["run", "eat", "sleep", "grab", "move",
                          "climb", "swim", "use", "release"]
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
    events: List[Tuple[str, str]]
) -> Generator[Tuple[str, str], None, None]:

    while events:
        idx = random.randrange(len(events))
        event = events.pop(idx)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    stream = gen_event()

    for i in range(1000):
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    ten_events = [next(stream) for _ in range(10)]
    print(f"\nbuild list of 10 events:{ten_events}\n")

    for consumed in consume_event(ten_events):
        print(f"Got event from list: {consumed}")
        print(f"Remains in list: {ten_events}\n")
