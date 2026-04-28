from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._data: list[str] = []
        self._index: int = 0
        self.total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise Exception("No data")
        value = self._data.pop(0)
        index = self._index
        self._index += 1
        return index, value


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(e, (int, float)) for e in data)
        return False

    def ingest(self, data: int | float | list[Any]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, list):
            for elem in data:
                self._data.append(str(elem))
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(e, (str)) for e in data)
        return False

    def ingest(self, data: str | list[Any]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, list):
            for elem in data:
                self._data.append(str(elem))
        else:
            self._data.append(str(data))


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (
                "log_level" in data
                and "log_message" in data
                and isinstance(data["log_level"], str)
                and isinstance(data["log_message"], str)
            )
        if isinstance(data, list):
            return all(
                isinstance(elem, dict)
                and "log_level" in elem
                and "log_message" in elem
                and isinstance(elem["log_level"], str)
                and isinstance(elem["log_message"], str)
                for elem in data
            )
        return (False)

    def ingest(self, data: dict | list[dict]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, list):
            for x in data:
                self._data.append(
                    f"{x['log_level']}: {x['log_message']}"
                )
        else:
            self._data.append(
                f"{data['log_level']}: {data['log_message']}"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")

    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    print("Trying to validate input '42':", end=" ")
    print(num.validate(42))
    print("Trying to validate input 'Hello':", end=" ")
    print(num.validate("Hello"))

    print("Test invalid ingestion of string 'foo' without prior validation")

    try:
        num.ingest("foo")
    except Exception as err:
        print(f"Got exception: {err}")

    print("Processing data: [1, 2, 3, 4, 5]")
    num.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    for i in range(3):
        value = num.output()[1]
        print(f"Numeric value {i}: {value}")

    print("\nTesting Text Processor...")
    print("Trying to validate input '42':", end=" ")
    print(txt.validate(42))

    print("Processing data: ['Hello', 'Nexus', 'World']")
    try:
        txt.ingest(['Hello', 'Nexus', 'World'])
    except Exception as err:
        print(f"Got exception: {err}")

    print("Extracting 1 value...")
    try:
        value = txt.output()[1]
        print(f"Numeric value 0: {value}")
    except Exception:
        print("No data utput")

    print("\nTesting Log Processor...")

    print("Trying to validate input 'Hello':", end=" ")
    print(log.validate("Hello"))

    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'},
    ]

    print(f"Processing data: {log_data}")
    log.ingest(log_data)

    print("Extracting 2 values...")
    for i in range(2):
        index, value = log.output()
        print(f"Log entry {i}: {value}")
