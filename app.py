from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import webbrowser  # Import webbrowser to open the browser

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

## Route for the default page
@app.route('/')
def index():
    return render_template('home.html')

## Route for prediction page
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            return render_template('home.html', results=results[0])
        except Exception as e:
            print(f"Error: {e}")
            return render_template('home.html', results="Error occurred")

if __name__ == "__main__":
    # Open browser to /predictdata on startup
    webbrowser.open('http://127.0.0.1:5000/predictdata')
    app.run(host="0.0.0.0", port=5000, debug=True)