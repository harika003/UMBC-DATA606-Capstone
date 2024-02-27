# 1. Title and Author
- Title: **Prediction of Heart Diseases**
- Prepared for UMBC Data Science Master Degree Capstone by Harika Tamma under the guidance of Dr Chaojie (Jay) Wang
- Author Name: Harika Tamma
- GitHub profile : https://github.com/harika003
- LinkedIn profile : https://www.linkedin.com/in/harika-tamma-938814173/
- PowerPoint presentation file : https://docs.google.com/presentation/d/1mH45OdcDaj2XBxirxAu-UqucxDpHWpjzz7ghj0g73XM/edit#slide=id.p7

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

    
    


