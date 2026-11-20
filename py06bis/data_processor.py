#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_processor.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/17 02:21:32 by aantela-            #+#    #+#            #
#   Updated: 2026/11/20 15:23:05 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data available to output")
        item = self._data.pop(0)
        current_rank = self._rank
        self._rank += 1
        return (current_rank, item)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: int | float | list[int] |
               list[float] | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._data.append(str(item))
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._data.append(item)
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) and len(data) > 0:
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(item, dict) and len(item) > 0
                and all(isinstance(k, str) and isinstance(v, str)
                        for k, v in item.items())
                for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for entry in items:
            level = entry.get("log_level", "")
            msg = entry.get("log_message", "")
            self._data.append(f"{level}: {msg}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor...")
    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    x = 42
    z = "Hello"
    print(f"Trying to validate input '{x}': {num_proc.validate(x)}")
    print(f"Trying to validate input '{z}': {num_proc.validate(z)}")
    y = "foo"
    print(
        f"Testing invalid ingestion of string '{y}'"
        "without prior validation:")
    try:
        num_proc.ingest(y)  # type: ignore[arg-type]
    except Exception as e:
        print(f"Got exception: {e}")
    a = [1, 2, 3, 4, 5]
    print(f"Processing data:{a}")
    num_proc.ingest(a)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")
    print("\nTesting Text Processor...")
    txt_proc = TextProcessor()
    print(f"Trying to validate input '{x}': {txt_proc.validate(x)}")
    b = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {b}")
    txt_proc.ingest(b)
    print("Extracting 1 value...")
    rank, val = txt_proc.output()
    print(f"Text value {rank}: {val}")
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input '{z}':{log_proc.validate(z)}")
    c = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
         {'log_level': 'Error', 'log_message': 'Unauthorized access!!'}]
    print(f"processing data:{c}")
    log_proc.ingest(c)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")
