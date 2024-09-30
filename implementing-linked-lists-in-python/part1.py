from __future__ import annotations
from typing import Any, Optional


class SLLNode:
    def __init__(self, data: Any, next: Optional[SLLNode] = None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data}"
