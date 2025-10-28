import cv2
import numpy as np
from ..config import CannyCfg
from ..utils import to_gray

def canny(img: np.ndarray, cfg: CannyCfg) -> np.ndarray:
    gray = to_gray(img)
    blur = cv2.GaussianBlur(gray, (cfg.blur_kernel, cfg.blur_kernel), 0)
    return cv2.Canny(blur, cfg.low_thresh, cfg.high_thresh)
