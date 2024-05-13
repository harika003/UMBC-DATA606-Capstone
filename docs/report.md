# 1. Title and Author
- Title:  **Prediction of Heart Diseases**
- Prepared for UMBC Data Science Master Degree Capstone by Harika Tamma under the guidance of Dr Chaojie (Jay) Wang
- Author Name: Harika Tamma
- Semester: Spring 2024
- GitHub rep link : https://github.com/harika003/UMBC-DATA606-Capstone
- Report link :https://github.com/harika003/UMBC-DATA606-Capstone/edit/main/docs/report.md
- PowerPoint presentation:https://github.com/harika003/UMBC-DATA606-Capstone/blob/main/docs/final_presenation.pptx
- Youtube video : https://youtu.be/_gMURe03XGc
- LinkedIn profile : https://www.linkedin.com/in/harika-tamma-938814173/
  
# 2. Background
- Heart attacks are a widespread and life-threatening issue globally, caused by blockages in blood vessels due to plaque buildup. In the United States, a heart attack occurs every 40 seconds, resulting in approximately 805,000 cases annually, with over 600,000 resulting in death. Similarly, India faces a significant burden, with 70% of cardiac deaths occurring in the 30-60 age group. Over the past three years, India has consistently recorded over 28,000 deaths annually due to heart attacks.
  
  ### Problem Statement:
  * Heart disease remains a leading cause of morbidity and mortality worldwide, with early detection and preventive interventions playing pivotal roles in mitigating its impact.
  * The project aims to develop and implement machine learning-based predictive models to accurately identify individuals at high risk of heart attacks. By leveraging demographic, clinical, and lifestyle data, the objective is to create robust models capable of early detection and personalized risk assessment, ultimately enabling proactive interventions and improving patient outcomes.
    
  ### Why does it matter?
  * The proposed project holds significant implications for public health by enabling early identification and targeted intervention for individuals at high risk of cardiovascular diseases. By leveraging machine learning techniques, this project aims to enhance the accuracy and efficiency of CVD risk prediction, thereby facilitating more personalized and proactive healthcare approaches.
  * Predicting heart diseases using machine learning matters because it saves lives, improves healthcare efficiency, enhances patient care, fosters innovation, and empowers individuals to take control of their health.
  ### Research questions:
  * How do different machine learning algorithms compare in terms of their predictive performance for identifying individuals at risk of developing heart disease?
  * What are the most influential clinical and demographic factors associated with the occurrence of heart disease, as identified by predictive modeling techniques?
  * which algorithm best suits the model?
  * Success Parameter:Whether the model has predicted & recommended accurately.

    
# 3. Data
  * Data Source: The coronary heart disease dataset (Framingham dataset), which is available for download from University of Washington’s Bio-Statistics Class, was used in this study. This data collection is derived from current cardiovascular research of people living in Framingham, Massachusetts.This dataset is on-going research.

    
  * Data Size:
  
     * Size of the dataset: 0.5177001953125 MB
     * Size of the dataset: 0.0005055665969848633 GB

  * Data shape:

      * No. of Records : 4240 
      * No. of Features :  16
  * Data Description: 
      * What does each row represent?
        - sex: Male(1) or Female(0)
        - currentSmoker: Whether the patient is smoker or not. Yes(1) and No(0)
        - BPMeds: Whether the patient was on blood pressure medications. Yes(1) and No(0)
        - prevalentStroke: Whether the patient had a stroke before. Yes(1) and No(0)
        - prevalentHyp: Whether the patient has history of Hypertension. Yes(1) and No(0)
        - diabetes: Whether the patient has diabetes. Yes(1) and No(0)
        - TenYearCHD: This is our target variable which we will be predicting. Yes(1) and No(0)
        - education: Defined in classes 1-4. Tells us how much our patient is educated.
        - age: Contains ages of our patients in whole numbers.
        - cigsPerDay: Contains the average of cigarettes smoked by the patients in one day.
        - totChol: Contains total cholesterol level of each patient.
        - sysBP: Contains systolic blood pressure levels of each patient.
        - diaBP: Contains diastolic blood pressure levels of each patient.
        - BMI: Contains body mass index of each patient.
        - heartRate: Contains the average heart rate of the patient.
        - glucose: Contains the glucose level of each patient.



  * Data dictionary:

    <img src = "https://github.com/harika003/UMBC-DATA606-Capstone/blob/main/images/df_info.jpeg" width="600">

    
 * Which variable/column will be your target/label in your ML model?
   - TenYearCHD: This is our target variable which we will be predicting. Yes(1) and No(0)
   - To determine whether the patient will experience coronary heart disease during the following ten years is the classification goal (CHD).

 * Which variables/columns may be selected as features/predictors for your ML models?
   - We have 4240 records and 16 features associated to the data set. We will be dealing with all the features for our Ml model.
     
