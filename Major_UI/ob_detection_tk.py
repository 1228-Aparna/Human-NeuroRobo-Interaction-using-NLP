import cv2
import numpy as np
from gtts import gTTS
from playsound import playsound
# Load YOLOv3-tiny model and coco classes
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Set up webcam
cap = cv2.VideoCapture(0)
# define the colors for different classes
COLORS = np.random.uniform(0, 255, size=(len(classes), 3))
while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break
    # Create a blob from the input frame
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)

    # Pass the blob through the network
    net.setInput(blob)
    layerOutputs = net.forward(["yolo_82", "yolo_94", "yolo_106"])
    objects = []
    # Get the bounding boxes, confidences, and class IDs
    boxes = []
    confidences = []
    classIDs = []
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > 0.5:
                box = detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # Apply non-maxima suppression to suppress weak, overlapping bounding boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Loop over the detections and draw bounding boxes and labels
    if len(idxs) > 0:
        for i in idxs.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
            cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            

    # Show the frame
    cv2.imshow("Object detection", frame)

    # Check if the user wants to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # audio = (text.split(":")[0])
        audio = ("I see a: "+text.split(":")[0])
        tts = gTTS(audio)
        tts.save("audio.mp3")
        playsound("audio.mp3")
        audio = ("I see a: "+text.split(":")[0])
        break
    # audio = "I see " + ", ".join(set(objects))
    # print(audio)
    # tts = gTTS(audio)
    # tts.save("audio.mp3")
    # playsound("audio.mp3")

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()