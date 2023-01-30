"""Components interns de MicroPython."""
from typing import Any, TypeVar, overload
_T = TypeVar('_T')

def const(expr: _T) -> _T:
    """S'utilitza per declarar que l'expressió és una constant perquè el compilador pugui
optimitzar-la.

The use of this function should be as follows::

    from micropython import const
    CONST_X = const(123)
    CONST_Y = const(2 * CONST_X + 1)

Constants declared this way are still accessible as global variables from
outside the module they are declared in. On the other hand, if a constant
begins with an underscore then it is hidden, it is not available as a
global variable, and does not take up any memory during execution.

:param expr: Una expressió constant"""
    ...

@overload
def opt_level() -> int:
    """Obté el nivell d'optimització actual per a la compilació d'scripts.

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
    """Estableix el nivell d'optimització per a la compilació posterior dels scripts.

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

:param level: Un nivell d'optimització enter."""
    ...

def mem_info(verbose: Any=None) -> None:
    """Imprimeix informació sobre la memòria utilitzada actualment. (informació de la memòria)

Example: ``micropython.mem_info()``

:param verbose: Si es dona l'argument ``verbose``, s'imprimeix informació addicional."""
    ...

def qstr_info(verbose: Any=None) -> None:
    """Imprimeix informació sobre les cadenes internades actualment.

Example: ``micropython.qstr_info()``

:param verbose: Si es dona l'argument ``verbose``, s'imprimeix informació addicional.

The information that is printed is implementation dependent, but currently
includes the number of interned strings and the amount of RAM they use.  In
verbose mode it prints out the names of all RAM-interned strings."""
    ...

def stack_use() -> int:
    """Retorna un nombre enter que representa la quantitat actual de pila que està sent
utilitzada.

Example: ``micropython.stack_use()``

The absolute value of this is not particularly useful, rather it
should be used to compute differences in stack usage at different points.

:return: An integer representing current stack use."""
    ...

def heap_lock() -> None:
    """Bloqueja el munt.

Example: ``micropython.heap_lock()``

When locked no memory allocation can occur and a ``MemoryError`` will be
raised if any heap allocation is attempted."""
    ...

def heap_unlock() -> None:
    """Desbloqueja el munt.

Example: ``micropython.heap_unlock()``

When locked no memory allocation can occur and a ``MemoryError`` will be
raised if any heap allocation is attempted."""
    ...

def kbd_intr(chr: int) -> None:
    """Estableix el caràcter que generarà una excepció ``KeyboardInterrupt``.

Example: ``micropython.kbd_intr(-1)``

:param chr: Codi de caràcter per augmentar la interrupció o -1 per desactivar la captura de Ctrl-C.

By default this is set to 3 during script execution, corresponding to Ctrl-C.
Passing -1 to this function will disable capture of Ctrl-C, and passing 3
will restore it.

This function can be used to prevent the capturing of Ctrl-C on the
incoming stream of characters that is usually used for the REPL, in case
that stream is used for other purposes."""
    ...