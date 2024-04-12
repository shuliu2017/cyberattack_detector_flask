from flask import Flask, request, render_template
import dill
import pandas as pd
from app_helper import data_type, selected_features


app = Flask(__name__)

# Load your trained model
model = dill.load(open('flask_dt_model.dill', 'rb'))

# Define a route to render the HTML form
@app.route('/')
def home():
    return render_template('upload.html')

# Define a route to handle file upload and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']
        
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return "No selected file"

        if file:
            # Read the CSV file
            X = pd.read_csv(file, low_memory=False, dtype=data_type)
            X = X[selected_features]
            
            # Make predictions
            predictions = model.predict(X)
            
            # You can return the predictions in any format you want
            return str(predictions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
