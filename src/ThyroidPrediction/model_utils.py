from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import classification_report

def get_best_params_for_random_forest(train_x, train_y):
    # Initialize with different combinations of parameters
    param_grid = {
        "n_estimators": [50, 100, 150, 200],  # Adjusting number of trees in the forest
        "criterion": ['gini', 'entropy'],
        "max_depth": [None, 10, 20, 30],  # Adjusting maximum depth of each tree
        "max_features": ['auto', 'sqrt', 'log2']  # Adjusting the number of features to consider at every split
    }

    clf = RandomForestClassifier()

    # Create an object of the Grid Search class
    grid = GridSearchCV(estimator=clf, param_grid=param_grid, cv=5, verbose=3)

    # Find the best parameters
    grid.fit(train_x, train_y)

    # Extract the best parameters
    best_params = grid.best_params_
    criterion = best_params['criterion']
    max_depth = best_params['max_depth']
    max_features = best_params['max_features']
    n_estimators = best_params['n_estimators']

    # Create a new model with the best parameters
    clf = RandomForestClassifier(n_estimators=n_estimators, criterion=criterion,
                                 max_depth=max_depth, max_features=max_features)

    # Train the new model
    clf.fit(train_x, train_y)

    print('Random Forest best params:', best_params)

    return clf

def train_rf_model(X_train, y_train):
    # Oversample to handle class imbalance
    ros = RandomOverSampler(random_state=2)
    X_sampled, y_sampled = ros.fit_resample(X_train, y_train)
    
    # Train the model with best parameters
    rfc_model = get_best_params_for_random_forest(X_sampled, y_sampled)

    return rfc_model

def evaluate_model(model, X_test, y_test):
    # Make predictions
    rfc_pred = model.predict(X_test)
    
    # Print classification report
    print(classification_report(y_test, rfc_pred))
