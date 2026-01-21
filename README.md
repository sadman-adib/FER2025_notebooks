<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>
<body>

  <h1>Explainable Gender-Aware Facial Emotion Recognition Using a Curated Dataset and a Hybrid Object Detection Framework</h1>

  <p><strong>FER2025</strong> is a deep learning-based project that integrates Facial Emotion Recognition (FER) with Gender Classification using Convolutional Neural Networks (CNNs). This multi-task learning approach improves recognition accuracy by considering gender-specific expression patterns.</p>

  <h2>Features</h2>
  <ul>
    <li>Emotion + Gender classification (12 classes)</li>
    <li>Object detection with bounding boxes</li>
    <li>Preprocessing: Grayscale, 640×640 resize, auto-orientation</li>
    <li>Dataset: 7,386 images, 11,253 annotations</li>
  </ul>

  <h2>Models Trained</h2>
  <ul>
    <li>YOLOv7</li>
    <li>YOLOv8</li>
    <li>YOLOv11</li>
    <li>YOLOv12</li>
    <li>RF-DETR</li>
    <li>XFDetNet (Best Performer)</li>
  </ul>

  <h2>Best Model Performance</h2>
  <ul>
    <li><strong>Precision:</strong> 96.1% </li>
    <li><strong>Recall:</strong> 99.2% </li>
    <li><strong>mAP@50:</strong> 99.5 </li>
  </ul>

  <h2>Dataset & Access</h2>
  <p>Source: Royalty-free images</p>
  <p>Public Dataset: <a href="https://data.mendeley.com/datasets/y7xfffjh6z/4" target="_blank">Mendeley Data</a></p>

  <h2>Tools Used</h2>
  <ul>
    <li>Roboflow (annotation)</li>
    <li>PyTorch, YOLO, Transformers</li>
  </ul>

  <h2>Usage</h2>
  <p>Clone the repo and follow model training scripts in the <code>/models</code> directory. Dataset folder structure: <code>train/</code>, <code>valid/</code>, <code>test/</code>.</p>

</body>
</html>
