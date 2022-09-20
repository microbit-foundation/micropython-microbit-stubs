"""将数据记录到您的 micro:bit V2。 (日志)"""
from typing import Literal, Optional, Union, overload
MILLISECONDS = 1
"""毫秒时间戳格式。 (毫秒)"""
SECONDS = 10
"""秒时间戳格式。 (秒)"""
MINUTES = 600
"""分钟时间戳格式。 (分钟)"""
HOURS = 36000
"""小时时间戳格式。 (小时)"""
DAYS = 864000
"""日期时间戳格式。 (天)"""

def set_labels(*labels: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """设置日志文件头。

Example: ``log.set_labels('X', 'Y', 'Z', timestamp=log.MINUTES)``

Ideally this function should be called a single time, before any data is
logged, to configure the data table header once.

If a log file already exists when the program starts, or if this function
is called multiple times, it will check the labels already defined in the
log file. If this function call contains any new labels not already
present, it will generate a new header row with the additional columns.

By default the first column contains a timestamp for each row. The time
unit can be selected via the timestamp argument.

:param *labels: Any number of positional arguments, each corresponding to an entry in the log header.
:param timestamp: Select the timestamp unit that will be automatically added as the first column in every row. Timestamp values can be one of ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS`` or ``None`` to disable the timestamp. The default value is ``log.SECONDS``."""
    ...

@overload
def add(data_dictionary: Optional[dict[str, Union[str, int, float]]]) -> None:
    """通过传递包含标题和值的字典将数据行添加到日志中。

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: The data to log as a dictionary with a key for each header."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """使用关键字参数将数据行添加到日志中。

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """删除日志的内容，包括标题。

Example: ``log.delete()``

To add the log headers again the ``set_labels`` function should to be called after this function.

There are two erase modes; “full” completely removes the data from the physical storage,
and “fast” invalidates the data without removing it.

:param full: ``True`` selects a “full” erase and ``False`` selects the “fast” erase method."""
    ...

def set_mirroring(serial: bool):
    """Configure mirroring of the data logging activity to the serial output.

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: ``True`` enables mirroring data to the serial output."""
    ...