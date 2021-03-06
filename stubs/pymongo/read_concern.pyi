from typing import Any, Dict, Optional


class ReadConcern(object):
    def __init__(self, level: Optional[str] = ...) -> None: ...
    @property
    def level(self) -> str: ...
    @property
    def ok_for_legacy(self) -> bool: ...
    @property
    def document(self) -> Dict[str, str]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __repr__(self) -> str: ...
DEFAULT_READ_CONCERN: ReadConcern = ...
