from _typeshed import SupportsWrite
from typing import Any, Callable, Tuple, Type, TypeVar
_T = TypeVar('_T')
_FuncT = TypeVar('_FuncT', bound=Callable[..., Any])

class ABCMeta(type):
    __abstractmethods__: set[str]

    def __init__(self, name: str, bases: Tuple[type, ...], namespace: dict[str, Any]) -> None:
        ...

    def __instancecheck__(cls: ABCMeta, instance: Any) -> Any:
        ...

    def __subclasscheck__(cls: ABCMeta, subclass: Any) -> Any:
        ...

    def _dump_registry(cls: ABCMeta, file: SupportsWrite[str] | None=...) -> None:
        ...

    def register(cls: ABCMeta, subclass: Type[_T]) -> Type[_T]:
        ...

def abstractmethod(funcobj: _FuncT) -> _FuncT:
    ...

class abstractproperty(property):
    ...

def abstractstaticmethod(callable: _FuncT) -> _FuncT:
    ...

def abstractclassmethod(callable: _FuncT) -> _FuncT:
    ...

class ABC(metaclass=ABCMeta):
    ...

def get_cache_token() -> object:
    ...