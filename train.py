import pandas as pd #we will use it for handling data as without it model cannnot be trained
from sklearn.feature_extraction.text import TfidfVectorizer #we will use it to convert text to numerical vectors
from sklearn.pipeline import Pipeline # we use it to make machine learning pipeline
from sklearn.linear_model import LogisticRegression # it is used for logistic regression classification
from sklearn.metrics import classification_report, accuracy_score # these are evaluation metrics
from sklearn.impute import SimpleImputer # actually it is used for filling the missing values
from sklearn.preprocessing import FunctionTransformer  # it will be used here for applying functions in pipelines
from sklearn.pipeline import FeatureUnion # it is used for combining the transformers)
from sklearn.compose import ColumnTransformer # we will be using it for different preprocessing (transformations) to specific columns of your dataset.
from sklearn.model_selection import train_test_split  # it will help usin splitting the dataset for training and testing 
import joblib # it will be used for saving or loading the trained model

# Step 1: we will be loading the dataset
df = pd.read_csv("health(2).csv")  # we will be  loading the CSV file into a pandas DataFrame 
# As on this dataset only we will be training data 

# Step 2: we will be checking for distribution of doctor type 
print("Samples per doctor type:\n", df['doctor_type'].value_counts())  # it will print how many samples will be their per doctor type

# Step 3: we will be  combining symptoms and disease into a single input text feature
# If their is either NaN, we will fill it with empty string
df['symptoms'] = df['symptoms'].fillna("") # it will replace NaN in 'symptoms' column with an empty string
df['disease'] = df['disease'].fillna("") # it will replace NaN in 'disease' column with an empty string
df['combined_text'] = df['symptoms'] + " " + df['disease'] # we will then combine symptoms and disease text into one string

# Step 4: we will do splitting of train-test of dataset 
X_train, X_test, y_train, y_test = train_test_split( 
    df["combined_text"], df["doctor_type"], # it will contain Features (input text)
    # it will also contain Labels (target classes)
    test_size=0.2, # we will use 20% data for testing
    random_state=42 # it will ensure us reproducible results
)

# Step 5: we will be building the pipeline (TF-IDF + Logistic Regression)
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()), # we will then convert text to TF-IDF features
    ("clf", LogisticRegression(max_iter=1000, class_weight='balanced')) # we will then make classifier with balanced class weights
])

# Step 6: In this step we will be training the model
pipeline.fit(X_train, y_train) # we will fit the pipeline to the training data


# Step 7: In this step we will used for evaluating the model
y_pred = pipeline.predict(X_test) # we will predicting result on the test set 

print("\n Accuracy:", accuracy_score(y_test, y_pred)) # it will print the accuracy of the whole model 
print("\n Classification Report:\n", classification_report(y_test, y_pred))  # it will print the detailed classification metrics


# Step 8: In this we will save the pipeline
joblib.dump(pipeline, "doctor_recommendation_model_v2.pkl") # in this we will save the trained pipeline to a file
print("\n Model saved as doctor_recommendation_model_v2.pkl") #it will print the confirmation of saving