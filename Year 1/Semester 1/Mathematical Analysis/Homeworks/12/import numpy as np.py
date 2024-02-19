#using a real data set found online from a school from portugal, we have 75 students which were monitored during a semester, absences
#failures, activities, etc, we aim to predict using sklearn librairy the next grade the student will get
#in the end we compare the predicted model grade and calculate the mean_squared_error of our model
#predicted grade are found in another csv attached with its name

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

#load data
data = pd.read_csv('student-mat.csv')

# The last column 'G3' is the the target (future grade) we aim to predict and at the end compare to the real result
X = data.drop('G3', axis=1)
y = data['G3']

#columns that need encoding
categorical_cols = X.select_dtypes(include=['object', 'category']).columns

#column transformer for one-hot encoding
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_cols)
    ], remainder='passthrough')

#pipeline with preprocessing and model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', Ridge())
])

#training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train the model
model.fit(X_train, y_train)

#predictions on the test set
y_pred = model.predict(X_test)

#print the Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

#actual and predicted grades
grades_comparison = pd.DataFrame({'Actual Grades': y_test, 'Predicted Grades': y_pred})

grades_comparison.reset_index(drop=True, inplace=True)

#save the DataFrame to a new CSV file
grades_comparison.to_csv('predicted_grades.csv', index=False)

#message to confirm the file has been saved
print('Predicted grades have been saved to predicted_grades.csv')
