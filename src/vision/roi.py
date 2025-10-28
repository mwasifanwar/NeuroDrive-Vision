import numpy as np
import cv2
from ..config import ROIConfig

def relative_triangle(mask_shape: tuple[int,int], cfg: ROIConfig) -> np.ndarray:
    h, w = mask_shape
    p1 = (int(cfg.bottom_left[0]*w),  int(cfg.bottom_left[1]*h))
    p2 = (int(cfg.top_mid[0]*w),      int(cfg.top_mid[1]*h))
    p3 = (int(cfg.bottom_right[0]*w), int(cfg.bottom_right[1]*h))
    return np.array([[p1, p2, p3]], dtype=np.int32)

def apply_roi(canny_img: np.ndarray, cfg: ROIConfig) -> np.ndarray:
    mask = np.zeros_like(canny_img)
    tri = relative_triangle(canny_img.shape[0:2], cfg)
    cv2.fillPoly(mask, tri, 255)
    return cv2.bitwise_and(canny_img, mask)
