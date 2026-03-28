import cv2
from Detection.face_detector import face_detect
from Detection.eye_detector import detect_eyes
from Detection.eye_detector import calculate_ear
import time
import winsound
from playsound import playsound
import threading

webcam = cv2.VideoCapture(0)
counter = 0
limit = 20
voice_played = False

def play_voice():
    playsound('voice.wav')

while True:
   success, frame = webcam.read()
   timestamp = int(time.time() * 1000)
   faces = face_detect(frame)
   for face in faces:
      x,y,w,h = face
      cv2.rectangle(frame, (x,y), (x+w,y+h),  color=(0,255,0), thickness=2)
   
   eyes = detect_eyes(frame, timestamp)
   if eyes:
      left_eye_points, right_eye_points = eyes

      for (x,y) in left_eye_points:
         cv2.circle(frame, (x,y), 3, (0,0,255), thickness=-1)
      for (x, y) in right_eye_points:
         cv2.circle(frame, (x, y), 3, (0,0,255), thickness=-1)
   
   ear = calculate_ear(left_eye_points)
   

   EAR_THRESHOLD = 0.15

   if ear < EAR_THRESHOLD:
      counter = counter + 1
   else:
      counter = 0
   
   cv2.rectangle(frame, (20,20), (350,130), (0,0,0), -1)
   cv2.putText(frame, "DRIVER STATUS", (30,50),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
   if counter > limit:
    status = "Drowsy"
    color = (0,0,255)
   else:
    status = "Awake"
    color = (0,255,0)
   
   if counter > limit:
      cv2.putText(frame, f'Status: {status}', (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(0,0,255), thickness=2)
   else:
      cv2.putText(frame, f'Status: {status}', (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(0,255,0), thickness=2)
      

   if counter > limit and voice_played == False:
      threading.Thread(target=play_voice).start()
      voice_played = True
      winsound.Beep(500, 150)
   elif ear >= EAR_THRESHOLD:
       voice_played = False
   

   cv2.imshow('title', frame)

   if cv2.waitKey(1) & 0xFF == ord('q'):
    break