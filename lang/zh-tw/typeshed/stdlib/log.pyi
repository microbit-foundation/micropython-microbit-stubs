"""將資料記錄到您的 micro:bit V2。"""
from typing import Literal, Optional, Union, overload
MILLISECONDS = 1
"""毫秒時間戳記格式。"""
SECONDS = 10
"""秒時間戳記格式。"""
MINUTES = 600
"""分鐘時間戳記格式"""
HOURS = 36000
"""小時時間戳記格式。"""
DAYS = 864000
"""天時間戳記格式。"""

def set_labels(*args: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """設定紀錄檔案標頭。

Example: ``log.set_labels('x', 'y', 'z', timestamp=log.MINUTES)``

Each call to this function with positional arguments will generate a new
header entry into the log file.

If the program starts and a log file already exists it will compare the
labels set up by this function call to the last headers declared in the
file. If the headers are different it will add a new header entry at the
end of the file.

:param *args: 各紀錄標頭的位置引數。
:param timestamp: (時間戳記) 將自動新增為每列第一行的時間郵戳單元。
將此引數設定為 ``None``，則會停用時間戳記。傳遞此模組定義的 ``log.MILLISECONDS``、``log.SECONDS``、``log.MINUTES``、``log.HOURS`` 或 ``log.DAYS`` 值。無效值將擲回例外狀況。"""
    ...

@overload
def add(log_data: Optional[dict[str, Union[str, int, float]]]) -> None:
    """透過傳遞包含標頭和數值的字典，將資料列新增至紀錄中。

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

Dictionary keys not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header
entry to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row.

:param log_data: 若要記錄為字典的資料，每個標頭都有一把金鑰。"""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """使用關鍵字引數，將資料列新增至紀錄中。

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

Keyword arguments not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header entry
to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """刪除紀錄的內容，包括標題。

Example: ``log.delete()``

To add the log headers the ``set_labels`` function has to be called again
after this.

:param full: 選擇從快閃存放裝置中移除資料的「完全」清除格式。
如果設定為 ``False``，則會使用「快速」方法，該方法會使資料無效，而不是執行較慢的完全清除。"""
    ...

def set_mirroring(serial: bool):
    """將資料紀錄活動鏡像到序列輸出。

Example: ``log.set_mirroring(True)``

Mirroring is disabled by default.

:param serial: 傳遞 ``True`` 將資料紀錄活動鏡像到序列輸出，``False`` 則停用鏡像。"""
    ...