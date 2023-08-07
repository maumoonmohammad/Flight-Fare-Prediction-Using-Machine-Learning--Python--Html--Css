import numpy as np
from flask import Flask,request,render_template
import pandas as pd
import numpy as np
import pickle
# app=Flask(__name__)
app = Flask(__name__, static_url_path='/static')

model=pickle.load(open('flight_fare_prediction1.pickle','rb'))
model1=pickle.load(open('input_flight_fare1.pickle','rb'))

@app.route('/')
def home():
    return render_template('Flight_price.html')
@app.route('/predict',methods=['POST'])
def predict():
    dep_date=request.form['departdate']
    dep_day=int(pd.to_datetime(dep_date,format='%Y-%m-%d').day)
    dep_mnth=int(pd.to_datetime(dep_date,format='%Y-%m-%d').month)

    dep_time=request.form['departtime']
    dep_hr=int(pd.to_datetime(dep_time,format='%H:%M').hour)
    dep_mn=int(pd.to_datetime(dep_time,format='%H:%M').minute)


    arr_time=request.form['arrivaltime']
    arr_hr=int(pd.to_datetime(arr_time,format='%H:%M').hour)
    arr_mn=int(pd.to_datetime(arr_time,format='%H:%M').minute)

    no_stops=int(request.form['stops'])

    final_array=np.zeros(30)

    final_array[0]=no_stops
    final_array[2]=dep_hr
    final_array[3]=dep_mn
    final_array[4]=arr_hr
    final_array[5]=arr_mn
    final_array[6]=dep_day
    final_array[7]=dep_mnth

    source_flight=request.form['source']
    destination_flight=request.form['destination']
    airline_company=request.form['airline']
    index_source=np.where(model1.columns==source_flight)[0][0]
    index_destination=np.where(model1.columns==destination_flight)[0][0]
    index_airline=np.where(model1.columns==airline_company)[0][0]
    if index_airline>=0 and index_destination>=0 and index_source>=0:
        final_array[index_source]=1
        final_array[index_airline]=1
        final_array[index_destination]=1

    pred=model.predict([final_array])
    out=round(pred[0],2)
    if source_flight==destination_flight:
        return render_template('Flight_price.html', flight_price=f'the source and the destination locations are same please choose different locations')
    else:
        return render_template('Flight_price.html',flight_price=f'The ticket price is {out}')
app.run(debug=True)