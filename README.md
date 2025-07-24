#  Shopper Intent Prediction

Developed a machine learning web application using **Flask** to predict whether a website visitor will complete a purchase (generate revenue). The project includes data preprocessing, feature engineering, model training, and deployment of the final predictive model. Achieved high accuracy using decision tree classification via scikit-learn.

---

##  Shopper Intent Prediction App

This Flask web application predicts whether an online shopper will complete a purchase based on user session behavior and attributes. It uses a pre-trained machine learning model to classify whether the visitor is likely to generate revenue.

---

##  Features

- Interactive HTML form for user input
- Input fields for behavioral and session-related parameters (e.g., `Administrative_Duration`, `Month`, `VisitorType`)
- Real-time prediction using a trained Decision Tree model
- Preprocessing using saved encoders and column ordering
- Clear prediction result (Purchase: `True` or `False`)

---

##  Tech Stack

- **Python**
- **Flask** (for web interface)
- **pandas** (for data processing)
- **Scikit-learn** (for ML model)
- **Pickle** (for loading model and encoders)
- **HTML/CSS** (frontend form)

---

##  Installation

### 1. Clone the Repository

git clone https://github.com/your-username/shopper-intent-predictor.git
cd shopper-intent-predictor

Install Dependencies

We recommend using a virtual environment:

pip install flask pandas scikit-learn

Required Files
Make sure the following files are present in the project directory:

shopper_tree.pkl: Contains the trained model, feature encoders, and feature order

app.py: Flask app backend logic

index.html: Frontend form for user input

4. Run the App

python app.py

Then, open your browser and go to:

cpp
http://127.0.0.1:5000/

Input Parameters
Parameter	Description
Administrative -	Number of administrative pages visited, 
Administrative_Duration	-Total time spent on administrative pages, 
Informational	-Number of informational pages visited, 
Informational_Duration-	Total time spent on informational pages, 
ProductRelated-	Number of product-related pages visited, 
ProductRelated_Duration	-Total time spent on product-related pages, 
BounceRates -	Average bounce rate value, 
ExitRates	-Average exit rate value, 
PageValues -	Average value of pages viewed, 
SpecialDay-	Closeness of the visit to a special day (e.g., Valentine’s Day, Black Friday), 
Month	-Month of the session (e.g., Jan, Feb, ..., Dec), 
OperatingSystems -	Type of operating system used, 
Browser -	Browser used by the visitor, 
Region -	Geographical region of the visitor, 
TrafficType	 - Type of traffic source, 
VisitorType	- Type of visitor (Returning Visitor, New Visitor, Other), 
Weekend -	Whether the visit occurred on a weekend (True or False). 

Sample Output
Prediction: The visitor will generate revenue (True)

Prediction: The visitor will not generate revenue (False)

Project Structure

shopper-intent-predictor/
│
├── app.py               # Flask app script
├── index.html           # Frontend input form
├── shopper_tree.pkl     # Pre-trained ML model with encoders
└── README.md            # Project documentation

License
This project is open-source under the MIT License. See LICENSE for more details.
