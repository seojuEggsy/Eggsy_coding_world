import cv2
import torch
from torchvision import transforms
from yolov5.models.experimental import attempt_load
from yolov5.utils.datasets import letterbox
from yolov5.utils.general import non_max_suppression, scale_coords
from yolov5.utils.plots import plot_one_box
from yolov5.utils.torch_utils import select_device

# 객체 탐지 함수
def detect(img, model, device):
    # 이미지 전처리
    img_size = 640
    img0 = img.copy()
    img = letterbox(img, img_size, stride=32)[0]
    img = img[:, :, ::-1].transpose(2, 0, 1)
    img = np.ascontiguousarray(img)
    img = torch.from_numpy(img).to(device)
    img = img.float() / 255.0
    img = img.unsqueeze(0)

    # 모델 추론
    pred = model(img)[0]

    # 탐지 결과 후처리
    pred = non_max_suppression(pred, conf_thres=0.4, iou_thres=0.5)
    for i, det in enumerate(pred):
        if len(det):
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()
            for *xyxy, conf, cls in reversed(det):
                label = f'{model.names[int(cls)]} {conf:.2f}'
                plot_one_box(xyxy, img0, label=label, color=(0, 255, 0), line_thickness=3)

    return img0

# 이미지 경로 지정
img_path = "image.jpg"

# 모델 로드
weights_path = "yolov5s.pt"
model = attempt_load(weights_path, map_location=torch.device('cpu')).autoshape()

# 장치 설정
device = select_device('cpu')

# 이미지 로드
img = cv2.imread(img_path)

# 객체 탐지
img_detected = detect(img, model, device)

# 탐지 결과 출력
cv2.imshow("Detection Results", img_detected)
cv2.waitKey(0)
cv2.destroyAllWindows()
