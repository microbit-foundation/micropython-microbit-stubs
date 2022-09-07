"""将数据记录到您的 micro:bit V2。 (log)"""
from typing import Literal, Optional, Union, overload
MILLISECONDS = 1
"""毫秒时间戳格式。 (milliseconds)"""
SECONDS = 10
"""秒时间戳格式。 (seconds)"""
MINUTES = 600
"""分钟时间戳格式。 (minutes)"""
HOURS = 36000
"""小时时间戳格式。 (hours)"""
DAYS = 864000
"""日期时间戳格式。 (days)"""

def set_labels(*args: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """设置日志文件头。 (set labels)

Example: ``log.set_labels('x', 'y', 'z', timestamp=log.MINUTES)``

Each call to this function with positional arguments will generate a new
header entry into the log file.

If the program starts and a log file already exists it will compare the
labels set up by this function call to the last headers declared in the
file. If the headers are different it will add a new header entry at the
end of the file.

:param *args: (*args) 每个日志头的位置参数。
:param timestamp: (timestamp) 将自动添加为每行第一列的时间戳单位。
将此参数设置为 ``None`` 来禁用时间戳。传递此模块定义的 ``log.MILLISECONDS``、 ``log.SECONDS``、 ``log.MINUTES``、 ``log.HOURS`` 或 ``log.DAYS`` 值。 无效的值会抛出异常。"""
    ...

@overload
def add(log_data: Optional[dict[str, Union[str, int, float]]]) -> None:
    """通过传递包含标题和值的字典将数据行添加到日志中。 (add)

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

Dictionary keys not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header
entry to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row.

:param log_data: (log data) 要记录为字典的数据，每个标题都有一个键。"""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """使用关键字参数将数据行添加到日志中。 (add)

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

Keyword arguments not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header entry
to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """删除日志的内容，包括标题。 (delete)

Example: ``log.delete()``

To add the log headers the ``set_labels`` function has to be called again
after this.

:param full: (full) 选择“完全”擦除模式，将数据从闪存中删除。
如果设置为 ``False`` ，它将使用“快速”方法，该方法会使得数据无效，而不是执行较慢的完全擦除。"""
    ...

def set_mirroring(serial: bool):
    """把数据记录活动镜像到串行输出。 (set mirroring)

Example: ``log.set_mirroring(True)``

Mirroring is disabled by default.

:param serial: (serial) ``True`` 则把数据记录活动镜像到串行输出，``False`` 则禁用镜像。"""
    ...