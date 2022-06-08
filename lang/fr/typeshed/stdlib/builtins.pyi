import sys
import types
from _typeshed import OpenBinaryMode, OpenTextMode, ReadableBuffer, Self, StrOrBytesPath, SupportsDivMod, SupportsKeysAndGetItem, SupportsLenAndGetItem, SupportsLessThan, SupportsLessThanT, SupportsRDivMod, SupportsWrite
from types import CodeType, TracebackType
from typing import IO, AbstractSet, Any, AsyncIterable, AsyncIterator, BinaryIO, ByteString, Callable, FrozenSet, Generic, ItemsView, Iterable, Iterator, KeysView, Mapping, MutableMapping, MutableSequence, MutableSet, NoReturn, Protocol, Reversible, Sequence, Set, Sized, SupportsAbs, SupportsBytes, SupportsComplex, SupportsFloat, SupportsInt, SupportsRound, TextIO, Tuple, Type, TypeVar, Union, ValuesView, overload
from typing_extensions import Literal, SupportsIndex, final
if sys.version_info >= (3, 9):
    from types import GenericAlias

class _SupportsTrunc(Protocol):

    def __trunc__(self) -> int:
        ...
_T = TypeVar('_T')
_T_co = TypeVar('_T_co', covariant=True)
_T_contra = TypeVar('_T_contra', contravariant=True)
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')
_S = TypeVar('_S')
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_TT = TypeVar('_TT', bound='type')
_TBE = TypeVar('_TBE', bound='BaseException')

class object:
    __doc__: str | None
    __dict__: dict[str, Any]
    __slots__: str | Iterable[str]
    __module__: str
    __annotations__: dict[str, Any]

    @property
    def __class__(self: _T) -> Type[_T]:
        ...

    @__class__.setter
    def __class__(self, __type: Type[object]) -> None:
        ...

    def __init__(self) -> None:
        ...

    def __new__(cls: Type[_T]) -> _T:
        ...

    def __setattr__(self, name: str, value: Any) -> None:
        ...

    def __eq__(self, o: object) -> bool:
        ...

    def __ne__(self, o: object) -> bool:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def __hash__(self) -> int:
        ...

    def __format__(self, format_spec: str) -> str:
        ...

    def __getattribute__(self, name: str) -> Any:
        ...

    def __delattr__(self, name: str) -> None:
        ...

    def __sizeof__(self) -> int:
        ...

    def __reduce__(self) -> str | Tuple[Any, ...]:
        ...
    if sys.version_info >= (3, 8):

        def __reduce_ex__(self, protocol: SupportsIndex) -> str | Tuple[Any, ...]:
            ...
    else:

        def __reduce_ex__(self, protocol: int) -> str | Tuple[Any, ...]:
            ...

    def __dir__(self) -> Iterable[str]:
        ...

    def __init_subclass__(cls) -> None:
        ...

class staticmethod(object):
    __func__: Callable[..., Any]
    __isabstractmethod__: bool

    def __init__(self, f: Callable[..., Any]) -> None:
        ...

    def __new__(cls: Type[_T], *args: Any, **kwargs: Any) -> _T:
        ...

    def __get__(self, obj: _T, type: Type[_T] | None=...) -> Callable[..., Any]:
        ...

class classmethod(object):
    __func__: Callable[..., Any]
    __isabstractmethod__: bool

    def __init__(self, f: Callable[..., Any]) -> None:
        ...

    def __new__(cls: Type[_T], *args: Any, **kwargs: Any) -> _T:
        ...

    def __get__(self, obj: _T, type: Type[_T] | None=...) -> Callable[..., Any]:
        ...

class type(object):
    __base__: type
    __bases__: Tuple[type, ...]
    __basicsize__: int
    __dict__: dict[str, Any]
    __dictoffset__: int
    __flags__: int
    __itemsize__: int
    __module__: str
    __name__: str
    __qualname__: str
    __text_signature__: str | None
    __weakrefoffset__: int

    @overload
    def __init__(self, o: object) -> None:
        ...

    @overload
    def __init__(self, name: str, bases: Tuple[type, ...], dict: dict[str, Any], **kwds: Any) -> None:
        ...

    @overload
    def __new__(cls, o: object) -> type:
        ...

    @overload
    def __new__(cls: Type[_TT], name: str, bases: Tuple[type, ...], namespace: dict[str, Any], **kwds: Any) -> _TT:
        ...

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        ...

    def __subclasses__(self: _TT) -> list[_TT]:
        ...

    def __instancecheck__(self, instance: Any) -> bool:
        ...

    def __subclasscheck__(self, subclass: type) -> bool:
        ...

    @classmethod
    def __prepare__(metacls, __name: str, __bases: Tuple[type, ...], **kwds: Any) -> Mapping[str, Any]:
        ...
    if sys.version_info >= (3, 10):

        def __or__(self, t: Any) -> types.UnionType:
            ...

        def __ror__(self, t: Any) -> types.UnionType:
            ...

class super(object):

    @overload
    def __init__(self, t: Any, obj: Any) -> None:
        ...

    @overload
    def __init__(self, t: Any) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

