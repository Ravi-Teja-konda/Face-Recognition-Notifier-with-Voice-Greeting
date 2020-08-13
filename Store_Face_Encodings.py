import face_recognition
import pickle
import os
from tqdm import tqdm

#######################################################################################################################################

all_face_encodings = {}


print("Loading known face encodings... \nPlease wait..It may take some momemts....")


images = os.listdir('images')

for image in tqdm(images,ncols=100):
    # load the image
    #print(image)
    known_image = face_recognition.load_image_file("images/" + image)

    # Get the face encodings for the known images
    #time.sleep(1)
    all_face_encodings[str(image[:-4])] = face_recognition.face_encodings(known_image)[0]

with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)
