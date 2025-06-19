# Project Flowchart

# Dataset Preparation and Preprocessing

- **Data Description**
  - MRI and CT scan images
  - Associated clinical data
- **Ground Truth Challenge**
  - No manual ground truth masks available

# Image Segmentation

- **Segmentation Strategy**
  - Traditional thresholding and supervised learning
  - Transfer learning with U-Net model
    - Pre-trained on related dataset
- **Segmentation Types**
  - Tumor only
  - Tumor with wall
- **Output**
  - Generated segmentation masks for tumor regions

# Feature Extraction

- **Radiomics Features**
  - PyRadiomics Python library
  - Shape, intensity, texture-based features
- **Clinical Data Integration**
  - Cleaned and merged with radiomics data

# Classification

- **Objective**
  - Predict tumor recurrence (Yes/No)
- **Model Architecture**
  - 3-layer Multilayer Perceptron (MLP)
  - Hidden layer dimension: hidden_dim
  - Loss function: Binary Cross Entropy (BCE)
  - Optimizer: Adam
  - Output activation: Sigmoid
- **Constraints**
  - Small dataset size
  - Use of lightweight MLP

# Cross-Validation

- **Approach**
  - 5-fold cross-validation
- **Evaluation**
  - Best results recorded
  - Plotted loss vs. validation accuracy
  - Confusion matrix analysis

# Conclusion

- **Integration**
  - Combined segmentation, radiomics, and machine learning
- **Challenges**
  - Managed data limitations
  - Tackled absence of manual ground truth masks