class int:

    @overload
    def __new__(cls: Type[_T], x: str | bytes | SupportsInt | SupportsIndex | _SupportsTrunc=...) -> _T:
        ...

    @overload
    def __new__(cls: Type[_T], x: str | bytes | bytearray, base: SupportsIndex) -> _T:
        ...

    def to_bytes(self, length: SupportsIndex, byteorder: Literal['little', 'big'], *, signed: bool=...) -> bytes:
        ...

    @classmethod
    def from_bytes(cls, bytes: Iterable[SupportsIndex] | SupportsBytes, byteorder: Literal['little', 'big'], *, signed: bool=...) -> int:
        ...

    def __add__(self, x: int) -> int:
        ...

    def __sub__(self, x: int) -> int:
        ...

    def __mul__(self, x: int) -> int:
        ...

    def __floordiv__(self, x: int) -> int:
        ...

    def __truediv__(self, x: int) -> float:
        ...

    def __mod__(self, x: int) -> int:
        ...

    def __divmod__(self, x: int) -> Tuple[int, int]:
        ...

    def __radd__(self, x: int) -> int:
        ...

    def __rsub__(self, x: int) -> int:
        ...

    def __rmul__(self, x: int) -> int:
        ...

    def __rfloordiv__(self, x: int) -> int:
        ...

    def __rtruediv__(self, x: int) -> float:
        ...

    def __rmod__(self, x: int) -> int:
        ...

    def __rdivmod__(self, x: int) -> Tuple[int, int]:
        ...

    @overload
    def __pow__(self, __x: Literal[2], __modulo: int | None=...) -> int:
        ...

    @overload
    def __pow__(self, __x: int, __modulo: int | None=...) -> Any:
        ...

    def __rpow__(self, x: int, mod: int | None=...) -> Any:
        ...

    def __and__(self, n: int) -> int:
        ...

    def __or__(self, n: int) -> int:
        ...

    def __xor__(self, n: int) -> int:
        ...

    def __lshift__(self, n: int) -> int:
        ...

    def __rshift__(self, n: int) -> int:
        ...

    def __rand__(self, n: int) -> int:
        ...

    def __ror__(self, n: int) -> int:
        ...

    def __rxor__(self, n: int) -> int:
        ...

    def __rlshift__(self, n: int) -> int:
        ...

    def __rrshift__(self, n: int) -> int:
        ...

    def __neg__(self) -> int:
        ...

    def __pos__(self) -> int:
        ...

    def __invert__(self) -> int:
        ...

    def __trunc__(self) -> int:
        ...

    def __ceil__(self) -> int:
        ...

    def __floor__(self) -> int:
        ...

    def __round__(self, ndigits: SupportsIndex=...) -> int:
        ...

    def __getnewargs__(self) -> Tuple[int]:
        ...

    def __eq__(self, x: object) -> bool:
        ...

    def __ne__(self, x: object) -> bool:
        ...

    def __lt__(self, x: int) -> bool:
        ...

    def __le__(self, x: int) -> bool:
        ...

    def __gt__(self, x: int) -> bool:
        ...

    def __ge__(self, x: int) -> bool:
        ...

    def __str__(self) -> str:
        ...

    def __float__(self) -> float:
        ...

    def __int__(self) -> int:
        ...

    def __abs__(self) -> int:
        ...

    def __hash__(self) -> int:
        ...

    def __bool__(self) -> bool:
        ...

    def __index__(self) -> int:
        ...

class float:

    def __new__(cls: Type[_T], x: SupportsFloat | SupportsIndex | str | bytes | bytearray=...) -> _T:
        ...

    def __add__(self, x: float) -> float:
        ...

    def __sub__(self, x: float) -> float:
        ...

    def __mul__(self, x: float) -> float:
        ...

    def __floordiv__(self, x: float) -> float:
        ...

    def __truediv__(self, x: float) -> float:
        ...

    def __mod__(self, x: float) -> float:
        ...

    def __divmod__(self, x: float) -> Tuple[float, float]:
        ...

    def __pow__(self, x: float, mod: None=...) -> float:
        ...

    def __radd__(self, x: float) -> float:
        ...

    def __rsub__(self, x: float) -> float:
        ...

    def __rmul__(self, x: float) -> float:
        ...

    def __rfloordiv__(self, x: float) -> float:
        ...

    def __rtruediv__(self, x: float) -> float:
        ...

    def __rmod__(self, x: float) -> float:
        ...

    def __rdivmod__(self, x: float) -> Tuple[float, float]:
        ...

    def __rpow__(self, x: float, mod: None=...) -> float:
        ...

    def __getnewargs__(self) -> Tuple[float]:
        ...

    def __trunc__(self) -> int:
        ...
    if sys.version_info >= (3, 9):

        def __ceil__(self) -> int:
            ...

        def __floor__(self) -> int:
            ...

    @overload
    def __round__(self, ndigits: None=...) -> int:
        ...

    @overload
    def __round__(self, ndigits: SupportsIndex) -> float:
        ...

    def __eq__(self, x: object) -> bool:
        ...

    def __ne__(self, x: object) -> bool:
        ...

    def __lt__(self, x: float) -> bool:
        ...

    def __le__(self, x: float) -> bool:
        ...

    def __gt__(self, x: float) -> bool:
        ...

    def __ge__(self, x: float) -> bool:
        ...

    def __neg__(self) -> float:
        ...

    def __pos__(self) -> float:
        ...

    def __str__(self) -> str:
        ...

    def __int__(self) -> int:
        ...

    def __float__(self) -> float:
        ...

    def __abs__(self) -> float:
        ...

    def __hash__(self) -> int:
        ...

    def __bool__(self) -> bool:
        ...

class complex:

    @overload
    def __new__(cls: Type[_T], real: float=..., imag: float=...) -> _T:
        ...

    @overload
    def __new__(cls: Type[_T], real: str | SupportsComplex | SupportsIndex | complex) -> _T:
        ...

    @property
    def real(self) -> float:
        ...

    @property
    def imag(self) -> float:
        ...

    def __add__(self, x: complex) -> complex:
        ...

    def __sub__(self, x: complex) -> complex:
        ...

    def __mul__(self, x: complex) -> complex:
        ...

    def __pow__(self, x: complex, mod: None=...) -> complex:
        ...

    def __truediv__(self, x: complex) -> complex:
        ...

    def __radd__(self, x: complex) -> complex:
        ...

    def __rsub__(self, x: complex) -> complex:
        ...

    def __rmul__(self, x: complex) -> complex:
        ...

    def __rpow__(self, x: complex, mod: None=...) -> complex:
        ...

    def __rtruediv__(self, x: complex) -> complex:
        ...

    def __eq__(self, x: object) -> bool:
        ...

    def __ne__(self, x: object) -> bool:
        ...

    def __neg__(self) -> complex:
        ...

    def __pos__(self) -> complex:
        ...

    def __str__(self) -> str:
        ...

    def __abs__(self) -> float:
        ...

    def __hash__(self) -> int:
        ...

    def __bool__(self) -> bool:
        ...

