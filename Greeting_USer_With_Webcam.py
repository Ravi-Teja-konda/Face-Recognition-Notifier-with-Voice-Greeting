import face_recognition
import cv2
import numpy as np
from gtts import * 
import os
import time
import pickle
import numpy as np
import datetime
import requests

##########################################################################################################################


def Send_Push_Notifications(Name , Image_File):
    Image_File = 'Webcam_'+str(Image_File)+'.jpg'
    r = requests.post("https://api.pushover.net/1/messages.json", data = {
      "token": "YOUR TOKEN HERE",
      "user": "YOUR USER KEY HERE",
      "message": "\""+"Found : "+str(Name)+" With your Laptop.\n"+"Time :"+ Image_File +"\""
    },
    files = {
      "attachment": ("image.jpg", open(Image_File, "rb"), "image/jpeg")
    })
    print(r.text)



video_capture = cv2.VideoCapture(0)

print("Loading Application..")

with open('/home/ravi/PYTHON/Store_Face_Encodings/dataset_faces.dat', 'rb') as f:
	all_face_encodings = pickle.load(f)

# Create arrays of known face encodings and their names
known_face_encodings =  np.array(list(all_face_encodings.values()))
known_face_names = list(all_face_encodings.keys())


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

print("Loading App Done.")
print("Getting camera Ready..\nRecognizing Face..Please be steady..");

time.sleep(2)

#while True:
    # Grab a single frame of video
ret, frame = video_capture.read()
print("Frame Captured..");

# Resize frame of video to 1/4 size for faster face recognition processing
small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#x = datetime.datetime.now()
#cv2.imwrite('Webcam_'+str(x)+'.jpg',frame)

# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
rgb_small_frame = small_frame[:, :, ::-1]

# Only process every other frame of video to save time
if process_this_frame:
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
        print(face_names)

    face_names_string = " ".join(face_names)
    #print(face_names_string)
    face_names_string = face_names_string.replace("_" ," ")

    #Send_Push_Notifications(str(face_names_string) , x)

    mytext = 'Sueswagatham'+ str(face_names_string)

    # Language in which you want to convert
    language = 'te'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")
    # Playing the converted file
    os.system("mpg321 welcome.mp3")

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    x = datetime.datetime.now()
    cv2.imwrite('Webcam_'+str(x)+'.jpg',frame)
    Send_Push_Notifications(str(face_names_string) , x)







