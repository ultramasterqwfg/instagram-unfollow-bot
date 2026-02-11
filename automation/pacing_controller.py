import time
from dataclasses import dataclass

@dataclass
class RateLimit:
    per_second: float = 1.0
    burst: int = 3

class Pacer:
    def __init__(self, limit: RateLimit):
        self.limit = limit
        self._min_interval = 1.0 / max(self.limit.per_second, 0.1)
        self._last = 0.0

    def wait(self) -> None:
        now = time.time()
        elapsed = now - self._last
        if elapsed < self._min_interval:
            time.sleep(self._min_interval - elapsed)
        self._last = time.time()
