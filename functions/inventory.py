"""Simple global inventory singleton shared across floors.

API (Inventory methods):
- add(name, quantity=1, attrs=None) -> None
- remove(name, quantity=1) -> bool
- has(name) -> bool
- get_count(name) -> int
- list_items() -> dict
- save_to_file(path) -> bool
- load_from_file(path) -> bool

This module exposes a process-global `inventory` instance you can import from
any floor or module: `from functions.inventory import inventory`
"""
from __future__ import annotations

import json
import threading
from typing import Dict, Any


class Inventory:
    """A tiny thread-safe inventory suitable for a text adventure.

    Items are stored as a mapping: name -> {"count": int, "attrs": dict}
    """

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._items: Dict[str, Dict[str, Any]] = {}

    def add(self, name: str, quantity: int = 1, attrs: Dict[str, Any] | None = None) -> None:
        """Add `quantity` of `name`. If attrs are provided and the item exists,
        attrs will be merged (new keys added, existing keys overwritten).
        """
        if quantity <= 0:
            return

        with self._lock:
            entry = self._items.get(name)
            if entry is None:
                self._items[name] = {"count": quantity, "attrs": dict(attrs) if attrs else {}}
            else:
                entry["count"] += quantity
                if attrs:
                    entry["attrs"].update(attrs)

    def remove(self, name: str, quantity: int = 1) -> bool:
        """Remove up to `quantity` of `name`. Returns True if removal succeeded
        (enough items existed), False otherwise.
        """
        if quantity <= 0:
            return False

        with self._lock:
            entry = self._items.get(name)
            if not entry or entry["count"] < quantity:
                return False
            entry["count"] -= quantity
            if entry["count"] <= 0:
                del self._items[name]
            return True

    def has(self, name: str) -> bool:
        with self._lock:
            return name in self._items and self._items[name]["count"] > 0

    def get_count(self, name: str) -> int:
        with self._lock:
            entry = self._items.get(name)
            return entry["count"] if entry else 0

    def list_items(self) -> Dict[str, Dict[str, Any]]:
        """Return a shallow copy of the inventory state."""
        with self._lock:
            return {k: {"count": v["count"], "attrs": dict(v["attrs"])} for k, v in self._items.items()}

    def to_dict(self) -> Dict[str, Any]:
        with self._lock:
            return {"version": 1, "items": self.list_items()}

    def save_to_file(self, path: str) -> bool:
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
            return True
        except Exception:
            return False

    def load_from_file(self, path: str) -> bool:
        try:
            with open(path, "r", encoding="utf-8") as f:
                payload = json.load(f)
            items = payload.get("items", {})
            with self._lock:
                # replace current state with loaded state
                self._items = {k: {"count": int(v.get("count", 0)), "attrs": dict(v.get("attrs", {}))} for k, v in items.items()}
            return True
        except Exception:
            return False

    # convenience
    def save(self, path: str) -> bool:
        return self.save_to_file(path)

    def load(self, path: str) -> bool:
        return self.load_from_file(path)

    def __repr__(self) -> str:  # pragma: no cover - tiny helper
        return f"Inventory({self.list_items()})"


# module-level singleton; import this from floors and modules
inventory = Inventory()
