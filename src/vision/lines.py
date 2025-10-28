import numpy as np
import cv2
from ..config import DrawCfg
from ..utils import safe_int

def _make_points(image: np.ndarray, slope: float, intercept: float) -> list[int]:
    h = image.shape[0]
    y1 = h                         # bottom
    y2 = safe_int(h * 0.6)         # 60% height
    if abs(slope) < 1e-6:          # avoid div-by-zero
        return [0, y1, 0, y2]
    x1 = safe_int((y1 - intercept) / slope)
    x2 = safe_int((y2 - intercept) / slope)
    return [x1, y1, x2, y2]

def average_slope_intercept(image: np.ndarray, lines) -> list[list[int]] | None:
    if lines is None or len(lines) == 0:
        return None
    left, right = [], []
    for line in lines:
        for x1,y1,x2,y2 in line:
            if x2 == x1:
                continue
            slope = (y2 - y1) / (x2 - x1 + 1e-6)
            intercept = y1 - slope * x1
            if slope < 0:
                left.append((slope, intercept))
            else:
                right.append((slope, intercept))
    if not left and not right:
        return None
    out = []
    if left:
        l = np.mean(left, axis=0)
        out.append(_make_points(image, l[0], l[1]))
    if right:
        r = np.mean(right, axis=0)
        out.append(_make_points(image, r[0], r[1]))
    return out if out else None

def draw_lines(base: np.ndarray, lines_pts: list[list[int]] | None, cfg: DrawCfg) -> np.ndarray:
    overlay = np.zeros_like(base)
    if lines_pts:
        for x1,y1,x2,y2 in lines_pts:
            cv2.line(overlay, (x1,y1), (x2,y2), cfg.line_color, cfg.line_thickness)
    return overlay
