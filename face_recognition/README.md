# Face Recognition Project

This project aims to perform face recognition using OpenCV, Haar cascade classifier for face detection, and LBPHFace recognizer. Below are the key components and functionalities of the project:

## 1. Face Capture using OpenCV
Faces are captured using the OpenCV library for training the recognition model. This involves capturing images of individuals' faces to be used for training the model.

## 2. Assigning IDs to Individual Faces
Each captured face is assigned a unique numerical ID for identification and distinction within the dataset.

## 3. Face Detection using Haar Cascade Classifier
Haar cascade classifier is utilized for face detection within images. This helps in identifying and isolating the faces from the rest of the image.

## 4. LBPHFace Recognizer
The LBPHFace recognizer is employed for recognizing faces based on the patterns and features extracted from the face images.

## 5. Model Training
A model is trained using the collected faces and their corresponding IDs. This training process involves teaching the recognizer to associate specific faces with their respective IDs.

## 6. Real-time Face Recognition
The trained model is tested in real-time face recognition scenarios. It is capable of recognizing faces in real-time, associating them with the correct individual, and providing the accuracy of recognition.

## 7. Multiple Face Detection
The system supports the detection of multiple faces within a single image, enabling it to recognize and differentiate between multiple individuals simultaneously.
