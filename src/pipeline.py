import cv2
import numpy as np
from .config import AppCfg
from .vision.edges import canny
from .vision.roi import apply_roi
from .vision.hough import hough_lines
from .vision.lines import average_slope_intercept, draw_lines
from .vision.smoothing import EMALineSmoother
from .utils import blend

class LanePipeline:
    def __init__(self, cfg: AppCfg | None = None):
        self.cfg = cfg or AppCfg()
        self.smoother = EMALineSmoother(alpha=self.cfg.smooth.ema_alpha)

    def process_frame(self, frame: np.ndarray) -> np.ndarray:
        edges = canny(frame, self.cfg.canny)
        masked = apply_roi(edges, self.cfg.roi)
        lines = hough_lines(masked, self.cfg.hough)
        averaged = average_slope_intercept(frame, lines)
        smoothed = self.smoother.update(averaged)
        overlay = draw_lines(frame, smoothed, self.cfg.draw)
        return blend(frame, overlay,
                     self.cfg.draw.blend_alpha,
                     self.cfg.draw.blend_beta,
                     self.cfg.draw.blend_gamma)
