#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_stream.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/19 20:14:02 by aantela-            #+#    #+#            #
#   Updated: 2026/11/20 14:47:16 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any
import typing
from data_processor import (
    DataProcessor,
    TextProcessor,
    NumericProcessor,
    LogProcessor
)


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            processed = False
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break
            if not processed:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {item}"
                )

    def print_processors_stats(self) -> None:
        if not self._processors:
            print("No processor found, no data")
        for proc in self._processors:
            total = len(proc._data) + proc._rank
            remaining = len(proc._data)
            n_proc = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{n_proc}: total {total} items processed", end="")
            print(f", remaining {remaining} on processor")


if __name__ == "__main__":
    stream = DataStream()
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    stream_data: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print("\nRegistering Numeric Processor\n")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)
    print(f"Send first batch of data on stream: {stream_data}")
    stream.process_stream(stream_data)
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(txt_proc)
    stream.register_processor(log_proc)
    print("Send the same batch again")
    stream.process_stream(stream_data)
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        txt_proc.output()
    for _ in range(1):
        log_proc.output()
    print("== DataStream statistics ==")
    stream.print_processors_stats()
