import numpy as np
from src.vision.edges import canny
from src.config import CannyCfg

def test_canny_runs():
    img = (np.random.rand(64,64,3)*255).astype("uint8")
    out = canny(img, CannyCfg())
    assert out.shape[:2] == (64,64)
