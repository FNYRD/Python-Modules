#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Union, Dict, Protocol


# This is the export interface that all export plugins must satisfy
# using duck typing via Protocol — no inheritance required
class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        ...


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.queue: List[Tuple[int, str]] = []
        self.total: int = 0
        self.rank: int = 0
        self.type: str = "Generic Processor"

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # Standard method: silently dequeues count items from the processor
    def output(self, count: int) -> None:
        extracted: int = 0
        while extracted < count and self.queue:
            self.queue.pop(0)
            extracted += 1

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        remaining: int = 0
        for _ in self.queue:
            remaining += 1
        stats: Dict[str, Union[str, int, float]] = {
            "total": self.total,
            "remaining": remaining
        }
        return stats


# This class will only process numeric data (int and float)
# using @staticmethod to validate individual values before ingesting
class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.type: str = "Numeric Processor"

    @staticmethod
    def is_numeric(value: Any) -> bool:
        return (isinstance(value, (int, float))
                and not isinstance(value, bool))

    def validate(self, data: Any) -> bool:
        try:
            if NumericProcessor.is_numeric(data):
                return True
            if isinstance(data, list) and data:
                for x in data:
                    if not NumericProcessor.is_numeric(x):
                        return False
                return True
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    # This method ingests the data, avoiding invalid types
    # and storing each value as a (rank, str) tuple in the queue
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        try:
            if isinstance(data, list):
                for item in data:
                    self.queue.append((self.rank, str(item)))
                    self.rank += 1
                    self.total += 1
            else:
                self.queue.append((self.rank, str(data)))
                self.rank += 1
                self.total += 1
        except Exception as e:
            print(f"Unexpected error: {e}")


# This class will only process text data (str or list of str)
class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.type: str = "Text Processor"

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, str):
                return True
            if isinstance(data, list) and data:
                for x in data:
                    if not isinstance(x, str):
                        return False
                return True
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    # This method ingests the data, avoiding invalid types
    # and storing each string as a (rank, str) tuple in the queue
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        try:
            if isinstance(data, list):
                for item in data:
                    self.queue.append((self.rank, item))
                    self.rank += 1
                    self.total += 1
            else:
                self.queue.append((self.rank, data))
                self.rank += 1
                self.total += 1
        except Exception as e:
            print(f"Unexpected error: {e}")


# This class will only process log entries (dicts with log_level/log_message)
# using @staticmethod to validate each log entry structure
class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.type: str = "Log Processor"

    @staticmethod
    def is_log_entry(value: Any) -> bool:
        return (isinstance(value, dict)
                and "log_level" in value
                and "log_message" in value)

    def validate(self, data: Any) -> bool:
        try:
            if LogProcessor.is_log_entry(data):
                return True
            if isinstance(data, list) and data:
                for x in data:
                    if not LogProcessor.is_log_entry(x):
                        return False
                return True
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    # This method ingests the data, avoiding invalid types
    # and storing each entry as (rank, "level: message") in the queue
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        try:
            if isinstance(data, list):
                for item in data:
                    level: str = item['log_level']
                    msg: str = item['log_message']
                    self.queue.append((self.rank, f"{level}: {msg}"))
                    self.rank += 1
                    self.total += 1
            else:
                level = data['log_level']
                msg = data['log_message']
                self.queue.append((self.rank, f"{level}: {msg}"))
                self.rank += 1
                self.total += 1
        except Exception as e:
            print(f"Unexpected error: {e}")


# This plugin exports processed data as comma-separated values
class CSVExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        print("CSV Output:")
        result: str = ""
        flag: int = 0
        for _, value in data:
            if flag:
                result += ","
            result += value
            flag = 1
        print(result)


# This plugin exports processed data as a JSON-formatted string
# using item_N keys where N is the original rank of each element
class JSONExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        print("JSON Output:")
        result: str = "{"
        flag: int = 0
        for rank, value in data:
            if flag:
                result += ", "
            result += f'"item_{rank}": "{value}"'
            flag = 1
        result += "}"
        print(result)


class DataStream:
    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    # Here each element is routed to the first processor that validates it
    # showing how polymorphism works with different types in the same interface
    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            processed: bool = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break
            if not processed:
                print(
                    f"DataStream error - Can't process element"
                    f" in stream: {element}"
                )

    # This method consumes nb elements from each registered processor
    # and exports them using the provided plugin via duck typing
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            items: List[Tuple[int, str]] = []
            extracted: int = 0
            while extracted < nb and proc.queue:
                items.append(proc.queue.pop(0))
                extracted += 1
            plugin.process_output(items)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            stats: Dict[str, Union[str, int, float]] = proc.get_stats()
            print(
                f"{proc.type}: total {stats['total']}"
                f" items processed, remaining"
                f" {stats['remaining']} on processor"
            )


def main() -> None:
    try:
        print("=== Code Nexus - Data Pipeline ===\n")
        ds: DataStream = DataStream()

        print("Initialize Data Stream...\n")
        ds.print_processors_stats()

        print("\nRegistering Processors\n")
        numeric: NumericProcessor = NumericProcessor()
        text: TextProcessor = TextProcessor()
        log: LogProcessor = LogProcessor()
        ds.register_processor(numeric)
        ds.register_processor(text)
        ds.register_processor(log)

        batch1: List[Any] = [
            'Hello world',
            [3.14, -1, 2.71],
            [
                {'log_level': 'WARNING',
                 'log_message': 'Telnet access! Use ssh instead'},
                {'log_level': 'INFO',
                 'log_message': 'User wil is connected'}
            ],
            42,
            ['Hi', 'five']
        ]

        print(f"Send first batch of data on stream: {batch1}\n")
        ds.process_stream(batch1)
        ds.print_processors_stats()

        csv_plugin: CSVExportPlugin = CSVExportPlugin()
        print("\nSend 3 processed data from each processor to a CSV plugin:")
        ds.output_pipeline(3, csv_plugin)
        print()
        ds.print_processors_stats()

        batch2: List[Any] = [
            21,
            ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            [
                {'log_level': 'ERROR',
                 'log_message': '500 server crash'},
                {'log_level': 'NOTICE',
                 'log_message': 'Certificate expires in 10 days'}
            ],
            [32, 42, 64, 84, 128, 168],
            'World hello'
        ]

        print(f"\nSend another batch of data: {batch2}\n")
        ds.process_stream(batch2)
        ds.print_processors_stats()

        json_plugin: JSONExportPlugin = JSONExportPlugin()
        print("\nSend 5 processed data from each processor to a JSON plugin:")
        ds.output_pipeline(5, json_plugin)
        print()
        ds.print_processors_stats()
    except (ValueError, TypeError) as e:
        print(f"Data processing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
