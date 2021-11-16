# microbit-module: log@1.0.0
"""Log data to your micro:bit."""

from typing import Literal, Optional, Union


MILLISECONDS = 1
"""Milliseconds timestamp format."""

SECONDS = 10
"""Seconds timestamp format."""

MINUTES = 600
"""Minutes timestamp format."""

HOURS = 36000
"""Hours timestamp format."""

DAYS = 864000
"""Days timestamp format."""


def set_labels(
    *args: str,
    timestamp: Optional[Literal[1, 10, 36000, 864000]] = MILLISECONDS
) -> None:
    """Set up the log file header.

    Each call to this function with positional arguments will generate a new
    header entry into the log file.

    If the program starts and a log file already exists it will compare the
    labels set up by this function call to the last headers declared in the
    file. If the headers are different it will add a new header entry at the
    end of the file.

    :param *args: Positional arguments are used to generate the log headers,
                  which go on the first line of the CSV file, so users can
                  specify as many labels as they need.
    :param timestamp: Select the timestamp unit that will be automatically
                      added as the first column in every row.
                      Setting this argument to `None` disables the timestamp.
                      Pass the ``log.MILLISECONDS``, ``log.SECONDS``, , ``log.MINUTES``,
                      ``log.HOURS`` or ``log.DAYS`` values defined by this module.
                      An invalid value will throw an exception.
    """
    ...


def set_mirroring(serial: bool):
    """Mirrors the data logging activity to the serial output.

    Mirroring is disabled by default.

    :param serial: Pass ``True`` to mirrors the data logging activity to the serial output, ``False`` to disable mirroring.
    """
    ...


def delete(full=False):
    """Deletes the contents of the log, including headers.

    To add the log headers the ``set_labels`` function has to be called again
    after this.

    :param full: Selects a "full" erase format that removes the data from the
                 flash storage. If set to ``False`` it uses a "fast" method,
                 which invalidates the data instead of performing a slower 
                 full erase.
    """
    ...


def add(
    log_data: dict[str, Union[str, int, float, bool]],
    /, *,
    **kwargs: Union[str, int, float, bool]
) -> None:
    """Add a data row to the log.
    
    Two ways to add data a data row into the log:
        1. From a positional argument dictionary (key == label)
            - e.g. ``log.add({ 'temp': microbit.temperature() })``
        2. From keyword arguments (argument name == label)
            - e.g. ``log.add(temp=microbit.temperature())``

    Each call to this function adds a row to the log.

    New data labels (dictionary keys or keyword arguments) not already
    specified via the ``set_labels`` function, or by a previous call to this
    function, will trigger a new header entry to be added to the log with
    the extra label.

    Labels previously specified and not present in this function call will be
    skipped with an empty value in the log row.
    """
    ...