# 4. Exploratory Data Analysis (EDA)
 Different data analysis has been done for feature selection to see the impact on prediction.
 - **Heatmap:** Explains which features are relevant for the prediction.


<img src = "https://github.com/harika003/UMBC-DATA606-Capstone/blob/main/images/Heatmap.png" width="500">
We can see that
SysBP and diaBP appear to be quite strongly correlated, and there is a negative connection between education and the output variable. 

- **Bivariate Analysis plot Gender wise absence / presence of Chronic Heart Disease (CHD):**

  <img src ="https://github.com/harika003/UMBC-DATA606-Capstone/blob/main/images/CHD_by_gender.png" width= "500">
  
  1. The  analysis plot above shows the prevalence and absence of chronic heart disease (CHD) by gender.
  2. Our observations indicate that there are far too many people in our dataset who do not have CHD.
  3. Negative: Between 80 and 90 percent of females and 60 to 70 percent of males belong to the negative category.
  4. positive: CHD affects roughly 10% of both male and female individuals.
  5. Based on this, we can conclude that our dataset is unbalanced, with roughly 80–90% of the classifications being negative and 10–15%         being positive.
  
- **Distributions of Features:**

  <img src = "https://github.com/harika003/UMBC-DATA606-Capstone/blob/main/images/Distribution_features.png" width= "500">

  * We can see Glucose, Total Cholesterol, Systolic BP & BMI is Right Skewed.
    

  <img src = "https://github.com/harika003/UMBC-DATA606-Capstone/blob/main/images/download-5.png" width= "500">
  
 
  * We can clearly observe that as Age increases the count of Glucose increases too. While Gender wise Glucose Count has almost similiar Median with Few outliers in each. 
Excluding Outliers, Observation make us Clear that for females Cholesterol level is Increasing by Age considering the Quantile (25%, 50%, 75%) values into account. While, for Males the Cholesterol level Quantile is Approx. Similar for each Age Group.

- **Target class count:**
   - **Before Resampling:**

      <img src = "https://github.com/harika003/UMBC-DATA606-Capstone/blob/main/images/data_imbalance.png" width= "500">

      * We got class imbalance that there are 84.5% negative results while 15.15% are positive.  
So  data resampling is done by using random oversampling to address the class imbalance.

   - **After Resampling:**
   
    <img src = "https://github.com/harika003/UMBC-DATA606-Capstone/blob/main/images/Resampled_data.png" width = "500">

- **Feature Importance**

    - **Before Resampling:**

       <img src = "https://github.com/harika003/UMBC-DATA606-Capstone/blob/main/images/feature_imp_unbalanced.png" width = "500">
      
   - **After Resampling:**

      <img src = "https://github.com/harika003/UMBC-DATA606-Capstone/blob/main/images/feature_imp_balanced.png" width= "500">

  
# 5. Model training
  * **Models used for predictive analytics:**
       - Logestic Regression
       - Random Forest Classifier
       - KNNeighborsClassifier
       - Gradient Boosting Classifier
       - Support Vector Classifier
       - Decision Tree Classifier
         
  * **Training the models:**
       - Train vs test split : The data is split into training and testing sets using an 80/20 ratio, where 80% of the data is used for training (X_train, y_train) and 20% for testing (X_test, y_test). This split ratio is specified in the test_size parameter of the train_test_split function.
         
       - Python packages used: pandas:
           * for data manipulation and handling DataFrame structures (df_data).
           * sklearn: for machine learning tasks, including train_test_split for data splitting
           *  MinMaxScaler for feature scaling.
             
       - The development environment : Google CoLab

  * **Measuring and comparing the performance of the models:**
       I Compared the performance of the models based on the evaluation metrics which include accuracy, precision, recall, F1-score.
       The main objective was to select a model based on its accuracy and its diagnostic ability.
   
   * Logistic Regression:
    Accuracy: 40%
    Precision: 100%
    Recall: 40%
    F1-score: 57%

   * Random Forest:
    Accuracy: 97%
    Precision: 100%
    Recall: 97%
    F1-score: 99%

   * K Nearest Neighbors (KNN) Classifier:
    Accuracy: 98%
    Precision: 100%
    Recall: 98%
    F1-score: 99%

   * Gradient Boosting Classifier:
    Accuracy: 97%
    Precision: 100%
    Recall: 97%
    F1-score: 99%

   * Support Vector Classifier (SVC):
    Accuracy: 40%
    Precision: 100%
    Recall: 40%
    F1-score: 57%

   * Decision Tree Classifier:
    Accuracy: 98%
    Precision: 100%
    Recall: 98%
    F1-score: 99%

 ##### KNN and Decision Tree classifiers are recommended for predicting heart disease risk due to their superior performance.I used Decision Tree classifiers.

