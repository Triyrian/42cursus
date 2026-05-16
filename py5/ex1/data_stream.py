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
                self.total_processed += 1
        else:
            self._data.append(str(data))
            self.total_processed += 1


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
                self.total_processed += 1
        else:
            self._data.append(str(data))
            self.total_processed += 1


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
                self.total_processed += 1
        else:
            self._data.append(
                f"{data['log_level']}: {data['log_message']}"
            )
            self.total_processed += 1


class DataStream():

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            test = False
            for ops in self.processors:
                if ops.validate(element):
                    ops.ingest(element)
                    test = True
                    break

            if not test:
                print(
                    "DataStream error - Can't process element in stream:"
                    f" {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name = proc.__class__.__name__.replace(
                "Processor", " Processor"
            )
            print(
                f"{name}: total {proc.total_processed} items processed, "
                f"remaining {len(proc._data)} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    print("Initialize Data Stream...")
    check = DataStream()
    check.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    num = NumericProcessor()
    check.register_processor(num)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead',
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected',
            },
        ],
        42,
        ['Hi', 'five'],
    ]

    print(f"Send first batch of data on stream: {batch}")
    check.process_stream(batch)
    check.print_processors_stats()

    print("\nRegistering other data processors")
    txt = TextProcessor()
    log = LogProcessor()
    check.register_processor(txt)
    check.register_processor(log)

    print("Send the same batch again")
    check.process_stream(batch)
    check.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        num.output()

    for _ in range(2):
        txt.output()

    log.output()

    check.print_processors_stats()
