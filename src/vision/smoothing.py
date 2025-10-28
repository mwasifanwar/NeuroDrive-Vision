from collections import deque

class EMALineSmoother:
    """Keeps an EMA of left/right lane points (x1,y1,x2,y2)."""
    def __init__(self, alpha: float = 0.2):
        self.alpha = alpha
        self.state_left = None
        self.state_right = None

    def _ema(self, prev, new):
        if prev is None:
            return new
        return [self.alpha*n + (1-self.alpha)*p for p,n in zip(prev, new)]

    def update(self, pts):
        if pts is None:
            return None
        out = []
        # classify left/right by x1 vs x2 (slope sign is already used upstream)
        for p in pts:
            if len(out) == 0:
                self.state_left = self._ema(self.state_left, p)
                out.append([int(v) for v in self.state_left])
            else:
                self.state_right = self._ema(self.state_right, p)
                out.append([int(v) for v in self.state_right])
        return out
