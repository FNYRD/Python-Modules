#!/usr/bin/env python3
try:
    from abc import ABC, abstractmethod
    from typing import Any, List, Union, Dict
except ImportError as e:
    print(f"Something went wrong during the import: {e}")


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.queue: List[Any] = []
        self.total: int = 0
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
    # and storing each value individually in the queue
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        try:
            if isinstance(data, list):
                for item in data:
                    self.queue.append(item)
                    self.total += 1
            else:
                self.queue.append(data)
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
    # and storing each string individually in the queue
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        try:
            if isinstance(data, list):
                for item in data:
                    self.queue.append(item)
                    self.total += 1
            else:
                self.queue.append(data)
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
    # and storing each log entry individually in the queue
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        try:
            if isinstance(data, list):
                for item in data:
                    self.queue.append(item)
                    self.total += 1
            else:
                self.queue.append(data)
                self.total += 1
        except Exception as e:
            print(f"Unexpected error: {e}")


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
        print("=== Code Nexus - Data Stream ===\n")
        ds: DataStream = DataStream()

        print("Initialize Data Stream...")
        ds.print_processors_stats()

        print("\nRegistering Numeric Processor")
        numeric: NumericProcessor = NumericProcessor()
        ds.register_processor(numeric)

        batch: List[Any] = [
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

        print(f"\nSend first batch of data on stream: {batch}")
        ds.process_stream(batch)
        ds.print_processors_stats()

        print("\nRegistering other data processors")
        text: TextProcessor = TextProcessor()
        log: LogProcessor = LogProcessor()
        ds.register_processor(text)
        ds.register_processor(log)

        print("Send the same batch again")
        ds.process_stream(batch)
        ds.print_processors_stats()

        print(
            "\nConsume some elements from the data processors:"
            " Numeric 3, Text 2, Log 1"
        )
        numeric.output(3)
        text.output(2)
        log.output(1)
        ds.print_processors_stats()
    except (ValueError, TypeError) as e:
        print(f"Data processing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()


# How does polymorphism allow the DataStream to handle different data
# types in the stream without knowing their specific implementations?
# Each processor implements validate() and ingest() differently, but
# DataStream only calls these common methods. It never needs to know
# if it's dealing with numbers, text or logs - it just asks each
# processor "can you handle this?" and delegates accordingly.
# This way adding a new data type only requires a new DataProcessor
# subclass, without touching DataStream at all.