# 6. Application of the Trained Models

- I have used Streamlit to develop a web app for people to interact with my trained model.My Streamlit Heart Disease Prediction App offers a user-friendly interface where,
- Firstly, users can input a variety of health information into the app, including their age, smoking status, medication usage, medical history, and key health metrics such as cholesterol, blood pressure, BMI, and glucose level. This comprehensive input allows for a thorough assessment of their heart disease risk factors.

- Once the user has inputted their information, they simply click the 'Predict' button. The app then processes this data and promptly displays the predicted risk of heart disease. If the risk is determined to be high, an error message is shown, advising the user to seek medical attention promptly. Conversely, if the risk is low, a success message is displayed, providing reassurance to the user.

- Users receive an immediate prediction of their heart disease risk, clearly categorized as either high or low. Additionally, the app offers guidance on necessary actions based on the risk assessment, empowering users to make informed decisions about their health.

- One of the key strengths of our app lies in its user-friendly interface. Intuitive sliders and dropdown menus make it incredibly easy for users to input their information and obtain predictions with just a click, ensuring a seamless user experience.

- Furthermore, the app is equipped with robust error handling mechanisms. In the event of any issues or errors, the app handles them gracefully, prompting users to retry if necessary and ensuring a smooth user experience throughout.
  
# 7. Conclusion
- **Summary:** In conclusion, our project underscores the potential of machine learning in proactive healthcare by developing models for predicting heart disease risk. Leveraging the Framingham dataset, we trained and evaluated several models,with Random Forest, KNN, Gradient Boosting, and Decision Tree models demonstrating superior performance.Overall, our project lays a foundation for early detection and personalized risk assessment in heart disease management, promising improved patient outcomes and reduced healthcare burden.

- **Limitation:**
   * While our project has made strides in predicting heart disease risk, it's crucial to acknowledge its limitations. One significant limitation is the reliance on the Framingham dataset, which may not capture the full spectrum of demographic, clinical, and lifestyle factors contributing to heart disease risk.
   * Furthermore, the models' generalizability to diverse populations and healthcare settings may be limited, necessitating validation on external datasets for robustness. Future efforts should focus on addressing these limitations through more comprehensive data collection, handling class imbalance more effectively, and validating models across diverse populations to ensure their reliability and applicability in real-world scenarios.

- **Lessons Learned:** Through our project, we've learned that the quality of data, addressing class imbalance, appropriate model selection, and understanding evaluation metrics are crucial for building reliable predictive models for heart disease risk assessment. Continuous improvement through techniques like hyperparameter tuning and feature engineering, along with interdisciplinary collaboration, ensures the applicability and effectiveness of these models in real-world healthcare settings.

- **Future research direction:** In future research, focusing on novel data sources like genetic markers and wearable device data, addressing class imbalance through advanced techniques, and exploring deep learning methods can enhance predictive models for heart disease risk assessment. Prospective studies and clinical trials are necessary to validate model predictions in real-world settings, while interdisciplinary collaboration remains crucial for translating research findings into actionable interventions for heart disease prevention and management.

# 8. References
 - Chawla NV, Bowyer KW, Hall LO, Kegelmeyer WP. SMOTE: synthetic minority over-sampling technique. J Artif Intell Res. 2002;16:321-357. doi:10.1613/jair.953
 - D'Agostino Sr RB, Vasan RS, Pencina MJ, et al. General cardiovascular risk profile for use in primary care: the Framingham Heart Study. Circulation. 2008;117(6):743-753. doi:10.1161/CIRCULATIONAHA.107.699579
 - Hastie T, Tibshirani R, Friedman J. The Elements of Statistical Learning: Data Mining, Inference, and Prediction. 2nd ed. New York, NY: Springer; 2009.





  
