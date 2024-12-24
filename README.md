# Face Detection Project

This project demonstrates face detection using OpenCV with a Haar cascade model. The application includes two scripts:

1. **face-detector.py**: Detects faces in real-time using a webcam.
2. **faceimg.py**: Detects faces in static images.

## Features
- Real-time face detection using the webcam.
- Face detection in static images, including a sample dog picture.
- Highlights detected faces with randomly colored rectangles.

## Requirements
To run this project, you'll need the following:

- Python 3.x
- OpenCV library
- Haar cascade model for face detection

### Installing Requirements
Install the required Python library using the following command:

```bash
pip install opencv-python
```

### Download the Haar Cascade Model
Download the `haarcascade_frontalface_default.xml` model from [OpenCV's GitHub repository](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) or use the pre-included file in this project.

Place the downloaded model in the project folder.

## Project Structure
```
.
|-- face-detector.py      # Real-time face detection using a webcam
|-- faceimg.py            # Face detection in static images
|-- haarcascade_frontalface_default.xml  # Haar cascade model for face detection
|-- IN.mp4                # Sample video file for testing
|-- dog.webp              # Sample image file for testing
|-- requirements.txt      # Required Python packages
```

## Usage

### 1. Real-Time Face Detection
To detect faces using your webcam, run the `face-detector.py` script:

```bash
python face-detector.py
```

#### Key Features:
- Press `q` or `Q` to quit the program.

### 2. Face Detection in Images
To detect faces in static images, run the `faceimg.py` script:

```bash
python faceimg.py
```

#### Output:
- The image with detected faces is displayed in a window.
- Press any key to close the window.

### 3. Testing with Video Files
You can replace the webcam feed in `face-detector.py` with a video file (e.g., `IN.mp4`) by changing:

```python
webcam = cv2.VideoCapture(0)
```

to:

```python
webcam = cv2.VideoCapture('IN.mp4')
```

## Files
### `haarcascade_frontalface_default.xml`
The Haar cascade model is essential for detecting faces. If you don't have this file, download it from:

[Haar Cascade Model on GitHub](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

Place the file in the project directory.

### `dog.webp`
A sample image included in the project folder for testing face detection.

### `IN.mp4`
A sample video file for testing real-time face detection. Replace with your own video if needed.

## Requirements File
The `requirements.txt` includes:
```
opencv-python
```
Install the required packages using:

```bash
pip install -r requirements.txt
```

## Credits
- OpenCV: [https://opencv.org](https://opencv.org)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

