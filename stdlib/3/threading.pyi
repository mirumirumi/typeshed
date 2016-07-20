# Stubs for threading

# NOTE: These are incomplete!

from typing import Any, Optional, Callable, TypeVar, Union, Mapping, Sequence, List

class Thread:
    name = ...  # type: str
    ident = 0
    daemon = False

    def __init__(self, group: Any = ..., target: Callable[..., Any] = ...,
                 name: str = ..., args: Sequence[Any] = ...,
                 kwargs: Mapping[str, Any] = ..., daemon: bool = ...) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def join(self, timeout: float = ...) -> None: ...
    def is_alive(self) -> bool: ...

    # Legacy methods
    def getName(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def isDaemon(self) -> bool: ...
    def setDaemon(self, daemon: bool) -> None: ...

class Timer(Thread):
    def __init__(self, interval: float, function: Callable[..., Any],
                 args: Sequence[Any] = ...,
                 kwargs: Mapping[str, Any] = ...) -> None: ...
    def cancel(self) -> None : ...

class local(Any): ...

class Event:
    def is_set(self) -> bool: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    # TODO can it return None?
    def wait(self, timeout: float = ...) -> bool: ...

class Lock:
    def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    def release(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, *args): ...

class RLock:
    def acquire(self, blocking: bool = ...,
                timeout: float = ...) -> Optional[bool]: ...
    def release(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, *args): ...

_T = TypeVar('_T')

class Condition:
    def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    def release(self) -> None: ...
    def notify(self, n: int = ...) -> None: ...
    def notify_all(self) -> None: ...
    def wait(self, timeout: float = ...) -> bool: ...
    def wait_for(self, predicate: Callable[[], _T], timeout: float = ...) -> Union[_T, bool]: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, *args): ...

def current_thread() -> Thread: ...
def active_count() -> int: ...
def enumerate() -> List[Thread]: ...
def main_thread() -> Thread: ...
