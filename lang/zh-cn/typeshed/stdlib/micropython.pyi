"""MicroPython 内设。 (MicroPython)"""
from typing import Any, TypeVar, overload
_T = TypeVar('_T')

def const(expr: _T) -> _T:
    """用于声明表达式是一个常量，以便编译器可以优化它。 (常数)

The use of this function should be as follows::

    from micropython import const
    CONST_X = const(123)
    CONST_Y = const(2 * CONST_X + 1)

Constants declared this way are still accessible as global variables from
outside the module they are declared in. On the other hand, if a constant
begins with an underscore then it is hidden, it is not available as a
global variable, and does not take up any memory during execution.

:param expr: (表达式) 一个常量表达式。"""
    ...

@overload
def opt_level() -> int:
    """获取脚本编译的当前优化级别。 (优化级别)

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
    """设置后续脚本编译的优化级别。 (优化级别)

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

:param level: (级别) 整数优化级别。"""
    ...

def mem_info(verbose: Any=None) -> None:
    """打印与当前使用内存相关的信息。

Example: ``micropython.mem_info()``

:param verbose: (详细) 如果给出 ``verbose`` 参数，则打印额外信息。"""
    ...

def qstr_info(verbose: Any=None) -> None:
    """打印与当前驻留字符串相关的信息。 (字符串信息)

Example: ``micropython.qstr_info()``

:param verbose: (详细) 如果给出 ``verbose`` 参数，则打印额外信息。

The information that is printed is implementation dependent, but currently
includes the number of interned strings and the amount of RAM they use.  In
verbose mode it prints out the names of all RAM-interned strings."""
    ...

def stack_use() -> int:
    """返回一个整数，来表示当前正在使用的堆栈数量。 (堆栈使用)

Example: ``micropython.stack_use()``

The absolute value of this is not particularly useful, rather it
should be used to compute differences in stack usage at different points.

:return: An integer representing current stack use."""
    ...

def heap_lock() -> None:
    """锁定堆。 (锁住堆)

Example: ``micropython.heap_lock()``

When locked no memory allocation can occur and a ``MemoryError`` will be
raised if any heap allocation is attempted."""
    ...

def heap_unlock() -> None:
    """解锁堆。 (解锁堆)

Example: ``micropython.heap_unlock()``

When locked no memory allocation can occur and a ``MemoryError`` will be
raised if any heap allocation is attempted."""
    ...

def kbd_intr(chr: int) -> None:
    """设置将引发``KeyboardInterrupt``异常的字符。 (键盘中断)

Example: ``micropython.kbd_intr(-1)``

:param chr: (字符) 用于提高中断的字符代码；或者-1，用于禁止捕获 Ctrl-C。

By default this is set to 3 during script execution, corresponding to Ctrl-C.
Passing -1 to this function will disable capture of Ctrl-C, and passing 3
will restore it.

This function can be used to prevent the capturing of Ctrl-C on the
incoming stream of characters that is usually used for the REPL, in case
that stream is used for other purposes."""
    ...