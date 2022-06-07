import abc
import sys
from typing import TYPE_CHECKING as TYPE_CHECKING, Any, AsyncContextManager as AsyncContextManager, AsyncGenerator as AsyncGenerator, AsyncIterable as AsyncIterable, AsyncIterator as AsyncIterator, Awaitable as Awaitable, Callable, ChainMap as ChainMap, ClassVar as ClassVar, ContextManager as ContextManager, Coroutine as Coroutine, Counter as Counter, DefaultDict as DefaultDict, Deque as Deque, ItemsView, KeysView, Mapping, NewType as NewType, NoReturn as NoReturn, Text as Text, Tuple, Type as Type, TypeVar, ValuesView, _Alias, overload as overload
_T = TypeVar("""_T""")
_F = TypeVar("""_F""", bound=Callable[..., Any])
_TC = TypeVar("""_TC""", bound=Type[object])

class _SpecialForm:

    def __getitem__(self, typeargs: Any) -> Any:
        ...

def runtime_checkable(cls: _TC) -> _TC:
    ...
runtime = runtime_checkable
Protocol: _SpecialForm = ...
Final: _SpecialForm = ...

def final(f: _F) -> _F:
    ...
Literal: _SpecialForm = ...

def IntVar(name: str) -> Any:
    ...

class _TypedDict(Mapping[str, object], metaclass=abc.ABCMeta):

    def copy(self: _T) -> _T:
        ...

    def setdefault(self, k: NoReturn, default: object) -> object:
        ...

    def pop(self, k: NoReturn, default: _T=...) -> object:
        ...

    def update(self: _T, __m: _T) -> None:
        ...

    def items(self) -> ItemsView[str, object]:
        ...

    def keys(self) -> KeysView[str]:
        ...

    def values(self) -> ValuesView[object]:
        ...

    def __delitem__(self, k: NoReturn) -> None:
        ...
TypedDict: object = ...
OrderedDict = _Alias()

def get_type_hints(obj: Callable[..., Any], globalns: dict[str, Any] | None=..., localns: dict[str, Any] | None=..., include_extras: bool=...) -> dict[str, Any]:
    ...
if sys.version_info >= (3, 7):

    def get_args(tp: Any) -> Tuple[Any, ...]:
        ...

    def get_origin(tp: Any) -> Any | None:
        ...
Annotated: _SpecialForm = ...
_AnnotatedAlias: Any = ...

@runtime_checkable
class SupportsIndex(Protocol, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __index__(self) -> int:
        ...
if sys.version_info >= (3, 10):
    from typing import Concatenate as Concatenate, ParamSpec as ParamSpec, TypeAlias as TypeAlias, TypeGuard as TypeGuard
else:

    class ParamSpecArgs:
        __origin__: ParamSpec

        def __init__(self, origin: ParamSpec) -> None:
            ...

    class ParamSpecKwargs:
        __origin__: ParamSpec

        def __init__(self, origin: ParamSpec) -> None:
            ...

    class ParamSpec:
        __name__: str
        __bound__: Type[Any] | None
        __covariant__: bool
        __contravariant__: bool

        def __init__(self, name: str, *, bound: None | Type[Any] | str=..., contravariant: bool=..., covariant: bool=...) -> None:
            ...

        @property
        def args(self) -> ParamSpecArgs:
            ...

        @property
        def kwargs(self) -> ParamSpecKwargs:
            ...
    Concatenate: _SpecialForm = ...
    TypeAlias: _SpecialForm = ...
    TypeGuard: _SpecialForm = ...