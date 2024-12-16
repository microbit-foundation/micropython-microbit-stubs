"""MicroPython 내부 정보입니다."""
from typing import Any, TypeVar, overload
_T = TypeVar('_T')

def const(expr: _T) -> _T:
    """컴파일러가 최적화할 수 있도록 해당 수식이 상수임을 선언합니다.

The use of this function should be as follows::

    from micropython import const
    CONST_X = const(123)
    CONST_Y = const(2 * CONST_X + 1)

Constants declared this way are still accessible as global variables from
outside the module they are declared in. On the other hand, if a constant
begins with an underscore then it is hidden, it is not available as a
global variable, and does not take up any memory during execution.

:param expr: 상수 표현식입니다."""
    ...

@overload
def opt_level() -> int:
    """스크립트의 현재 컴파일 최적화 레벨을 불러옵니다.

Example: ``micropython.opt_level()``

The optimisation level controls the following compilation features:

- Assertions: at level 0 assertion statements are enabled and compiled
  into the bytecode; at levels 1 and higher assertions are not compiled.

- Built-in ``__debug__`` variable: at level 0 this variable expands to
  True; at levels 1 and higher it expands to False.

- Source-code line numbers: at levels 0, 1 and 2 source-code line number
  are stored along with the bytecode so that exceptions can report the
  line number they occurred at; at levels 3 and higher line numbers are
  not stored.

:return: An integer representing the current level."""
    ...

@overload
def opt_level(level: int) -> None:
    """스크립트의 후속 컴파일 최적화 레벨을 설정합니다.

Example: ``micropython.opt_level(1)``

The optimisation level controls the following compilation features:

- Assertions: at level 0 assertion statements are enabled and compiled
  into the bytecode; at levels 1 and higher assertions are not compiled.

- Built-in ``__debug__`` variable: at level 0 this variable expands to
  True; at levels 1 and higher it expands to False.

- Source-code line numbers: at levels 0, 1 and 2 source-code line number
  are stored along with the bytecode so that exceptions can report the
  line number they occurred at; at levels 3 and higher line numbers are
  not stored.

The default optimisation level is usually level 0.

:param level: 정수로 된 최적화 레벨입니다."""
    ...

def mem_info(verbose: Any=None) -> None:
    """현재 사용 중인 메모리에 대한 정보를 프린트합니다.

Example: ``micropython.mem_info()``

:param verbose: ``verbose`` 인자가 주어지면 추가 정보를 프린트합니다."""
    ...

def qstr_info(verbose: Any=None) -> None:
    """현재 반환된 문자열에 대한 정보를 프린트합니다.

Example: ``micropython.qstr_info()``

:param verbose: ``verbose`` 인자가 주어지면 추가 정보를 프린트합니다.

The information that is printed is implementation dependent, but currently
includes the number of interned strings and the amount of RAM they use.  In
verbose mode it prints out the names of all RAM-interned strings."""
    ...

def stack_use() -> int:
    """현재 사용 중인 스택의 수를 나타내는 정수를 반환합니다.

Example: ``micropython.stack_use()``

The absolute value of this is not particularly useful, rather it
should be used to compute differences in stack usage at different points.

:return: An integer representing current stack use."""
    ...

def heap_lock() -> None:
    """힙을 잠급니다.

Example: ``micropython.heap_lock()``

When locked no memory allocation can occur and a ``MemoryError`` will be
raised if any heap allocation is attempted."""
    ...

def heap_unlock() -> None:
    """힙을 잠금 해제합니다.

Example: ``micropython.heap_unlock()``

When locked no memory allocation can occur and a ``MemoryError`` will be
raised if any heap allocation is attempted."""
    ...

def kbd_intr(chr: int) -> None:
    """``KeyboardInterrupt`` 예외를 제기할 문자를 설정합니다.

Example: ``micropython.kbd_intr(-1)``

:param chr: 인터럽트를 제기하기 위한 문자 코드입니다. -1은 Ctrl-C 캡처를 비활성화합니다.

By default this is set to 3 during script execution, corresponding to Ctrl-C.
Passing -1 to this function will disable capture of Ctrl-C, and passing 3
will restore it.

This function can be used to prevent the capturing of Ctrl-C on the
incoming stream of characters that is usually used for the REPL, in case
that stream is used for other purposes."""
    ...