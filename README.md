# Flight Fare Prediction (Machine Learning)

A machine learning web application that predicts flight fares. A Random Forest model is trained in a Jupyter notebook, saved with pickle, and served through a Flask web app where users enter their flight details into a form to get a predicted ticket price.

## How It Works

1. **Data** — The model is trained on a Kaggle dataset of domestic flight fares (`Data_Train.xlsx`).
2. **Preprocessing** — Date and time columns are broken into numeric features (day, month, hour, minute), categorical columns (airline, source, destination) are one-hot encoded, and special characters in the data are cleaned.
3. **Model** — A `RandomForestRegressor` from scikit-learn, with hyperparameters tuned using `GridSearchCV` and `RandomizedSearchCV`.
4. **Persistence** — The trained model and the feature-column template are saved as pickle files (`flight_fare_prediction1.pickle` and `input_flight_fare1.pickle`).
5. **Serving** — The Flask app loads the pickled model, takes the user's inputs from a form, builds the matching feature vector, and returns the predicted fare. It also checks that the source and destination are not the same.

## Inputs

The prediction form takes: departure date, departure time, arrival time, number of stops, source, destination, and airline.

## Tech Stack

- **Machine learning:** Python, scikit-learn, pandas, NumPy, Jupyter Notebook, pickle
- **Back end:** Flask
- **Front end:** HTML, CSS, Bootstrap 5

## Getting Started

### Prerequisites
- Python 3.9

### Setup

```bash
# Clone the repository
git clone https://github.com/maumoonmohammad/Flight-Fare-Prediction-Using-Machine-Learning--Python--Html--Css.git
cd Flight-Fare-Prediction-Using-Machine-Learning--Python--Html--Css

# Install dependencies
pip install flask scikit-learn pandas numpy openpyxl
```

### Run

```bash
python Flask_app.py
```

Then open the local server URL shown in the terminal (by default `http://127.0.0.1:5000/`), fill in the flight details, and submit to get the predicted fare.

## Project Structure

- `Flask_app.py` — Flask web server that loads the model and serves predictions
- `machine_learning_model.ipynb` — Jupyter notebook with the full data cleaning, training, and tuning workflow
- `flight_fare_prediction1.pickle` — the trained Random Forest model
- `input_flight_fare1.pickle` — the feature-column template used to build the input vector
- `Data_Train.xlsx` — the training dataset
- `templates/` — the HTML form (`Flight_price.html`)
- `static/` — CSS and image assets
