import cv2
import mediapipe as mp
from scipy.spatial import distance as dist

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# eye landmark indices (same rahenge)
left_eye = [33, 160, 158, 133, 153, 144]
right_eye = [362, 385, 387, 263, 373, 380]

# ----------- SETUP DETECTOR -----------

BaseOptions = python.BaseOptions
FaceLandmarker = vision.FaceLandmarker
FaceLandmarkerOptions = vision.FaceLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="models/face_landmarker.task"),
    running_mode=VisionRunningMode.VIDEO,
    num_faces=1
)

detector = FaceLandmarker.create_from_options(options)

# ----------- FUNCTION -----------

def detect_eyes(frame, timestamp):
    left_eye_points = []
    right_eye_points = []

    # convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # convert to mediapipe image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # detect
    result = detector.detect_for_video(mp_image, timestamp)

    if result.face_landmarks:
        landmarks = result.face_landmarks[0]
        height, width, _ = frame.shape

        for idx in left_eye:
            landmark = landmarks[idx]
            x = int(landmark.x * width)
            y = int(landmark.y * height)
            left_eye_points.append((x, y))

        for idx in right_eye:
            landmark = landmarks[idx]
            x = int(landmark.x * width)
            y = int(landmark.y * height)
            right_eye_points.append((x, y))

        return left_eye_points, right_eye_points
    else:
        return None

def calculate_ear(eye):
    vertical1 = dist.euclidean(eye[1], eye[5])
    vertical2 = dist.euclidean(eye[2], eye[4])

    horizontal1 = dist.euclidean(eye[0], eye[3])

    EAR = (vertical1 + vertical2) / (2.0*horizontal1)
    return EAR