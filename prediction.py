 # we will be importing joblib to load the trained machine learning model
import joblib

# we will be loading the trained pipeline model which we will be using from from a saved .pkl file
model = joblib.load("doctor_recommendation_model_v2.pkl")

# this content will be displaying welcome message and give instructions to the user
print("👨‍⚕ Doctor Recommendation System") #it will print doctor recommendation system
print("Enter your symptoms, disease, or both in a single line.") # we will be asking any symptoms or disease 
print("Type 'exit' to quit.\n") #if user want to exit, he/she can type exit to quit

# we will be starting an infinite loop which will continuously take user input
while True:
    # we will be asking the user to input their symptoms or disease
    user_input = input("📝 Enter symptoms/disease: ").strip() #it will be asking to write symptoms/disease from user
    # this condition will be for breaking the loop
    # If we see the user types 'exit', we will break the loop and we will end the program
    if user_input.lower() == "exit":
        print("👋 Exiting. Take care!") # it will print exit 
        break  # we will exit the loop
    # we will check if loop is empty
    # If the user input is empty, we wil prompt it again
    if user_input == "":
        print("⚠ Input cannot be empty. Please try again.") #it will ask user to try again
        continue  # we will go back to the starting of the loop

    # we will use the trained model that will predict the type of doctor needed for the given symptoms or disease
    prediction = model.predict([user_input])  # we will take input in the list format only

    # it will be displaying the predicted type of doctor needed
    print("🔍 Recommended Doctor Type:", prediction[0], "\n")