from dataclasses import dataclass

@dataclass
class CannyCfg:
    blur_kernel: int = 5
    low_thresh: int = 50
    high_thresh: int = 150

@dataclass
class HoughCfg:
    rho: float = 2.0
    theta: float = 3.14159 / 180.0
    threshold: int = 100
    min_line_len: int = 40
    max_line_gap: int = 5

@dataclass
class DrawCfg:
    line_color: tuple[int, int, int] = (255, 0, 0)  # BGR
    line_thickness: int = 10
    blend_alpha: float = 0.8
    blend_beta: float = 1.0
    blend_gamma: float = 1.0

@dataclass
class ROIConfig:
    
    bottom_left: tuple[float, float] = (0.1, 1.0)
    top_mid: tuple[float, float] = (0.5, 0.6)
    bottom_right: tuple[float, float] = (0.9, 1.0)

@dataclass
class SmoothCfg:
    ema_alpha: float = 0.2 

@dataclass
class AppCfg:
    canny: CannyCfg = CannyCfg()
    hough: HoughCfg = HoughCfg()
    draw: DrawCfg = DrawCfg()
    roi: ROIConfig = ROIConfig()
    smooth: SmoothCfg = SmoothCfg()
