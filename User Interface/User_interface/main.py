# main.py
from flask import Flask, render_template, request


import pickle

# Load data from a file
with open('rf.pkl', 'rb') as file:
    loaded_data = pickle.load(file)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')



@app.route('/get_data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        # Access form data using request.form
        location = request.form['location']
        furnishing_status = request.form['furnishing_status']
        room_select = request.form['roomSelect']
        num_bathroom = request.form['Number_of_Bathroom']
        Number_of_Rooms = request.form['Number_of_Rooms']
        covered_parking = request.form['Covered_Parking']
        view_select = request.form['viewSelect']
        balcony = request.form['balcony']
        uncovered_parking = request.form['Uncovered_Parking']
        park = request.form['Park']
        crime = 0
        hospital = request.form['hospital']
        playgrounds = request.form['Playgrounds']

        import pandas as pd
        data = [location,Number_of_Rooms,furnishing_status,num_bathroom,covered_parking,room_select,view_select,balcony,uncovered_parking,park,playgrounds,crime,hospital]
        print(data)
        column_names = ['Locality',   'Number of Rooms','Furnishing Status',
       'Number of Bathroom', 'Covered Parking',  'Additional Rooms','View',
       'Balcony', 'Open/Uncovered Parking', 'park1',
       'Playgrounds1',  'crime','hospital']
        df = pd.DataFrame([data], columns=column_names)

        result=loaded_data.predict(df.values.reshape(1, -1))

        # Process the form data as needed (e.g., store in a database)


        print(f" {result}")
        result=int(result[0])

        return render_template('index.html',data=result)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('your_template.html')

