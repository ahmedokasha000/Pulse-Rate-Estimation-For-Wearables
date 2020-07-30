# FDA  Submission

**Your Name:** 
Prithvi Kambhampati

**Name of your Device:** 
Pneumonia Detection Assistant

## Algorithm Description 

### 1. General Information

**Intended Use Statement:**   
For assisting a radiologist in detection of pneumonia in x-ray images.  
**Indications for Use:**  
Gender: Men and women  
Age: 2 to 90  
Body part: Chest  
Position: AP (Anterior/Posterior) or PA (Posterior/Anterior)  
Modality: DX (Digital Radiography)  
**Device Limitations:**  
Pneumonia is similar to at least 2 other diseases: Pneumothorax and emphysema. The system should not be used with these diseases.  
**Clinical Impact of Performance:**  
If the model predicts negative, it is correct with 91% probability, and if the model predicts positive, it is correct with 29% probability. The algorithm is recommended for assisting a radiologist screening those images that most probably do not contain Pneumonia.  
### 2. Algorithm Design and Function

![](flowchart.png)    
**DICOM Checking Steps:**      
Check if age is between 2 and 90.    
Check if body part is 'CHEST'.    
Check if position is either 'PA' or 'AP'.    
Check modality is 'DX'.    
**Preprocessing Steps:**      
Convert images to grayscale if needed.    
Normalize images.    
Resize images to the specific size the trained model uses.      
**CNN Architecture:**    
    input_3  
    block1_conv1  
    block1_conv2  
    block1_pool  
    block2_conv1  
    block2_conv2  
    block2_pool  
    block3_conv1  
    block3_conv2  
    block3_conv3  
    block3_pool  
    block4_conv1  
    block4_conv2  
    block4_conv  
    block4_pool  
    block5_conv1  
    block5_conv2  
    block5_conv3  
    block5_pool  
    flatten_2  
    dropout_5  
    dense_5  
    dropout_6  
    dense_6  
    dropout_7  
    dense_7  
    dropout_8  
    dense_8  

### 3. Algorithm Training

**Parameters:**
* Types of augmentation used during training:
1. horizontal flip
2. height shift: 0.1
3. width shift: 0.1
4. rotation angle range: 0 to 20 degrees
5. shear: 0.1
6. zoom: 0.1
* Batch size: 32
* Optimizer learning rate: 1e-4
* Layers of pre-existing architecture that were frozen  
    input_3   
    block1_conv1   
    block1_conv2   
    block1_pool   
    block2_conv1   
    block2_conv2   
    block2_pool   
    block3_conv1   
    block3_conv2   
    block3_conv3   
    block3_pool   
    block4_conv1   
    block4_conv2    
    block4_conv3  
    block4_pool   
    block5_conv1   
    block5_conv2   
* Layers of pre-existing architecture that were fine-tuned  
    block5_conv3   
    block5_pool  
* Layers added to pre-existing architecture  
    flatten_2  
    dropout_5  
    dense_5  
    dropout_6  
    dense_6  
    dropout_7  
    dense_7  
    dropout_8    
    dense_8  
![](performance.png)
![](precision_v_recall.png)
![](auc.png)
**Final Threshold and Explanation:**
The maximum F1 score is 0.423. At this score, the values of threshold: 0.435, precision: 0.334, recall: 0.572. With threshold = 0.3, we can see that the the recall is at 77% and precision is at 29%. At this threshold we can acheive higher recall rate at a low loss in precision.
### 4. Databases

**Description of Training Dataset:** 
Training dataset consisted of 2290 chest xray images, with a 50/50 split between positive and negative cases. The data is further increased using image augmentation techniques.
Example images: 
![](training_images.png)
**Description of Validation Dataset:** 
The validation data is not augmented. Example images:
![](valid_data.png)

### 5. Ground Truth
There are 15 types of diagnoses:
Total types diagnoses:  15
{'Atelectasis',
 'Cardiomegaly',
 'Consolidation',
 'Edema',
 'Effusion',
 'Emphysema',
 'Fibrosis',
 'Hernia',
 'Infiltration',
 'Mass',
 'No Finding',
 'Nodule',
 'Pleural_Thickening',
 'Pneumonia',
 'Pneumothorax'}

The data is taken from a larger dataset. There could be some mistakes in the labels.

### 6. FDA Validation Plan

**Patient Population Description for FDA Validation Dataset:**  
Both male and female patients' data was present in the dataset.  
The age distribution is between 2 years old and 90 years old. It is not recommended for the model to be used outside of this distribution.  
**Ground Truth Acquisition Methodology:**  
The ground truth for the FDA Validation Dataset can be obtained as an average of three practicing radiologists (as a widely used 'silver standard').  
**Algorithm Performance Standard:**  
The algorithm should perform better that the silver standard.   