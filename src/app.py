import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

def speak(sentence):
    print(sentence)
    language = 'en'
    speech = gTTS(text = sentence, lang = language, slow = False)

    speech.save("./sounds/speech.mp3")
    playsound("./sounds/speech.mp3")



# open webcam
video = cv2.VideoCapture(0)

labels = []

while True:
    ret, frame = video.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Real-time object detection", output_image)

    for i in label:
        if i in labels:
            pass
        else:
            labels.append(i)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

i = 0
new_sentence = []
for label in labels:
    if i == 0:
        new_sentence.append(f"I see a {label} and,")
        i += 1
    else:
        new_sentence.append(f"a {label}")
    
    i += 1

speak(" ".join(new_sentence))