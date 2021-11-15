# microbit-module: data_logging@1.0.0
"""
Log data to your micro:bit
"""
from typing import TextIO, Union

def set_log(
    *args: str,
    timestamp: bool = True,
    file: Union[str, TextIO] = "log.csv",
) -> None:
    """
    Set ups
    :param *args: Positional arguments are used to generate the CSV headers,
                  which go on the first line of the CSV file, so users can
                  specify as many as they need.
    :param timestamp: Select if the timestamp will be automatically added as
                      the first column in every row
    :param file: Specify the file name or file pointer to use for the logging.
    """
    ...

def clear_log() -> None:
    """
    Deletes the contents of the log, but keeps the same headers.
    """
    ...

def add_row(
    *args: Union[str, int, float, bool],
    file: Union[str, TextIO] = "log.csv",
) -> None:
    """Adds a row into the CSV file.
    More to describe.
    :param *args: Positional arguments are used to generate the CSV headers,
                  which go on the first line of the CSV file, so users can
                  specify as many as they need.
    :param timestamp:
    :param file:
    """
    ...

def log(
    log_data: dict[str, Union[str, int, float, bool]],
    file: Union[str, TextIO] = "log.csv",
) -> None:
    """Adds a dictionary"""
    ...
