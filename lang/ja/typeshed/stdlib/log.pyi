"""micro:bit V2のログにデータを記録します。"""
from typing import Literal, Optional, Union, overload
MILLISECONDS = 1
"""ミリ秒単位の日時フォーマット。"""
SECONDS = 10
"""秒単位の日時フォーマット。"""
MINUTES = 600
"""分単位の日時フォーマット。"""
HOURS = 36000
"""時間単位の日時フォーマット。"""
DAYS = 864000
"""日単位の日時フォーマット。"""

def set_labels(*args: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """ログファイルのヘッダーを設定します。

Example: ``log.set_labels('x', 'y', 'z', timestamp=log.MINUTES)``

Each call to this function with positional arguments will generate a new
header entry into the log file.

If the program starts and a log file already exists it will compare the
labels set up by this function call to the last headers declared in the
file. If the headers are different it will add a new header entry at the
end of the file.

:param *args: 各ログヘッダーの位置引数。
:param timestamp: すべての行の第１列に自動で追加される日時の単位。この引数に ``None`` を指定すると日時が追加されなくなります。
このモジュールに定義されている ``log.MILLISECONDS``、``log.SECONDS``、``log.MINUTES``、``log.HOURS``、``log.DAYS`` を渡します。不正な値を指定すると例外が起きます。"""
    ...

@overload
def add(log_data: Optional[dict[str, Union[str, int, float]]]) -> None:
    """ヘッダーと値の辞書を渡すことにより、ログにデータ行を追加します。

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

Dictionary keys not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header
entry to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row.

:param log_data: 各ヘッダーにキーがある辞書としてログに記録するデータ。"""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """キーワード引数でログにデータ行を追加します。

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

Keyword arguments not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header entry
to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """ログの内容を、ヘッダーもあわせて削除します。

Example: ``log.delete()``

To add the log headers the ``set_labels`` function has to be called again
after this.

:param full: フラッシュストレージからデータを削除する「完全」消去フォーマットを選びます。
``False`` を指定すると、遅い完全消去の代わりにデータを無効にするだけの「高速」手段を使います。"""
    ...

def set_mirroring(serial: bool):
    """データログのアクティビティをシリアル出力に反映させます。

Example: ``log.set_mirroring(True)``

Mirroring is disabled by default.

:param serial: ``True`` を渡すとデータログのアクティビティをシリアル出力に反映させるようになり、``False`` を渡すとシリアル出力への反映が無効になります。"""
    ...