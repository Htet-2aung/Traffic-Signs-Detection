# Traffic-Signs-Detection

This repository is for the Semester 1 2025-2026 Information Technology Project, held under the supervision of the Faculty of Information Technology, Ton Duc Thang University. This project aims to create a deep learning/computer vision model that can detect traffic signs globally and locally in Vietnam.


<p align="center">
  <img src="/batch/train_batch1.jpg" alt="Traffic Sign Example" width="400"/>
</p>

<hr>

This project uses two lifelike datasets: the GTSRB (German Traffic Sign Recognition Benchmark) and the Vietnam Traffic Signs Dataset from Roboflow.


## Data Engineering: Building a Unified Dataset

The core of this project's success lies in the creation of a robust, hybrid dataset. To build a model that understands the general concept of a traffic sign while also being an expert in the specific context of Vietnam, we merged two distinct datasets: GTSRB and a custom Vietnamese dataset. This process required a systematic data engineering pipeline to resolve challenges related to data formats and class label inconsistencies.

### The Challenge

The two source datasets were fundamentally incompatible for direct use:

1.  **Different Task Formats:**
    * **GTSRB:** A classification dataset containing thousands of pre-cropped images of individual signs. It lacks bounding box annotations.
      - **Total Images**: 51,839
      -  [GTSRB] : https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign
    * **VNTS (Roboflow):** A detection dataset with full images and corresponding `.txt` label files containing bounding box coordinates for each sign.
[VNTS] : https://universe.roboflow.com/vietnam-traffic-sign-detection/vietnam-traffic-sign-detection-2i2j8/dataset/5     
2.  **Inconsistent Class Labels:**
    * The class IDs are not aligned. For example, a `Stop` sign in GTSRB might be class `14`, while in our Vietnamese dataset, it could be class `0`. A direct merge would cause the model to learn incorrect labels.

### The Solution: A Three-Step Unification Pipeline

To overcome these challenges, we implemented the following data processing pipeline to create a single, cohesive dataset ready for YOLOv8.

#### Step 1: Creating a "Master Class Map"

The first and most critical step was to define a single, unified set of class labels. We created a master list of all unique traffic signs we wanted our model to recognize. Then, we generated a Python dictionary to map the original class IDs from the GTSRB dataset to our new, master class IDs.

*This ensures that a "Stop" sign from Germany (`ClassId: 14`) and a "Stop" sign from Vietnam (`ClassId: 0`) are both mapped to the same master ID (e.g., `MasterId: 0`).*

#### Step 2: Standardizing Annotation Formats to YOLOv8

With a unified class map, we processed each dataset to produce annotations in the standard YOLOv8 `.txt` format (`<class_id> <x_center> <y_center> <width> <height>`).

* **For the Vietnam Traffic Signs Dataset:** This was straightforward. We exported the dataset directly from Roboflow, selecting the "YOLOv8" format, which automatically generated the required label files.

* **For the GTSRB Dataset:** This required a creative solution. Since GTSRB is a classification dataset, each image contains only one centered sign. We developed a Python script to iterate through every image and:
    1.  Convert the image format from `.ppm` to `.png` for broader compatibility.
    2.  Create a corresponding `.txt` label file.
    3.  Generate a "pseudo" bounding box that covers the entire image, as the sign is the only object present.
    4.  Assign the **Master Class ID** from our map created in Step 1.

    The resulting YOLO annotation for every GTSRB image was:
    ```
    <master_class_id> 0.5 0.5 1.0 1.0
    ```

#### Step 3: Merging the Datasets

After standardizing both datasets, the final step was to merge them into the final directory structure required for training. We copied all processed images and their corresponding new label files from both the GTSRB and VNTS sources into the final `train/` and `valid/` folders.

This resulted in a single, powerful training dataset that leverages the scale and clean examples of GTSRB to build foundational knowledge, while using the specific, real-world examples from the Vietnamese dataset to specialize the model for its target environment.
