import cv2
import numpy as np

face_net = cv2.dnn.readNet('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')

age_groups = {
    0: "0-10",
    1: "11-20",
    2: "21-30",
    3: "31-40",
}

def detect_and_predict_age(image):
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

    face_net.setInput(blob)
    detections = face_net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
            (startX, startY, endX, endY) = box.astype("int")

            face = image[startY:endY, startX:endX]
            age = predict_age(face)

            text = f"Age: {age}"
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(image, text, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    return image

def predict_age(face):
    avg_pixel = np.mean(face)
    age_index = int(avg_pixel) % len(age_groups)
    predicted_age = age_groups.get(age_index, "Unknown")
    
    return predicted_age

def process_image(input_path):
    if input_path.isdigit():
        input_path = int(input_path)

    cap = cv2.VideoCapture(input_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detect_and_predict_age(frame)
        cv2.imshow('Age Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage:
# Replace 'input_path' with your image path or '0' for webcam feed
process_image('0')
