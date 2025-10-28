import argparse, os, cv2
from ..src.pipeline import LanePipeline
from ..src.io import video_reader, video_writer

def main():
    p = argparse.ArgumentParser(description="Lane detection CLI")
    p.add_argument("--input", required=True, help="Path to video (mp4/avi) or image")
    p.add_argument("--output", default="outputs/out.mp4", help="Output video/image path")
    args = p.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    pipe = LanePipeline()

    if args.input.lower().endswith((".png",".jpg",".jpeg",".bmp",".webp")):
        img = cv2.imread(args.input)
        out = pipe.process_frame(img)
        cv2.imwrite(args.output, out)
        print(f"Saved {args.output}")
        return

    # video path
    cap = cv2.VideoCapture(args.input)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open {args.input}")
    fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    writer = video_writer(args.output, fps, (w,h))

    while True:
        ok, frame = cap.read()
        if not ok:
            break
        out = pipe.process_frame(frame)
        writer.write(out)
    cap.release()
    writer.release()
    print(f"Saved {args.output}")

if __name__ == "__main__":
    main()
