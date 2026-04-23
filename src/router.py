from fastapi import APIRouter, UploadFile
import cv2
import mediapipe as mp



ROUTER = APIRouter(prefix="/API", tags=["Rooms"])

def to_file(file):
    with open("img/" + file.filename, "wb") as f:
        f.write(file.file.read())

async def find_hands(file_path: str):
    detector = None
    try:
        BaseOptions = mp.tasks.BaseOptions
        HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
        VisionRunningMode = mp.tasks.vision.RunningMode

        options = HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path="./hand_landmarker.task"),
            running_mode=VisionRunningMode.IMAGE,
            num_hands=10,
            min_hand_detection_confidence=0.5,
            min_hand_presence_confidence=0.5,
            min_tracking_confidence=0.5
        )
        detector = mp.tasks.vision.HandLandmarker.create_from_options(options)
        img = cv2.imread("img/" + file_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
        detection_result = detector.detect(mp_image)
        connections = [
                    (0, 1), (1, 2), (2, 3), (3, 4),
                    (0, 5), (5, 6), (6, 7), (7, 8),
                    (0, 9), (9, 10), (10, 11), (11, 12),
                    (0, 13), (13, 14), (14, 15), (15, 16),
                    (0, 17), (17, 18), (18, 19), (19, 20),
                    (5, 9), (9, 13), (13, 17)
                ]
        if detection_result.hand_landmarks:
            for hand_landmarks in detection_result.hand_landmarks:
                h, w, _ = img.shape
                
                for landmark in hand_landmarks:
                    x, y = int(landmark.x * w), int(landmark.y * h)
                    cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
                    
                for connection in connections:
                    start = hand_landmarks[connection[0]]
                    end = hand_landmarks[connection[1]]
                    cv2.line(img, 
                            (int(start.x * w), int(start.y * h)),
                            (int(end.x * w), int(end.y * h)),
                            (255, 0, 0), 2)
    finally:
        if detector:
            detector.close()
    print(f"Найдено рук: {len(detection_result.hand_landmarks) if detection_result.hand_landmarks else 0}")
    cv2.imwrite("result/" + file_path, img)
    return len(detection_result.hand_landmarks) if detection_result.hand_landmarks else 0

@ROUTER.post("/IMG")
async def upload_file(file: UploadFile):
    to_file(file)
    hands_cou = await find_hands(file.filename)
    print(type(hands_cou))
    return {"msg": "ok",
            "hands": hands_cou}