# Face Recognition Notifier with Voice Greeting
Face Recognition Notifier is a Python application that uses face recognition to identify known individuals, greet them using voice via gTTS, and send a push notification with the person's name and a timestamped photo to their mobile device. It is built using the face_recognition, cv2, gTTS, and requests libraries.

## Features
- Real-time face recognition
- Personalized voice greeting using Google Text-to-Speech (gTTS)
- Greeting in Telugu language (customizable to other languages)
- Push notifications with an attached image sent to mobile devices
- Timestamped images
- Minimal configuration required

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Face-Recognition-Notifier.git
```

Install required dependencies:
```bash
pip install -r requirements.txt
```

Configure the Send_Push_Notifications function with your Pushover API token and user key:
```
"token": "YOUR TOKEN HERE",
"user": "YOUR USER KEY HERE",
```

Add known faces to the dataset_faces.dat file using the Pickle library.

## Usage
Run the main Python script:

```
python main.py
```

## Future Enhancements
- Add support for multiple cameras
- Integrate with various notification services (e.g., Slack, Discord, or email)
- Improve the user interface for adding and managing known faces
- Add support for more languages in the voice greeting
- Implement a web-based user interface for easier configuration and monitoring

## Contributing
We welcome contributions from the community! Please submit your pull requests, and we'll review them as soon as possible.

## License
This project is licensed under the MIT License.

## References
pip install face_recognition  
https://pypi.org/project/face-recognition/  

pip install gTTS  
https://pypi.org/project/gTTS/  

#### Push over notification service  
for more info  
https://pushover.net/  
  
#### How to use push over notification service :   
https://www.cyberciti.biz/mobile-devices/android/how-to-push-send-message-to-ios-and-android-from-linux-cli/




