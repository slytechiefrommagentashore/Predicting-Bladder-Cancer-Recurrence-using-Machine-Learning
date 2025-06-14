# Predicting Bladder Cancer Recurrence using Machine Learning

## Overview
This project is part of my **final year research project**, conducted under the supervision of **Dr. Sanjay Saxena** from **IIIT BHU**.
Bladder cancer has a high recurrence rate, especially in non-muscle-invasive bladder cancer (NMIBC) cases. This project leverages machine learning techniques to predict recurrence using clinical and genomic data, improving early diagnosis and personalized treatment planning.

## Objectives
- Develop a **predictive model** for bladder cancer recurrence.
- Utilize **clinical and genomic** data from the **TCGA BLCA dataset**.
- Apply **machine learning** and **deep learning** techniques for enhanced prediction.
- Implement **image processing and segmentation** for tumor detection using **U-Net**.

## Dataset
The dataset used in this project comes from **The Cancer Genome Atlas (TCGA) - BLCA**:
- **120 patient samples** with structured clinical and genomic data.
- **111,781 DICOM medical images** (CT, CR, MR, PT, DX formats) converted to PNG.

## Methodology
### **1. Data Preprocessing**
- Data cleaning and handling of missing values.
- Normalization and feature selection for ML models.

### **2. Machine Learning Models**
- **Random Forest**
- **XGBoost**
- **Deep Learning-based U-Net segmentation** for medical images.

### **3. Model Evaluation**
- **Accuracy, Precision, Recall, and F1-score**.
- **ROC-AUC Curve Analysis** for model comparison.

## Repository Structure
```
Bladder-Cancer-Recurrence-ML/
│── clinical data/        # Processed clinical dataset
│── histopathololgy data/ # Processed image dataset
│── notebooks/            # Jupyter notebooks for exploration & model training
│── models/               # Trained ML models
│── src/                  # Python scripts for preprocessing & segmentation
│── results/              # Evaluation metrics, plots, and reports
│── projects folder/      # Evaluation metrics, plots, and reports
│── README.md             # Project overview and instructions
│── requirements.txt      # Dependencies (TensorFlow, PyTorch, etc.)
│── .gitignore            # Ignore unnecessary files (DICOMs, cache, large datasets)
```

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/YOUR-USERNAME/Bladder-Cancer-Recurrence-ML.git
cd Bladder-Cancer-Recurrence-ML
pip install -r requirements.txt
```
<!--
## Usage
Run the preprocessing script:
```bash
python src/data_cleaning.py
```
Train the model:
```bash
python src/train_model.py
```

## Future Enhancements
- **Feature extraction improvements** from both medical images and clinical data.
- **Integration of multi-modal features** for better accuracy.
- **Refinement of image processing techniques**.
- **Development of a clinical decision-support system**.

## Contributors
- **Vasireddy Satvika** (Lead Researcher & Developer)
- **Dr. Sanjay Saxena** (Supervisor - IIIT BHU)
- **Dr. Swapnil A. Lokhande** (On-campus Mentor)
-->

## References
1. [M. Lucas, I. Jansen, T. G. van Leeuwen, J. R. Oddens, D. M. de Bruin, and H. A. Marquering, "Deep Learning–based Recurrence Prediction in Patients with Non–muscle-invasive Bladder Cancer," Eur. Urol. Focus, vol. 8, no. 1, pp. 165-172, Jan. 2022.](https://doi.org/10.1016/j.euf.2020.12.008)
2. [The Cancer Imaging Archive, “TCGA-BLCA: The Cancer Genome Atlas Bladder Cancer Collection.”](https://www.cancerimagingarchive.net/collection/tcga-blca/) Accessed: Feb. 16th, 2025.
3. [National Cancer Institute, “TCGA-BLCA: The Cancer Genome Atlas Bladder Cancer Project,” Genomic Data Commons.](https://portal.gdc.cancer.gov/projects/TCGA-BLCA) Accessed: Feb. 16th, 2025.
4. [D. Malik, mritopng: A DICOM to PNG Conversion Tool, GitHub repository, 2018.](https://github.com/danishm/mritopng) Accessed: Feb. 23rd, 2025.

---
⭐ *If you find this project useful, please star the repository!*
