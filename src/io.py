import cv2
from typing import Generator, Optional

def video_reader(path: str) -> Generator[tuple[bool, Optional[cv2.Mat]], None, None]:
    cap = cv2.VideoCapture(path)
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            yield ok, frame
    finally:
        cap.release()

def video_writer(path: str, fps: float, size: tuple[int,int]) -> cv2.VideoWriter:
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    return cv2.VideoWriter(path, fourcc, fps, size)
