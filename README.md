# Thyroid Disease Prediction

This project focuses on predicting thyroid disease using machine learning techniques, specifically using a Random Forest classifier. The dataset used for training and evaluation contains various features related to thyroid health and patient information.


## Demo
[streamlit-app-2024-07-09-00-07-78.webm](https://github.com/vinayakverma24/Thyroid-Prediction/assets/164455230/42ef4955-4dad-4c27-90c8-90290492ee21)



## Installation

1. **Clone the repository:**

2. **Install dependencies:**
    ```bash
        pip install -r requirements.txt
    ```
    
## Running the Project

To run the project, use the following command:

```bash
python main.py
```

This command will trigger the execution of the project, including data preprocessing, model training, evaluation, and saving the model and encoder.


## Project Workflow

### Data Loading and Preprocessing:

- Data is loaded from a CSV file (`hypothyroid.csv`).
- Preprocessing includes handling missing values, converting categorical variables to numeric, and encoding target labels.

### Model Training:

- Random Forest classifier is trained using hyperparameter tuning and oversampling to handle class imbalance.

### Model Evaluation:

- Performance of the trained model is evaluated using classification metrics (precision, recall, F1-score).

### Saving Model and Encoder:

- Trained model (`trained_model.pkl`) and label encoder (`label_encoder.pkl`) are saved in the `model/` directory.


#### To run the Streamlit app:

```bash
streamlit run app.py
``` 
