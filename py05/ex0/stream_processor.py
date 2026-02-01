#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        try:
            iter(data)
            for num in data:
                if type(num) is not int and type(num) is not float:
                    raise TypeError("Only Numeric Value could be processed")
            return f"{data}"
        except TypeError:
            if type(data) is not int and type(data) is not float:
                raise TypeError("Only Numeric Value could be processed")
            return f"{data}"

    def validate(self, data: Any) -> bool:
        try:
            iter(data)
            for num in data:
                if type(num) is not int and type(num) is not float:
                    return False
            return True
        except TypeError:
            if type(data) is int or type(data) is float:
                return True
            else:
                return False

    def format_output(self, result: str) -> str:
        try:
            iter(result)
            data_sum = sum(data)
            data_len = len(data)
            data_avg = data_sum / data_len
            return (
                f"Processed {data_len} numeric values, "
                f"sum={data_sum}, "
                f"avg={data_avg:.1f}"
            )
        except TypeError:
            f"Processed one number and his value: {result}"


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if type(data) is not str:
            raise TypeError("Only text values should be processed")
        return f"{data}"

    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            return False
        return True

    def format_output(self, result: str) -> str:
        word_split = result.split()
        number_words = len(word_split)
        return (
            f"Processed text: "
            f"{len(result)} characters,"
            f"{number_words} words"
        )


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        type_of_logs = ["ERROR", "INFO", "SUCCESS"]
        arg = data.split(":")
        if arg[0] not in type_of_logs and len(arg) != 2:
            raise TypeError("Not valid log message")
        return f"{data}"

    def validate(self, data: Any) -> str:
        if type(data) is not str:
            return False
        return True

    def format_output(self, result: str) -> str:
        args = result.split(":")
        if args[0] == "ERROR":
            logs_mss = "ALERT"
        else:
            logs_mss = args[0]
        return f"[{logs_mss}] {args[0]} level detected: {args[1]}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    dict_of_test = {
        numeric: [1, 2, 3, 4, 5],
        text: "Hello Nexus World",
        log: "ERROR: Connection timeout",
    }

    for data_process, data in dict_of_test.items():
        try:
            if type(data_process) is NumericProcessor:
                print("Initializing Numeric Processor...")
            if type(data_process) is TextProcessor:
                print("Initializing Text Processor...")
            if type(data_process) is LogProcessor:
                print("Initializing Log Processor...")
            print(f"Processing data: {data_process.process(data)}")
            print("Validation: ", end="")
            if data_process.validate(data):
                print("Log entry verified")
            print(f"Output: {data_process.format_output(data)}\n")
        except TypeError as e:
            print(f"{e}\n")

    print("=== Polymorphic Processing Demo ===\n")

    list_of_process = {
        NumericProcessor(): [1, 2, 3],
        TextProcessor(): "Hello World!",
        LogProcessor(): "INFO: System ready",
    }

    number = 1
    for data_process, data in list_of_process.items():
        print(f"Result {number}: {data_process.format_output(data)}")
        number += 1
    print("\nFoundation systems online. Nexus ready for advanced streams")
