import cv2
import numpy as np
from ..config import HoughCfg

def hough_lines(cropped_canny: np.ndarray, cfg: HoughCfg):
    return cv2.HoughLinesP(
        cropped_canny,
        rho=cfg.rho,
        theta=cfg.theta,
        threshold=cfg.threshold,
        minLineLength=cfg.min_line_len,
        maxLineGap=cfg.max_line_gap,
    )
