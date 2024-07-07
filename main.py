from ThyroidPrediction.data_utils import load_data, preprocess_data, split_data
from ThyroidPrediction.model_utils import train_rf_model, evaluate_model
from ThyroidPrediction.file_utils import save_model, save_encoder, create_directory_if_not_exists

def main():
    # Load and preprocess data
    path = 'data/hypothyroid.csv'
    df = load_data(path)
    df_preprocessed, encoder = preprocess_data(df)
    
    X = df_preprocessed.drop('Class', axis=1)
    y = df_preprocessed['Class']
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Train the Random Forest model
    trained_model = train_rf_model(X_train, y_train)
    
    # Evaluate the trained model
    evaluate_model(trained_model, X_test, y_test)
    
    # Define file paths for saving
    model_directory="model"
    model_filename = "model/trained_model.pkl"
    encoder_filename = "model/label_encoder.pkl"
    
    # Save the trained model and encoder
    create_directory_if_not_exists(model_directory)
    save_model(trained_model, model_filename)
    save_encoder(encoder, encoder_filename)

if __name__ == "__main__":
    main()
