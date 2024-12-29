import cv2

from ultralytics import solutions

cap = cv2.VideoCapture(r"D:\py_xiangmu\学生行为检测\测试视频2.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Define region points
# region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)] # Pass region as list

# pass region as dictionary
region_points = {
    "region-01": [(0, 0), (950, 0), (950, 500), (0, 500)]
    # "region-02": [(640, 640), (780, 640), (780, 720), (640, 720)],
}

# Video writer
video_writer = cv2.VideoWriter("region_counting.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init RegionCounter
region = solutions.RegionCounter(
    show=True,
    region=region_points,
    model=r"D:\py_xiangmu\学生行为检测\yolo11n.pt",
    iou=0.3,
    # conf=0.7,
)
# Process vide2
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    im0 = region.count(im0)
    video_writer.write(im0)

cap.release()
video_writer.release()
cv2.destroyAllWindows()