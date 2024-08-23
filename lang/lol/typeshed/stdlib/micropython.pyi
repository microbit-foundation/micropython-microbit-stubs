"""crwdns330388:0crwdne330388:0 (crwdns330386:0crwdne330386:0)"""
from typing import Any, TypeVar, overload
_T = TypeVar('_T')

def const(expr: _T) -> _T:
    """crwdns330392:0crwdne330392:0 (crwdns330390:0crwdne330390:0)

The use of this function should be as follows::

    from micropython import const
    CONST_X = const(123)
    CONST_Y = const(2 * CONST_X + 1)

Constants declared this way are still accessible as global variables from
outside the module they are declared in. On the other hand, if a constant
begins with an underscore then it is hidden, it is not available as a
global variable, and does not take up any memory during execution.

:param expr: (crwdns330394:0crwdne330394:0) crwdns330396:0crwdne330396:0"""
    ...

@overload
def opt_level() -> int:
    """crwdns330400:0crwdne330400:0 (crwdns330398:0crwdne330398:0)

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
    """crwdns330404:0crwdne330404:0 (crwdns330402:0crwdne330402:0)

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

:param level: (crwdns330406:0crwdne330406:0) crwdns330408:0crwdne330408:0"""
    ...

def mem_info(verbose: Any=None) -> None:
    """crwdns330412:0crwdne330412:0 (crwdns330410:0crwdne330410:0)

Example: ``micropython.mem_info()``

:param verbose: (crwdns330414:0crwdne330414:0) crwdns330416:0``verbose``crwdne330416:0"""
    ...

def qstr_info(verbose: Any=None) -> None:
    """crwdns330420:0crwdne330420:0 (crwdns330418:0crwdne330418:0)

Example: ``micropython.qstr_info()``

:param verbose: (crwdns330422:0crwdne330422:0) crwdns330424:0``verbose``crwdne330424:0

The information that is printed is implementation dependent, but currently
includes the number of interned strings and the amount of RAM they use.  In
verbose mode it prints out the names of all RAM-interned strings."""
    ...

def stack_use() -> int:
    """crwdns330428:0crwdne330428:0 (crwdns330426:0crwdne330426:0)

Example: ``micropython.stack_use()``

The absolute value of this is not particularly useful, rather it
should be used to compute differences in stack usage at different points.

:return: An integer representing current stack use."""
    ...

def heap_lock() -> None:
    """crwdns330432:0crwdne330432:0 (crwdns330430:0crwdne330430:0)

Example: ``micropython.heap_lock()``

When locked no memory allocation can occur and a ``MemoryError`` will be
raised if any heap allocation is attempted."""
    ...

def heap_unlock() -> None:
    """crwdns330436:0crwdne330436:0 (crwdns330434:0crwdne330434:0)

Example: ``micropython.heap_unlock()``

When locked no memory allocation can occur and a ``MemoryError`` will be
raised if any heap allocation is attempted."""
    ...

def kbd_intr(chr: int) -> None:
    """crwdns330440:0``KeyboardInterrupt``crwdne330440:0 (crwdns330438:0crwdne330438:0)

Example: ``micropython.kbd_intr(-1)``

:param chr: (crwdns330442:0crwdne330442:0) crwdns330444:0crwdne330444:0

By default this is set to 3 during script execution, corresponding to Ctrl-C.
Passing -1 to this function will disable capture of Ctrl-C, and passing 3
will restore it.

This function can be used to prevent the capturing of Ctrl-C on the
incoming stream of characters that is usually used for the REPL, in case
that stream is used for other purposes."""
    ...