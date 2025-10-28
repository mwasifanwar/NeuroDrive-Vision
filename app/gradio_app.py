import gradio as gr
import cv2, numpy as np, tempfile, os
from ..src.pipeline import LanePipeline

pipe = LanePipeline()

def run_image(img: np.ndarray):
    bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    out = pipe.process_frame(bgr)
    return cv2.cvtColor(out, cv2.COLOR_BGR2RGB)

def run_video(video):
    cap = cv2.VideoCapture(video)
    fps = cap.get(cv2.CAP_PROP_FPS) or 24
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fd, path = tempfile.mkstemp(suffix=".mp4")
    os.close(fd)
    writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w,h))
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        out = pipe.process_frame(frame)
        writer.write(out)
    cap.release()
    writer.release()
    return path

with gr.Blocks(title="NeuroDrive Lanes (by mwasifanwar)") as demo:
    gr.Markdown("# 🚗 NeuroDrive Lanes\nUpload an image or video to visualize lane detection.")
    with gr.Tabs():
        with gr.TabItem("Image"):
            in_img = gr.Image(label="Upload image", type="numpy")
            out_img = gr.Image(label="Output", type="numpy")
            in_img.change(run_image, inputs=in_img, outputs=out_img)
        with gr.TabItem("Video"):
            in_vid = gr.Video(label="Upload video")
            out_vid = gr.Video(label="Processed video")
            btn = gr.Button("Process")
            btn.click(run_video, inputs=in_vid, outputs=out_vid)
    gr.Markdown("Made with ❤️ by **mwasifanwar**")

if __name__ == "__main__":
    demo.launch()
