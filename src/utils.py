import numpy as np
import cv2

def to_gray(img: np.ndarray) -> np.ndarray:
    if img.ndim == 3:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def safe_int(x: float, default: int = 0) -> int:
    try:
        return int(x)
    except Exception:
        return default

def blend(frame: np.ndarray, overlay: np.ndarray, a: float, b: float, g: float) -> np.ndarray:
    return cv2.addWeighted(frame, a, overlay, b, g)
