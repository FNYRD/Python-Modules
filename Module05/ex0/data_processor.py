#!/usr/bin/env python3
try:
    from abc import ABC, abstractmethod
    from typing import Any, List, Tuple, Union
except ImportError as e:
    print(f"Something went wrong during the import: {e}")


class DataProcessor(ABC):
    def __init__(self) -> None:
        # Internal queue storage: saves (rank, str_value)
        # tuples in insertion order
        self.storage: List[Tuple[int, str]] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> Tuple[int, str]:
        # Extracts the oldest stored element
        # with its rank and removes it from storage
        rank, value = self.storage[0]
        self.storage.pop(0)
        return (rank, value)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        # with the two levels of try except i've covered both cases:
        # When it's an iterable element and checked every item inside
        # And when it's just a digit, verifying if is an integer or float
        # element, if not, i'll return False
        if not isinstance(data, (int, float, list)):
            return False
        if isinstance(data, list):
            if len(data) == 0:
                return False
            try:
                for numeric in data:
                    numeric + 0
            except TypeError:
                return False
        else:
            try:
                data + 0
            except TypeError:
                return False
        return True

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        # Here i checked IF is the correct datatype,
        # raising an exception if invalid
        # Then stores each element individually in the
        # internal queue with its rank
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for numeric in data:
                self.storage.append((self.rank, str(numeric)))
                self.rank += 1
        else:
            self.storage.append((self.rank, str(data)))
            self.rank += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        # with the two levels of try except i've covered both cases:
        # When it's an iterable element and checked every item inside
        # is a string And when it's just a single string, verifying it
        # can concatenate with "test42" if not, i'll return False
        if not isinstance(data, (str, list)):
            return False
        if isinstance(data, list):
            if len(data) == 0:
                return False
            try:
                for text in data:
                    text + "test42"
            except TypeError:
                return False
        else:
            try:
                data + "test42"
            except TypeError:
                return False
        return True

    def ingest(self, data: Union[str, List[str]]) -> None:
        # IF the element is not a string or list of strings,
        # raises an exception Uses the string concatenation
        # test to distinguish single string from list, then
        # stores each element individually in the internal queue with its rank
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, str):
            self.storage.append((self.rank, data))
            self.rank += 1
        else:
            for text in data:
                self.storage.append((self.rank, text))
                self.rank += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        # Validates if data is a dict with log_level and log_message keys
        # or a list of such dicts, using the same flag/length pattern
        if not isinstance(data, (dict, list)):
            return False
        if isinstance(data, list):
            if len(data) == 0:
                return False
            try:
                for item in data:
                    item['log_level'] + item['log_message'] + 'test42'
            except (TypeError, KeyError):
                return False
        else:
            try:
                data['log_level'] + data['log_message'] + 'test42'
            except (TypeError, KeyError):
                return False
        return True

    def ingest(self, data: Union[dict, List[dict]]) -> None:
        # If data is not a valid log dict or list of log dicts,
        # raises an exception Converts each dict to "log_level:
        # log_message" format and stores it individually in the
        # internal queue with its rank
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                level: str = item['log_level']
                msg: str = item['log_message']
                self.storage.append((self.rank, f"{level}: {msg}"))
                self.rank += 1
        else:
            level = data['log_level']
            msg = data['log_message']
            self.storage.append((self.rank, f"{level}: {msg}"))
            self.rank += 1


def main() -> None:
    try:
        print("=== Code Nexus - Data Processor ===\n")
        numeric: NumericProcessor = NumericProcessor()
        text: TextProcessor = TextProcessor()
        log: LogProcessor = LogProcessor()

        print("Testing Numeric Processor...")
        print(f" Trying to validate input '42': {numeric.validate(42)}")
        print(" Trying to validate input 'Hello': "
              f"{numeric.validate('Hello')}")
        print(" Test invalid ingestion of string 'foo' without prior "
              "validation:")
        try:
            numeric.ingest('foo')
        except ValueError as e:
            print(f" Got exception: {e}")

        d1: List[Union[int, float]] = [1, 2, 3, 4, 5]
        print(f" Processing data: {d1}")
        numeric.ingest(d1)
        extract: int = 3
        print(f" Extracting {extract} values...")
        index: int = 0
        while index < extract:
            rank, value = numeric.output()
            print(f" Numeric value {rank}: {value}")
            index += 1

        print("\nTesting Text Processor...")
        print(f" Trying to validate input '42': {text.validate(42)}")
        d2: List[str] = ['Hello', 'Nexus', 'World']
        print(f" Processing data: {d2}")
        text.ingest(d2)
        extract = 1
        print(f" Extracting {extract} value...")
        index = 0
        while index < extract:
            rank, value = text.output()
            print(f" Text value {rank}: {value}")
            index += 1

        print("\nTesting Log Processor...")
        print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
        d3: List[dict] = [
            {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
        ]
        print(f" Processing data: {d3}")
        log.ingest(d3)
        extract = 2
        print(f" Extracting {extract} values...")
        index = 0
        while index < extract:
            rank, value = log.output()
            print(f" Log entry {rank}: {value}")
            index += 1
    except (ValueError, TypeError) as e:
        print(f"Data processing error: {e}")
    except IndexError as e:
        print(f"Queue access error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
