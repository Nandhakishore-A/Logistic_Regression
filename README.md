# Logistic_Regression

🚢 Titanic Survival Prediction

A Machine Learning web application that predicts whether a passenger survived the Titanic disaster based on features such as passenger class, gender, age, and fare.
The model is built using Logistic Regression and deployed using Streamlit.

🔗 Live Demo:
👉 https://logisticregression1234.streamlit.app/

📌 About the Project

This project uses a Logistic Regression classification model trained on the famous Titanic dataset.
The main objective is to predict passenger survival (Yes / No) based on user-provided details.

The application provides a clean and interactive web interface where users can enter passenger information and instantly receive a prediction result.

The project is optimized and deployed using Streamlit Cloud.

🛠️ Tech Stack

Frontend: Streamlit

Backend: Python

Machine Learning: Scikit-Learn

Model Saving: Joblib

Deployment: Streamlit Cloud

📂 Project Structure
├── app.py                     # Streamlit web application
├── train_model.py             # Script used to train the Logistic Regression model
├── logistic_model.pkl         # Trained model file
├── encoder.pkl                # Label encoder for categorical features
├── requirements.txt           # Required Python packages
└── DATA_SETS/
    └── Titanic-Dataset.csv    # Dataset used for training

▶️ How to Run Locally

Follow these steps to run the project on your local system:

1️⃣ Clone the Repository
git clone https://github.com/Nandhakishore-A/Logistic_Regression.git
cd Logistic_Regression

2️⃣ Install Dependencies

Make sure Python is installed, then run:

pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py


The app will open automatically in your browser.

🤖 Model Details

Algorithm: Logistic Regression

Library Used: Scikit-Learn

🔢 Input Features

Passenger Class (Pclass)

Gender (Sex)

Age

Fare

📤 Output

Survival Prediction

1 → Survived

0 → Not Survived

📊 Dataset

The dataset used in this project is the Titanic Dataset, which contains passenger information such as age, gender, ticket class, fare, and survival status.

🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit pull requests to enhance the model accuracy, add new features, or improve the UI.
