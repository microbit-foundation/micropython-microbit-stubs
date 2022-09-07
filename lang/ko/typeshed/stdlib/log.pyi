"""micro:bit V2에 데이터를 기록합니다. (log)"""
from typing import Literal, Optional, Union, overload
MILLISECONDS = 1
"""밀리초 타임스탬프 형식입니다. (milliseconds)"""
SECONDS = 10
"""초 타임스탬프 형식입니다. (seconds)"""
MINUTES = 600
"""분 타임스탬프 형식입니다. (minutes)"""
HOURS = 36000
"""시간 타임스탬프 형식입니다. (hours)"""
DAYS = 864000
"""일 타임스탬프 형식입니다. (days)"""

def set_labels(*args: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """로그 파일 헤더를 설정합니다. (set labels)

Example: ``log.set_labels('x', 'y', 'z', timestamp=log.MINUTES)``

Each call to this function with positional arguments will generate a new
header entry into the log file.

If the program starts and a log file already exists it will compare the
labels set up by this function call to the last headers declared in the
file. If the headers are different it will add a new header entry at the
end of the file.

:param *args: (*args) 각 로그 헤더의 위치 매개변수입니다.
:param timestamp: (타임스탬프) 모든 행의 첫 번째 열에 자동으로 타임스탬프 유닛이 추가됩니다. 이 인자를 ``None``으로 설정하면 타임스탬프가 비활성화됩니다. 이 모듈에 정해진 값에 따라 ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS``를 패스합니다. 올바르지 않은 값은 예외 처리가 발생합니다."""
    ...

@overload
def add(log_data: Optional[dict[str, Union[str, int, float]]]) -> None:
    """헤더 및 값의 딕셔너리를 패스해 로그에 데이터 행을 추가합니다. (add)

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

Dictionary keys not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header
entry to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row.

:param log_data: (log data) 각 헤더의 키가 있는 딕셔너리로 데이터를 로그합니다."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """키워드 인자를 사용해 로그에 데이터 행을 추가합니다. (add)

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

Keyword arguments not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header entry
to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """헤더를 포함한 로그의 내용을 삭제합니다. (delete)

Example: ``log.delete()``

To add the log headers the ``set_labels`` function has to be called again
after this.

:param full: (full) 'full' 제거 형식을 선택해 플래시 저장소에서 데이터를 제거합니다.
만약 ``False``로 설정된 경우 'fast' 방식을 사용해 속도가 느린 전체 제거를 수행하는 대신 데이터를 무효화합니다."""
    ...

def set_mirroring(serial: bool):
    """데이터 로깅 활동을 시리얼 출력으로 미러링합니다. (set mirroring)

Example: ``log.set_mirroring(True)``

Mirroring is disabled by default.

:param serial: (serial) ``True``를 패스하면 데이터 로깅 활동을 시리얼 출력으로, ``False``를 패스하면 미러링을 비활성화합니다."""
    ...