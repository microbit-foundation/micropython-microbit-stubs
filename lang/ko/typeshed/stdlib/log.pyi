"""micro:bit V2에 데이터를 기록합니다."""
from typing import Literal, Mapping, Optional, Union, overload
MILLISECONDS = 1
"""밀리초 타임스탬프 형식입니다."""
SECONDS = 10
"""초 타임스탬프 형식입니다."""
MINUTES = 600
"""분 타임스탬프 형식입니다."""
HOURS = 36000
"""시간 타임스탬프 형식입니다."""
DAYS = 864000
"""일 타임스탬프 형식입니다."""

def set_labels(*labels: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """로그 파일 헤더를 설정합니다.

Example: ``log.set_labels('X', 'Y', 'Z', timestamp=log.MINUTES)``

Ideally this function should be called a single time, before any data is
logged, to configure the data table header once.

If a log file already exists when the program starts, or if this function
is called multiple times, it will check the labels already defined in the
log file. If this function call contains any new labels not already
present, it will generate a new header row with the additional columns.

By default the first column contains a timestamp for each row. The time
unit can be selected via the timestamp argument.

:param *labels: (*레이블) 각각 로그 헤더의 항목에 해당하는 임의의 위치 인수 수입니다.
:param timestamp: (타임스탬프) 모든 행의 첫 번째에 자동으로 삽입될 타임스탬프 단위를 선택하십시오. 타임스탬프의 값은 ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS``가 될 수 있고 비활성화하려면 ``None``값으로 설정하십시오. 타임스탬프의 기본값은 ``log.SECONDS``입니다."""
    ...

@overload
def add(data_dictionary: Optional[Mapping[str, Union[str, int, float]]]) -> None:
    """헤더 및 값의 딕셔너리를 패스해 로그에 데이터 행을 추가합니다.

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: (데이터 사전) 각 헤더에 대한 키가 있는 사전으로 기록할 데이터입니다."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """키워드 인자를 사용해 로그에 데이터 행을 추가합니다.

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """헤더를 포함한 로그의 내용을 삭제합니다.

Example: ``log.delete()``

To add the log headers again the ``set_labels`` function should to be called after this function.

There are two erase modes; “full” completely removes the data from the physical storage,
and “fast” invalidates the data without removing it.

:param full: ``True``는 "전체" 지우기를 선택하고 ``False``는 "빠른" 지우기 방법을 선택합니다."""
    ...

def set_mirroring(serial: bool):
    """직렬 출력에 대한 데이터 로깅 작업 미러링을 구성합니다.

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: ``True``로 설정할 경우 시리얼 출력 인터페이스에 데이터를 미러링하는 것이 허용됩니다."""
    ...