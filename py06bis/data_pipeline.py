#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_pipeline.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: aantela- <aantela-@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/20 14:49:43 by aantela-            #+#    #+#            #
#   Updated: 2026/11/21 12:24:29 by aantela-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Protocol
from typing import Any
from data_processor import LogProcessor, NumericProcessor, TextProcessor
from data_stream import DataStream as BaseStream


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        values = [valor for _, valor in data]
        print("CSV Output:")
        print(",".join(values))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        pairs = [f'"item_{rank}": "{valor}"' for rank, valor in data]
        print("JSON Output:")
        print("{" + ", ".join(pairs) + "}")


class DataStream(BaseStream):
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted: list[tuple[int, str]] = []
            for _ in range(nb):
                if not proc._data:
                    break
                extracted.append(proc.output())
            plugin.process_output(extracted)


if __name__ == "__main__":
    stream = DataStream()
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...\n")
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nRegistering Processors\n")
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
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(num_proc)
    stream.register_processor(txt_proc)
    stream.register_processor(log_proc)
    print(f"Send first batch of data on stream: {stream_data}\n")
    stream.process_stream(stream_data)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVPlugin()
    stream.output_pipeline(3, csv_plugin)
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()
    stream_data = [
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {stream_data}")
    stream.process_stream(stream_data)
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONPlugin()
    stream.output_pipeline(5, json_plugin)
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()
