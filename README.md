# Song Hit/Flop Prediction Project

## Overview
This project aims to predict whether a song will be a **Hit** or a **Flop** based on various musical and technical attributes like acousticness, danceability, energy, tempo, valence, and more. By analying these features and training several machine learning classification models, we developed a system that identifies key patterns influencing a song's success. The best-performing model was saved and deployed as a web application using Flask, making it accessible for public use. The app has been hosted on **Render**.

You can access the deployed project here:  
[Song Hit/Flop Prediction Web App](https://spotify-song-prediction-app.onrender.com/)

## Project Structure

### 1. Exploratory Data Analysis (EDA)
- Conducted detailed analysis of features to undestand their individual statistical properties.

### 2. Data Preprocessing
- Handled missing values and outliers for clean and consistent data.

### 3. Model Training and Evaluation
- Trained several machine learning models for classification:
  - **Decision Tree**
  - **Random Forest**
  - **Extra Trees**
  - **Bagging**
  - **AdaBoost**
- Evaluated models using metrics:
  - **Accuracy** for predictive performance.
  - **ROC-AUC score** to have a comprehensive measure of a classification model's ability to distinguish between positive and negative classes.
- Saved the best-performing model as a `pickle` file for deployment.

### 4. Deployment
- Built a Flask-based web application that allows users to input song attributes and receive predictions.
- Deployed the application on **Render**, ensuring easy accessibility for users.

## Data Source
The dataset for this project was sourced from Kaggle, providing a rich collection of features for songs, making it ideal for building and evaluating classification models. Dataset can be accessed through [Spotify Dataset](https://www.kaggle.com/datasets/bricevergnou/spotify-recommendation)


## Dependencies Installation
To run the project locally, install the necessary dependencies in the new virtual environment using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

The requirement files for the deployment and running the flask app are provided in the `apprequirements.txt` file. To install the Flask App requirements run the following code in your terminal with active environment variable:
```bash
pip install -r apprequirements.txt
```
### Running the Project Locally

## Steps to Execute

**EDA and Feature Engineering**

1. Open the `Spotify-Music-Prediction.ipynb` file in Jupyter Notebook or Anaconda.
2. Run all cells sequentially to perform the following tasks:
    * Exploratory Data Analysis (EDA)
    * Preprocess the data
    * Engineer features for model training

**Model Training and Evaluation**

1. Train various machine learning models as described in the notebook.
2. Evaluate the models and save the best-performing one for deployment.

**Web Application**

1. Run the Flask application locally using the `app.py` file:

```bash
python app.py
```

## Contact

For any questions or feedback, please contact Ritik Suri at [Ritik1704@gmail.com](mailto:Ritik1704@gmail.com).
