import threading
import signal
import time
import functions.save as gameSave
import sys
from typing import Tuple, Optional

# /c:/Users/autis/InfiniteHallway/functions/playtimetracker.py


class PlaytimeTracker:
    """
    Thread-based playtime tracker counting seconds and minutes (no hours).

    Usage:
      tracker = PlaytimeTracker()
      thread = tracker.start()    # starts background thread
      ... query tracker.minutes/seconds ...
      tracker.stop()              # stop background thread
    """

    def __init__(self) -> None:
        self.minutes: int = 0
        self.seconds: int = 0
        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()

    def _run(self) -> None:
        while not self._stop_event.is_set():
            time.sleep(1)
            self.seconds += 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1

    def start(self) -> threading.Thread:
        """Start the tracker running in a background daemon thread."""
        if self._thread and self._thread.is_alive():
            return self._thread
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()
        return self._thread

    def stop(self, timeout: Optional[float] = None) -> None:
        """Stop the background thread and wait for it to finish."""
        if not self._thread:
            return
        self._stop_event.set()
        self._thread.join(timeout)
        self._thread = None

    def reset(self) -> None:
        """Reset minutes and seconds to zero. Does not stop the tracker."""
        self.minutes = 0
        self.seconds = 0

    def get(self) -> Tuple[int, int]:
        """Return (minutes, seconds)."""
        return self.minutes, self.seconds

    def formatted(self) -> str:
        """Return a human-readable string like '5:03' (minutes:seconds)."""
        return f"{self.minutes}:{self.seconds:02d}"


def start_playtime_tracker() -> PlaytimeTracker:
    """
    Convenience function: create and start a PlaytimeTracker, returning the instance.
    Call await tracker.stop() to stop it.
    """
    tracker = PlaytimeTracker()

    # Initialize tracker from existing save so playtime accumulates across sessions.
    try:
        existing = gameSave.load()
    except Exception:
        existing = {}

    try:
        saved_minutes = int(existing.get('playtime_minutes', 0))
    except Exception:
        saved_minutes = 0
    try:
        saved_seconds = int(existing.get('playtime_seconds', 0))
    except Exception:
        saved_seconds = 0

    total_seconds = saved_minutes * 60 + saved_seconds
    tracker.minutes = total_seconds // 60
    tracker.seconds = total_seconds % 60

    tracker.start()

    # Register a SIGINT (KeyboardInterrupt) handler that saves playtime to the
    # game's save data. We create a closure capturing `tracker` so the handler
    # can read the current playtime and persist it to disk.
    def _make_sigint_handler(tracker_ref: PlaytimeTracker):
        def _handler(signum, frame):
            try:
                saveData = gameSave.load()
            except Exception:
                saveData = {}

            try:
                minutes, seconds = tracker_ref.get()
            except Exception:
                minutes, seconds = 0, 0

            saveData['playtime_minutes'] = minutes
            saveData['playtime_seconds'] = seconds
            try:
                gameSave.save(saveData)
                print("Playtime saved to save file.")
            except Exception as e:
                print(f"Failed to save playtime: {e}")

            # Re-raise KeyboardInterrupt so existing application handlers run.
            raise KeyboardInterrupt

        return _handler

    try:
        signal.signal(signal.SIGINT, _make_sigint_handler(tracker))
    except Exception:
        # If the environment doesn't support signal handling, silently continue.
        pass

    return tracker