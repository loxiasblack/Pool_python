#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        list_of_data = []
        if criteria == "sensor":
            for data in data_batch:
                if isinstance(data, (int, float)):
                    list_of_data.append(data)
        elif criteria == "transaction":
            for data in data_batch:
                if isinstance(data, (int, float)):
                    list_of_data.append(data)
        elif criteria == "log":
            log_instructions = ["error", "login", "logout", "info", "success"]
            for data in data_batch:
                if data in log_instructions:
                    list_of_data.append(data)
        else:
            list_of_data = data_batch
        return list_of_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {}


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.data_read = 0
        self.temp = 0
        self.data_processed = 0
        print(f"Stream {self.stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        temp = []
        pressure = []
        humidity = []
        for data in data_batch:
            if not isinstance(data, (int, float)):
                raise ValueError("the data must be numeric")
            if data <= 50:
                temp.append(data)
            elif 50 < data <= 99:
                humidity.append(data)
            else:
                pressure.append(data)
            self.data_processed += 1
        avg_temp = sum(temp) / len(temp)
        self.temp = avg_temp
        avg_hum = sum(humidity) / len(humidity)
        avg_pressure = sum(pressure) / len(pressure)
        return (
            "Processing sensor batch: "
            f"[temp:{avg_temp:.1f}, "
            f"humidity:{avg_hum:.0f}, "
            f"pressure: {avg_pressure:.0f}]"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = {}
        stats.update({"data_process": self.data_processed})
        stats.update({"temp avg": self.temp})
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.operations = 0
        self.cash_flow = 0
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        new_process = []
        i = 0
        for data in data_batch:
            if not isinstance(data, (int, float)):
                raise ValueError(f"{data} is not a numeric value")
            if i % 2 == 0:
                value = ":".join(["buy", str(data)])
                self.cash_flow += data
            else:
                value = ":".join(["sell", str(data)])
                self.cash_flow = self.cash_flow - data
            new_process.append(value)
            i += 1
            self.operations += 1
        return f"Processing transaction batch: {new_process}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = {}
        stats.update({"num_operations": self.operations})
        stats.update({"cash_flow": self.cash_flow})
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.events = 0
        self.errors = 0
        print(f"Stream ID: {self.stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        events = ["login", "logout", "status", "error"]
        for data in data_batch:
            if data not in events:
                raise ValueError("You Enter a not valid Events")
            if data == "error":
                self.errors += 1
            self.events += 1
        return f"Processing event batch: {data_batch}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = {}
        stats.update({"event": self.events})
        stats.update({"errors": self.errors})
        return stats


class StreamProcessor:
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def process_all(self, data_batch: List[Any]) -> List[str]:
        streams = []
        i = 0
        for stream in self.streams:
            streams.append(stream.process_batch(data_batch[i]))
            i += 1
        return streams


if __name__ == "__main__":
    try:
        print("Initializing Sensor Stream...")
        sensor = SensorStream("SENSOR_001")
        data = sensor.process_batch([22.5, 65, 1013])
        print(f"{data}")
        stats = sensor.get_stats()
        print(
            f"Sensor anlaysis: {stats['data_process']} "
            f"readings processed, avg temp: {stats['temp avg']}°C\n"
        )
    except ValueError as e:
        print(f"Error ValueError: {e}")

    try:
        print("Initializing Transaction Stream...")
        transaction = TransactionStream("EVENT_001")
        data = transaction.process_batch([100, 150, 75])
        print(f"{data}")
        stats = transaction.get_stats()
        list_of_transaction = transaction.filter_data(
            [100, "log", 10000, "scan"], "transaction"
        )
        print(list_of_transaction)
        print(
            f"Transaction anlaysis: {stats['num_operations']} "
            f"operations, net flow: {stats['cash_flow']} units\n"
        )
    except ValueError as e:
        print(f"Error ValueError: {e}")

    try:
        print("Initializing Event Stream...")
        event = EventStream("EVENT_001")
        data = event.process_batch(["login", "error", "logout"])
        print(f"{data}")
        stats = event.get_stats()
        print(
            f"Event analysis: {stats['event']} events"
            f", {stats['errors']} error detected\n"
        )
    except ValueError as e:
        print(f"Error ValueError: {e}")

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    streamp = StreamProcessor([sensor, transaction, event])
    list_of_process = streamp.process_all(
        [[20, 60, 300], [100, 75, 100], ["login", "error"]]
    )
    for process in list_of_process:
        print(f"{process}")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