class str(Sequence[str]):

    @overload
    def __new__(cls: Type[_T], o: object=...) -> _T:
        ...

    @overload
    def __new__(cls: Type[_T], o: bytes, encoding: str=..., errors: str=...) -> _T:
        ...

    def count(self, x: str, __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> int:
        ...

    def encode(self, encoding: str=..., errors: str=...) -> bytes:
        ...

    def endswith(self, __suffix: str | Tuple[str, ...], __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> bool:
        ...

    def find(self, __sub: str, __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> int:
        ...

    def format(self, *args: object, **kwargs: object) -> str:
        ...

    def index(self, __sub: str, __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> int:
        ...

    def isalpha(self) -> bool:
        ...

    def isdigit(self) -> bool:
        ...

    def islower(self) -> bool:
        ...

    def isspace(self) -> bool:
        ...

    def isupper(self) -> bool:
        ...

    def join(self, __iterable: Iterable[str]) -> str:
        ...

    def lower(self) -> str:
        ...

    def lstrip(self, __chars: str | None=...) -> str:
        ...

    def replace(self, __old: str, __new: str, __count: SupportsIndex=...) -> str:
        ...

    def rfind(self, __sub: str, __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> int:
        ...

    def rindex(self, __sub: str, __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> int:
        ...

    def rsplit(self, sep: str | None=..., maxsplit: SupportsIndex=...) -> list[str]:
        ...

    def rstrip(self, __chars: str | None=...) -> str:
        ...

    def split(self, sep: str | None=..., maxsplit: SupportsIndex=...) -> list[str]:
        ...

    def startswith(self, __prefix: str | Tuple[str, ...], __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> bool:
        ...

    def strip(self, __chars: str | None=...) -> str:
        ...

    def upper(self) -> str:
        ...

    def __add__(self, s: str) -> str:
        ...

    def __contains__(self, o: str) -> bool:
        ...

    def __eq__(self, x: object) -> bool:
        ...

    def __ge__(self, x: str) -> bool:
        ...

    def __getitem__(self, i: int | slice) -> str:
        ...

    def __gt__(self, x: str) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    def __iter__(self) -> Iterator[str]:
        ...

    def __le__(self, x: str) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def __lt__(self, x: str) -> bool:
        ...

    def __mod__(self, x: Any) -> str:
        ...

    def __mul__(self, n: SupportsIndex) -> str:
        ...

    def __ne__(self, x: object) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def __rmul__(self, n: SupportsIndex) -> str:
        ...

    def __str__(self) -> str:
        ...

    def __getnewargs__(self) -> Tuple[str]:
        ...

class bytes(ByteString):

    @overload
    def __new__(cls: Type[_T], ints: Iterable[SupportsIndex]) -> _T:
        ...

    @overload
    def __new__(cls: Type[_T], string: str, encoding: str, errors: str=...) -> _T:
        ...

    @overload
    def __new__(cls: Type[_T], length: SupportsIndex) -> _T:
        ...

    @overload
    def __new__(cls: Type[_T]) -> _T:
        ...

    @overload
    def __new__(cls: Type[_T], o: SupportsBytes) -> _T:
        ...

    def count(self, __sub: bytes | SupportsIndex, __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> int:
        ...

    def decode(self, encoding: str=..., errors: str=...) -> str:
        ...

    def endswith(self, __suffix: bytes | Tuple[bytes, ...], __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> bool:
        ...

    def find(self, __sub: bytes | SupportsIndex, __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> int:
        ...

    def index(self, __sub: bytes | SupportsIndex, __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> int:
        ...

    def isalpha(self) -> bool:
        ...

    def isdigit(self) -> bool:
        ...

    def islower(self) -> bool:
        ...

    def isspace(self) -> bool:
        ...

    def isupper(self) -> bool:
        ...

    def join(self, __iterable_of_bytes: Iterable[ByteString | memoryview]) -> bytes:
        ...

    def lower(self) -> bytes:
        ...

    def lstrip(self, __bytes: bytes | None=...) -> bytes:
        ...

    def replace(self, __old: bytes, __new: bytes, __count: SupportsIndex=...) -> bytes:
        ...

    def rfind(self, __sub: bytes | SupportsIndex, __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> int:
        ...

    def rindex(self, __sub: bytes | SupportsIndex, __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> int:
        ...

    def rsplit(self, sep: bytes | None=..., maxsplit: SupportsIndex=...) -> list[bytes]:
        ...

    def rstrip(self, __bytes: bytes | None=...) -> bytes:
        ...

    def split(self, sep: bytes | None=..., maxsplit: SupportsIndex=...) -> list[bytes]:
        ...

    def startswith(self, __prefix: bytes | Tuple[bytes, ...], __start: SupportsIndex | None=..., __end: SupportsIndex | None=...) -> bool:
        ...

    def strip(self, __bytes: bytes | None=...) -> bytes:
        ...

    def upper(self) -> bytes:
        ...

    def __len__(self) -> int:
        ...

    def __iter__(self) -> Iterator[int]:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def __hash__(self) -> int:
        ...

    @overload
    def __getitem__(self, i: SupportsIndex) -> int:
        ...

    @overload
    def __getitem__(self, s: slice) -> bytes:
        ...

    def __add__(self, s: bytes) -> bytes:
        ...

    def __mul__(self, n: SupportsIndex) -> bytes:
        ...

    def __rmul__(self, n: SupportsIndex) -> bytes:
        ...

    def __mod__(self, value: Any) -> bytes:
        ...

    def __contains__(self, o: SupportsIndex | bytes) -> bool:
        ...

    def __eq__(self, x: object) -> bool:
        ...

    def __ne__(self, x: object) -> bool:
        ...

    def __lt__(self, x: bytes) -> bool:
        ...

    def __le__(self, x: bytes) -> bool:
        ...

    def __gt__(self, x: bytes) -> bool:
        ...

    def __ge__(self, x: bytes) -> bool:
        ...

    def __getnewargs__(self) -> Tuple[bytes]:
        ...

class bytearray:

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, ints: Iterable[SupportsIndex]) -> None:
        ...

    @overload
    def __init__(self, string: str, encoding: str, errors: str=...) -> None:
        ...

    @overload
    def __init__(self, length: SupportsIndex) -> None:
        ...

    def append(self, __item: SupportsIndex) -> None:
        ...

    def decode(self, encoding: str=..., errors: str=...) -> str:
        ...

    def extend(self, __iterable_of_ints: Iterable[SupportsIndex]) -> None:
        ...

    def __len__(self) -> int:
        ...

    def __iter__(self) -> Iterator[int]:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...
    __hash__: None

    @overload
    def __getitem__(self, i: SupportsIndex) -> int:
        ...

    @overload
    def __getitem__(self, s: slice) -> bytearray:
        ...

    @overload
    def __setitem__(self, i: SupportsIndex, x: SupportsIndex) -> None:
        ...

    @overload
    def __setitem__(self, s: slice, x: Iterable[SupportsIndex] | bytes) -> None:
        ...

    def __delitem__(self, i: SupportsIndex | slice) -> None:
        ...

    def __add__(self, s: bytes) -> bytearray:
        ...

    def __iadd__(self, s: Iterable[int]) -> bytearray:
        ...

    def __mul__(self, n: SupportsIndex) -> bytearray:
        ...

    def __rmul__(self, n: SupportsIndex) -> bytearray:
        ...

    def __imul__(self, n: SupportsIndex) -> bytearray:
        ...

    def __mod__(self, value: Any) -> bytes:
        ...

    def __contains__(self, o: SupportsIndex | bytes) -> bool:
        ...

    def __eq__(self, x: object) -> bool:
        ...

    def __ne__(self, x: object) -> bool:
        ...

    def __lt__(self, x: bytes) -> bool:
        ...

    def __le__(self, x: bytes) -> bool:
        ...

    def __gt__(self, x: bytes) -> bool:
        ...

    def __ge__(self, x: bytes) -> bool:
        ...

class memoryview(Sized, Sequence[int]):

    def __init__(self, obj: ReadableBuffer) -> None:
        ...

    @overload
    def __getitem__(self, i: SupportsIndex) -> int:
        ...

    @overload
    def __getitem__(self, s: slice) -> memoryview:
        ...

    def __contains__(self, x: object) -> bool:
        ...

    def __iter__(self) -> Iterator[int]:
        ...

    def __len__(self) -> int:
        ...

    @overload
    def __setitem__(self, s: slice, o: bytes) -> None:
        ...

    @overload
    def __setitem__(self, i: SupportsIndex, o: SupportsIndex) -> None:
        ...

@final
class bool(int):

    def __new__(cls: Type[_T], __o: object=...) -> _T:
        ...

    @overload
    def __and__(self, x: bool) -> bool:
        ...

    @overload
    def __and__(self, x: int) -> int:
        ...

    @overload
    def __or__(self, x: bool) -> bool:
        ...

    @overload
    def __or__(self, x: int) -> int:
        ...

    @overload
    def __xor__(self, x: bool) -> bool:
        ...

    @overload
    def __xor__(self, x: int) -> int:
        ...

    @overload
    def __rand__(self, x: bool) -> bool:
        ...

    @overload
    def __rand__(self, x: int) -> int:
        ...

    @overload
    def __ror__(self, x: bool) -> bool:
        ...

    @overload
    def __ror__(self, x: int) -> int:
        ...

    @overload
    def __rxor__(self, x: bool) -> bool:
        ...

    @overload
    def __rxor__(self, x: int) -> int:
        ...

    def __getnewargs__(self) -> Tuple[int]:
        ...

class slice(object):
    start: Any
    step: Any
    stop: Any
    __hash__: None

    def indices(self, len: SupportsIndex) -> Tuple[int, int, int]:
        ...

class tuple(Sequence[_T_co], Generic[_T_co]):

    def __new__(cls: Type[_T], iterable: Iterable[_T_co]=...) -> _T:
        ...

    def __len__(self) -> int:
        ...

    def __contains__(self, x: object) -> bool:
        ...

    @overload
    def __getitem__(self, x: int) -> _T_co:
        ...

    @overload
    def __getitem__(self, x: slice) -> Tuple[_T_co, ...]:
        ...

    def __iter__(self) -> Iterator[_T_co]:
        ...

    def __lt__(self, x: Tuple[_T_co, ...]) -> bool:
        ...

    def __le__(self, x: Tuple[_T_co, ...]) -> bool:
        ...

    def __gt__(self, x: Tuple[_T_co, ...]) -> bool:
        ...

    def __ge__(self, x: Tuple[_T_co, ...]) -> bool:
        ...

    @overload
    def __add__(self, x: Tuple[_T_co, ...]) -> Tuple[_T_co, ...]:
        ...

    @overload
    def __add__(self, x: Tuple[_T, ...]) -> Tuple[_T_co | _T, ...]:
        ...

    def __mul__(self, n: SupportsIndex) -> Tuple[_T_co, ...]:
        ...

    def __rmul__(self, n: SupportsIndex) -> Tuple[_T_co, ...]:
        ...

    def count(self, __value: Any) -> int:
        ...

    def index(self, __value: Any, __start: SupportsIndex=..., __stop: SupportsIndex=...) -> int:
        ...

class function:
    __name__: str
    __module__: str
    __code__: CodeType
    __qualname__: str
    __annotations__: dict[str, Any]

class list(MutableSequence[_T], Generic[_T]):

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, iterable: Iterable[_T]) -> None:
        ...

    def clear(self) -> None:
        ...

    def copy(self) -> list[_T]:
        ...

    def append(self, __object: _T) -> None:
        ...

    def extend(self, __iterable: Iterable[_T]) -> None:
        ...

    def pop(self, __index: SupportsIndex=...) -> _T:
        ...

    def index(self, __value: _T, __start: SupportsIndex=..., __stop: SupportsIndex=...) -> int:
        ...

    def count(self, __value: _T) -> int:
        ...

    def insert(self, __index: SupportsIndex, __object: _T) -> None:
        ...

    def remove(self, __value: _T) -> None:
        ...

    def reverse(self) -> None:
        ...

    @overload
    def sort(self: list[SupportsLessThanT], *, key: None=..., reverse: bool=...) -> None:
        ...

    @overload
    def sort(self, *, key: Callable[[_T], SupportsLessThan], reverse: bool=...) -> None:
        ...

    def __len__(self) -> int:
        ...

    def __iter__(self) -> Iterator[_T]:
        ...

    def __str__(self) -> str:
        ...
    __hash__: None

    @overload
    def __getitem__(self, i: SupportsIndex) -> _T:
        ...

    @overload
    def __getitem__(self, s: slice) -> list[_T]:
        ...

    @overload
    def __setitem__(self, i: SupportsIndex, o: _T) -> None:
        ...

    @overload
    def __setitem__(self, s: slice, o: Iterable[_T]) -> None:
        ...

    def __delitem__(self, i: SupportsIndex | slice) -> None:
        ...

    def __add__(self, x: list[_T]) -> list[_T]:
        ...

    def __iadd__(self: _S, x: Iterable[_T]) -> _S:
        ...

    def __mul__(self, n: SupportsIndex) -> list[_T]:
        ...

    def __rmul__(self, n: SupportsIndex) -> list[_T]:
        ...

    def __imul__(self: _S, n: SupportsIndex) -> _S:
        ...

    def __contains__(self, o: object) -> bool:
        ...

    def __reversed__(self) -> Iterator[_T]:
        ...

    def __gt__(self, x: list[_T]) -> bool:
        ...

    def __ge__(self, x: list[_T]) -> bool:
        ...

    def __lt__(self, x: list[_T]) -> bool:
        ...

    def __le__(self, x: list[_T]) -> bool:
        ...
    if sys.version_info >= (3, 9):

        def __class_getitem__(cls, item: Any) -> GenericAlias:
            ...

class dict(MutableMapping[_KT, _VT], Generic[_KT, _VT]):

    @overload
    def __init__(self: dict[_KT, _VT]) -> None:
        ...

    @overload
    def __init__(self: dict[str, _VT], **kwargs: _VT) -> None:
        ...

    @overload
    def __init__(self, map: SupportsKeysAndGetItem[_KT, _VT], **kwargs: _VT) -> None:
        ...

    @overload
    def __init__(self, iterable: Iterable[Tuple[_KT, _VT]], **kwargs: _VT) -> None:
        ...

    def __new__(cls: Type[_T1], *args: Any, **kwargs: Any) -> _T1:
        ...

    def clear(self) -> None:
        ...

    def copy(self) -> dict[_KT, _VT]:
        ...

    def popitem(self) -> Tuple[_KT, _VT]:
        ...

    def setdefault(self, __key: _KT, __default: _VT=...) -> _VT:
        ...

    @overload
    def update(self, __m: Mapping[_KT, _VT], **kwargs: _VT) -> None:
        ...

    @overload
    def update(self, __m: Iterable[Tuple[_KT, _VT]], **kwargs: _VT) -> None:
        ...

    @overload
    def update(self, **kwargs: _VT) -> None:
        ...

    def keys(self) -> KeysView[_KT]:
        ...

    def values(self) -> ValuesView[_VT]:
        ...

    def items(self) -> ItemsView[_KT, _VT]:
        ...

    @classmethod
    @overload
    def fromkeys(cls, __iterable: Iterable[_T], __value: None=...) -> dict[_T, Any | None]:
        ...

    @classmethod
    @overload
    def fromkeys(cls, __iterable: Iterable[_T], __value: _S) -> dict[_T, _S]:
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, k: _KT) -> _VT:
        ...

    def __setitem__(self, k: _KT, v: _VT) -> None:
        ...

    def __delitem__(self, v: _KT) -> None:
        ...

    def __iter__(self) -> Iterator[_KT]:
        ...
    if sys.version_info >= (3, 8):

        def __reversed__(self) -> Iterator[_KT]:
            ...

    def __str__(self) -> str:
        ...
    __hash__: None
    if sys.version_info >= (3, 9):

        def __class_getitem__(cls, item: Any) -> GenericAlias:
            ...

        def __or__(self, __value: Mapping[_T1, _T2]) -> dict[_KT | _T1, _VT | _T2]:
            ...

        def __ror__(self, __value: Mapping[_T1, _T2]) -> dict[_KT | _T1, _VT | _T2]:
            ...

        def __ior__(self, __value: Mapping[_KT, _VT]) -> dict[_KT, _VT]:
            ...

class set(MutableSet[_T], Generic[_T]):

    def __init__(self, iterable: Iterable[_T]=...) -> None:
        ...

    def add(self, element: _T) -> None:
        ...

    def clear(self) -> None:
        ...

    def copy(self) -> Set[_T]:
        ...

    def difference(self, *s: Iterable[Any]) -> Set[_T]:
        ...

    def difference_update(self, *s: Iterable[Any]) -> None:
        ...

    def discard(self, element: _T) -> None:
        ...

    def intersection(self, *s: Iterable[Any]) -> Set[_T]:
        ...

    def intersection_update(self, *s: Iterable[Any]) -> None:
        ...

    def isdisjoint(self, s: Iterable[Any]) -> bool:
        ...

    def issubset(self, s: Iterable[Any]) -> bool:
        ...

    def issuperset(self, s: Iterable[Any]) -> bool:
        ...

    def pop(self) -> _T:
        ...

    def remove(self, element: _T) -> None:
        ...

    def symmetric_difference(self, s: Iterable[_T]) -> Set[_T]:
        ...

    def symmetric_difference_update(self, s: Iterable[_T]) -> None:
        ...

    def union(self, *s: Iterable[_T]) -> Set[_T]:
        ...

    def update(self, *s: Iterable[_T]) -> None:
        ...

    def __len__(self) -> int:
        ...

    def __contains__(self, o: object) -> bool:
        ...

    def __iter__(self) -> Iterator[_T]:
        ...

    def __str__(self) -> str:
        ...

    def __and__(self, s: AbstractSet[object]) -> Set[_T]:
        ...

    def __iand__(self, s: AbstractSet[object]) -> Set[_T]:
        ...

    def __or__(self, s: AbstractSet[_S]) -> Set[_T | _S]:
        ...

    def __ior__(self, s: AbstractSet[_S]) -> Set[_T | _S]:
        ...

    def __sub__(self, s: AbstractSet[_T | None]) -> Set[_T]:
        ...

    def __isub__(self, s: AbstractSet[_T | None]) -> Set[_T]:
        ...

    def __xor__(self, s: AbstractSet[_S]) -> Set[_T | _S]:
        ...

    def __ixor__(self, s: AbstractSet[_S]) -> Set[_T | _S]:
        ...

    def __le__(self, s: AbstractSet[object]) -> bool:
        ...

    def __lt__(self, s: AbstractSet[object]) -> bool:
        ...

    def __ge__(self, s: AbstractSet[object]) -> bool:
        ...

    def __gt__(self, s: AbstractSet[object]) -> bool:
        ...
    __hash__: None
    if sys.version_info >= (3, 9):

        def __class_getitem__(cls, item: Any) -> GenericAlias:
            ...

class enumerate(Iterator[Tuple[int, _T]], Generic[_T]):

    def __init__(self, iterable: Iterable[_T], start: int=...) -> None:
        ...

    def __iter__(self) -> Iterator[Tuple[int, _T]]:
        ...

    def __next__(self) -> Tuple[int, _T]:
        ...
    if sys.version_info >= (3, 9):

        def __class_getitem__(cls, item: Any) -> GenericAlias:
            ...

class range(Sequence[int]):
    start: int
    stop: int
    step: int

    @overload
    def __init__(self, stop: SupportsIndex) -> None:
        ...

    @overload
    def __init__(self, start: SupportsIndex, stop: SupportsIndex, step: SupportsIndex=...) -> None:
        ...

    def __len__(self) -> int:
        ...

    def __contains__(self, o: object) -> bool:
        ...

    def __iter__(self) -> Iterator[int]:
        ...

    @overload
    def __getitem__(self, i: SupportsIndex) -> int:
        ...

    @overload
    def __getitem__(self, s: slice) -> range:
        ...

    def __repr__(self) -> str:
        ...

    def __reversed__(self) -> Iterator[int]:
        ...

class property(object):
    fget: Callable[[Any], Any] | None
    fset: Callable[[Any, Any], None] | None
    fdel: Callable[[Any], None] | None

    def __init__(self, fget: Callable[[Any], Any] | None=..., fset: Callable[[Any, Any], None] | None=..., fdel: Callable[[Any], None] | None=..., doc: str | None=...) -> None:
        ...

    def getter(self, fget: Callable[[Any], Any]) -> property:
        ...

    def setter(self, fset: Callable[[Any, Any], None]) -> property:
        ...

    def deleter(self, fdel: Callable[[Any], None]) -> property:
        ...

    def __get__(self, obj: Any, type: type | None=...) -> Any:
        ...

    def __set__(self, obj: Any, value: Any) -> None:
        ...

    def __delete__(self, obj: Any) -> None:
        ...

class _NotImplementedType(Any):
    __call__: NotImplemented
NotImplemented: _NotImplementedType

def abs(__x: SupportsAbs[_T]) -> _T:
    ...

def all(__iterable: Iterable[object]) -> bool:
    ...

def any(__iterable: Iterable[object]) -> bool:
    ...

def bin(__number: int | SupportsIndex) -> str:
    ...
if sys.version_info >= (3, 7):

    def breakpoint(*args: Any, **kws: Any) -> None:
        ...

def callable(__obj: object) -> bool:
    ...

def chr(__i: int) -> str:
    ...
_AnyStr_co = TypeVar('_AnyStr_co', str, bytes, covariant=True)

class _PathLike(Protocol[_AnyStr_co]):

    def __fspath__(self) -> _AnyStr_co:
        ...
if sys.version_info >= (3, 10):

    def aiter(__iterable: AsyncIterable[_T]) -> AsyncIterator[_T]:
        ...

    @overload
    async def anext(__i: AsyncIterator[_T]) -> _T:
        ...

    @overload
    async def anext(__i: AsyncIterator[_T], default: _VT) -> _T | _VT:
        ...

def delattr(__obj: Any, __name: str) -> None:
    ...

def dir(__o: object=...) -> list[str]:
    ...

@overload
def divmod(__x: SupportsDivMod[_T_contra, _T_co], __y: _T_contra) -> _T_co:
    ...

@overload
def divmod(__x: _T_contra, __y: SupportsRDivMod[_T_contra, _T_co]) -> _T_co:
    ...

def eval(__source: str | bytes | CodeType, __globals: dict[str, Any] | None=..., __locals: Mapping[str, Any] | None=...) -> Any:
    ...

def exec(__source: str | bytes | CodeType, __globals: dict[str, Any] | None=..., __locals: Mapping[str, Any] | None=...) -> Any:
    ...

class filter(Iterator[_T], Generic[_T]):

    @overload
    def __init__(self, __function: None, __iterable: Iterable[_T | None]) -> None:
        ...

    @overload
    def __init__(self, __function: Callable[[_T], Any], __iterable: Iterable[_T]) -> None:
        ...

    def __iter__(self) -> Iterator[_T]:
        ...

    def __next__(self) -> _T:
        ...

@overload
def getattr(__o: object, name: str) -> Any:
    ...

@overload
def getattr(__o: object, name: str, __default: None) -> Any | None:
    ...

@overload
def getattr(__o: object, name: str, __default: bool) -> Any | bool:
    ...

@overload
def getattr(__o: object, name: str, __default: _T) -> Any | _T:
    ...

def globals() -> dict[str, Any]:
    ...

def hasattr(__obj: object, __name: str) -> bool:
    ...

def hash(__obj: object) -> int:
    ...

def help(*args: Any, **kwds: Any) -> None:
    ...

def hex(__number: int | SupportsIndex) -> str:
    ...

def id(__obj: object) -> int:
    ...

def input(__prompt: Any=...) -> str:
    ...

@overload
def iter(__iterable: Iterable[_T]) -> Iterator[_T]:
    ...

@overload
def iter(__function: Callable[[], _T | None], __sentinel: None) -> Iterator[_T]:
    ...

@overload
def iter(__function: Callable[[], _T], __sentinel: Any) -> Iterator[_T]:
    ...
if sys.version_info >= (3, 10):

    def isinstance(__obj: object, __class_or_tuple: type | types.UnionType | Tuple[type | types.UnionType | Tuple[Any, ...], ...]) -> bool:
        ...

    def issubclass(__cls: type, __class_or_tuple: type | types.UnionType | Tuple[type | types.UnionType | Tuple[Any, ...], ...]) -> bool:
        ...
else:

    def isinstance(__obj: object, __class_or_tuple: type | Tuple[type | Tuple[Any, ...], ...]) -> bool:
        ...

    def issubclass(__cls: type, __class_or_tuple: type | Tuple[type | Tuple[Any, ...], ...]) -> bool:
        ...

def len(__obj: Sized) -> int:
    ...

def locals() -> dict[str, Any]:
    ...

class map(Iterator[_S], Generic[_S]):

    @overload
    def __init__(self, __func: Callable[[_T1], _S], __iter1: Iterable[_T1]) -> None:
        ...

    @overload
    def __init__(self, __func: Callable[[_T1, _T2], _S], __iter1: Iterable[_T1], __iter2: Iterable[_T2]) -> None:
        ...

    @overload
    def __init__(self, __func: Callable[[_T1, _T2, _T3], _S], __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3]) -> None:
        ...

    @overload
    def __init__(self, __func: Callable[[_T1, _T2, _T3, _T4], _S], __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4]) -> None:
        ...

    @overload
    def __init__(self, __func: Callable[[_T1, _T2, _T3, _T4, _T5], _S], __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4], __iter5: Iterable[_T5]) -> None:
        ...

    @overload
    def __init__(self, __func: Callable[..., _S], __iter1: Iterable[Any], __iter2: Iterable[Any], __iter3: Iterable[Any], __iter4: Iterable[Any], __iter5: Iterable[Any], __iter6: Iterable[Any], *iterables: Iterable[Any]) -> None:
        ...

    def __iter__(self) -> Iterator[_S]:
        ...

    def __next__(self) -> _S:
        ...

@overload
def max(__arg1: SupportsLessThanT, __arg2: SupportsLessThanT, *_args: SupportsLessThanT, key: None=...) -> SupportsLessThanT:
    ...

@overload
def max(__arg1: _T, __arg2: _T, *_args: _T, key: Callable[[_T], SupportsLessThan]) -> _T:
    ...

@overload
def max(__iterable: Iterable[SupportsLessThanT], *, key: None=...) -> SupportsLessThanT:
    ...

@overload
def max(__iterable: Iterable[_T], *, key: Callable[[_T], SupportsLessThan]) -> _T:
    ...

@overload
def max(__iterable: Iterable[SupportsLessThanT], *, key: None=..., default: _T) -> SupportsLessThanT | _T:
    ...

@overload
def max(__iterable: Iterable[_T1], *, key: Callable[[_T1], SupportsLessThan], default: _T2) -> _T1 | _T2:
    ...

@overload
def min(__arg1: SupportsLessThanT, __arg2: SupportsLessThanT, *_args: SupportsLessThanT, key: None=...) -> SupportsLessThanT:
    ...

@overload
def min(__arg1: _T, __arg2: _T, *_args: _T, key: Callable[[_T], SupportsLessThan]) -> _T:
    ...

@overload
def min(__iterable: Iterable[SupportsLessThanT], *, key: None=...) -> SupportsLessThanT:
    ...

@overload
def min(__iterable: Iterable[_T], *, key: Callable[[_T], SupportsLessThan]) -> _T:
    ...

@overload
def min(__iterable: Iterable[SupportsLessThanT], *, key: None=..., default: _T) -> SupportsLessThanT | _T:
    ...

@overload
def min(__iterable: Iterable[_T1], *, key: Callable[[_T1], SupportsLessThan], default: _T2) -> _T1 | _T2:
    ...

@overload
def next(__i: Iterator[_T]) -> _T:
    ...

@overload
def next(__i: Iterator[_T], default: _VT) -> _T | _VT:
    ...

def oct(__number: int | SupportsIndex) -> str:
    ...
_OpenFile = Union[StrOrBytesPath, int]
_Opener = Callable[[str, int], int]

@overload
def open(file: _OpenFile, mode: OpenTextMode=..., buffering: int=..., encoding: str | None=..., errors: str | None=..., newline: str | None=..., closefd: bool=..., opener: _Opener | None=...) -> TextIO:
    ...

@overload
def open(file: _OpenFile, mode: OpenBinaryMode, buffering: int=..., encoding: None=..., errors: None=..., newline: None=..., closefd: bool=..., opener: _Opener | None=...) -> BinaryIO:
    ...

@overload
def open(file: _OpenFile, mode: str, buffering: int=..., encoding: str | None=..., errors: str | None=..., newline: str | None=..., closefd: bool=..., opener: _Opener | None=...) -> IO[Any]:
    ...

def ord(__c: str | bytes) -> int:
    ...

def print(*values: object, sep: str | None=..., end: str | None=..., file: SupportsWrite[str] | None=..., flush: bool=...) -> None:
    ...
_E = TypeVar('_E', contravariant=True)
_M = TypeVar('_M', contravariant=True)

class _SupportsPow2(Protocol[_E, _T_co]):

    def __pow__(self, __other: _E) -> _T_co:
        ...

class _SupportsPow3(Protocol[_E, _M, _T_co]):

    def __pow__(self, __other: _E, __modulo: _M) -> _T_co:
        ...
if sys.version_info >= (3, 8):

    @overload
    def pow(base: int, exp: int, mod: None=...) -> Any:
        ...

    @overload
    def pow(base: int, exp: int, mod: int) -> int:
        ...

    @overload
    def pow(base: float, exp: float, mod: None=...) -> float:
        ...

    @overload
    def pow(base: _SupportsPow2[_E, _T_co], exp: _E) -> _T_co:
        ...

    @overload
    def pow(base: _SupportsPow3[_E, _M, _T_co], exp: _E, mod: _M) -> _T_co:
        ...
else:

    @overload
    def pow(__base: int, __exp: int, __mod: None=...) -> Any:
        ...

    @overload
    def pow(__base: int, __exp: int, __mod: int) -> int:
        ...

    @overload
    def pow(__base: float, __exp: float, __mod: None=...) -> float:
        ...

    @overload
    def pow(__base: _SupportsPow2[_E, _T_co], __exp: _E) -> _T_co:
        ...

    @overload
    def pow(__base: _SupportsPow3[_E, _M, _T_co], __exp: _E, __mod: _M) -> _T_co:
        ...

class reversed(Iterator[_T], Generic[_T]):

    @overload
    def __init__(self, __sequence: Reversible[_T]) -> None:
        ...

    @overload
    def __init__(self, __sequence: SupportsLenAndGetItem[_T]) -> None:
        ...

    def __iter__(self) -> Iterator[_T]:
        ...

    def __next__(self) -> _T:
        ...

def repr(__obj: object) -> str:
    ...

@overload
def round(number: SupportsRound[Any]) -> int:
    ...

@overload
def round(number: SupportsRound[Any], ndigits: None) -> int:
    ...

@overload
def round(number: SupportsRound[_T], ndigits: SupportsIndex) -> _T:
    ...

def setattr(__obj: object, __name: str, __value: Any) -> None:
    ...

@overload
def sorted(__iterable: Iterable[SupportsLessThanT], *, key: None=..., reverse: bool=...) -> list[SupportsLessThanT]:
    ...

@overload
def sorted(__iterable: Iterable[_T], *, key: Callable[[_T], SupportsLessThan], reverse: bool=...) -> list[_T]:
    ...
if sys.version_info >= (3, 8):

    @overload
    def sum(__iterable: Iterable[_T]) -> _T | int:
        ...

    @overload
    def sum(__iterable: Iterable[_T], start: _S) -> _T | _S:
        ...
else:

    @overload
    def sum(__iterable: Iterable[_T]) -> _T | int:
        ...

    @overload
    def sum(__iterable: Iterable[_T], __start: _S) -> _T | _S:
        ...

class zip(Iterator[_T_co], Generic[_T_co]):

    @overload
    def __new__(cls, __iter1: Iterable[_T1]) -> zip[Tuple[_T1]]:
        ...

    @overload
    def __new__(cls, __iter1: Iterable[_T1], __iter2: Iterable[_T2]) -> zip[Tuple[_T1, _T2]]:
        ...

    @overload
    def __new__(cls, __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3]) -> zip[Tuple[_T1, _T2, _T3]]:
        ...

    @overload
    def __new__(cls, __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4]) -> zip[Tuple[_T1, _T2, _T3, _T4]]:
        ...

    @overload
    def __new__(cls, __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4], __iter5: Iterable[_T5]) -> zip[Tuple[_T1, _T2, _T3, _T4, _T5]]:
        ...

    @overload
    def __new__(cls, __iter1: Iterable[Any], __iter2: Iterable[Any], __iter3: Iterable[Any], __iter4: Iterable[Any], __iter5: Iterable[Any], __iter6: Iterable[Any], *iterables: Iterable[Any]) -> zip[Tuple[Any, ...]]:
        ...

    def __iter__(self) -> Iterator[_T_co]:
        ...

    def __next__(self) -> _T_co:
        ...

def __import__(name: str, globals: Mapping[str, Any] | None=..., locals: Mapping[str, Any] | None=..., fromlist: Sequence[str]=..., level: int=...) -> Any:
    ...

class ellipsis:
    ...
Ellipsis: ellipsis

class BaseException(object):
    args: Tuple[Any, ...]
    __cause__: BaseException | None
    __context__: BaseException | None
    __suppress_context__: bool
    __traceback__: TracebackType | None

    def __init__(self, *args: object) -> None:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def with_traceback(self: _TBE, tb: TracebackType | None) -> _TBE:
        ...

class GeneratorExit(BaseException):
    ...

class KeyboardInterrupt(BaseException):
    ...

class SystemExit(BaseException):
    code: int

class Exception(BaseException):
    ...

class StopIteration(Exception):
    value: Any
_StandardError = Exception

class OSError(Exception):
    errno: int
    strerror: str
    filename: Any
    filename2: Any
    if sys.platform == 'win32':
        winerror: int
if sys.platform == 'win32':
    WindowsError = OSError

class ArithmeticError(_StandardError):
    ...

class AssertionError(_StandardError):
    ...

class AttributeError(_StandardError):
    if sys.version_info >= (3, 10):
        name: str
        obj: object

class EOFError(_StandardError):
    ...

class ImportError(_StandardError):

    def __init__(self, *args: object, name: str | None=..., path: str | None=...) -> None:
        ...
    name: str | None
    path: str | None
    msg: str

class LookupError(_StandardError):
    ...

class MemoryError(_StandardError):
    ...

class NameError(_StandardError):
    if sys.version_info >= (3, 10):
        name: str

class RuntimeError(_StandardError):
    ...

class StopAsyncIteration(Exception):
    value: Any

class SyntaxError(_StandardError):
    msg: str
    lineno: int | None
    offset: int | None
    text: str | None
    filename: str | None
    if sys.version_info >= (3, 10):
        end_lineno: int | None
        end_offset: int | None

class TypeError(_StandardError):
    ...

class ValueError(_StandardError):
    ...

class FloatingPointError(ArithmeticError):
    ...

class OverflowError(ArithmeticError):
    ...

class ZeroDivisionError(ArithmeticError):
    ...

class IndexError(LookupError):
    ...

class KeyError(LookupError):
    ...

class NotImplementedError(RuntimeError):
    ...

class IndentationError(SyntaxError):
    ...

class TabError(IndentationError):
    ...