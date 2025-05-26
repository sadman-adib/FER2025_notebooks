<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>FER2025 README</title>
</head>
<body>

  <h1>FER2025: Facial Emotion Recognition with Gender Classification</h1>

  <p><strong>FER2025</strong> is a deep learning-based project that integrates Facial Emotion Recognition (FER) with Gender Classification using Convolutional Neural Networks (CNNs). This multi-task learning approach improves recognition accuracy by considering gender-specific expression patterns.</p>

  <h2>Features</h2>
  <ul>
    <li>Emotion + Gender classification (12 classes)</li>
    <li>Object detection with bounding boxes</li>
    <li>Preprocessing: Grayscale, 640×640 resize, auto-orientation</li>
    <li>Dataset: 3,176 images, 5,160 annotations</li>
    <li>Formats: YOLO (TXT) & COCO (JSON)</li>
  </ul>

  <h2>Models Trained</h2>
  <ul>
    <li>YOLOv7</li>
    <li>YOLOv8</li>
    <li>YOLOv11</li>
    <li>YOLOv12</li>
    <li>RF-DETR (Best Performer)</li>
  </ul>

  <h2>Best Model (RF-DETR) Performance</h2>
  <ul>
    <li><strong>Precision:</strong> 0.842</li>
    <li><strong>Recall:</strong> 0.772</li>
    <li><strong>mAP@50:</strong> 0.856</li>
  </ul>

  <h2>Dataset & Access</h2>
  <p>Source: Royalty-free images</p>
  <p>Public Dataset: <a href="https://data.mendeley.com/datasets/y7xfffjh6z/3" target="_blank">Mendeley Data</a></p>

  <h2>Tools Used</h2>
  <ul>
    <li>Roboflow (annotation)</li>
    <li>PyTorch, YOLO, Transformers</li>
  </ul>

  <h2>Usage</h2>
  <p>Clone the repo and follow model training scripts in the <code>/models</code> directory. Dataset folder structure: <code>train/</code>, <code>valid/</code>, <code>test/</code>.</p>

</body>
</html>
