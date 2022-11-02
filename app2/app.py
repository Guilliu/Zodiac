import _pickle, pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def prueba(): 
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():

    personal_key = request.form['text']

    pickle_file = open('modelo_zodiac.pckl', 'rb')
    modelo = _pickle.load(pickle_file)
    pickle_file.close()

    url ="https://docs.google.com/spreadsheets/d/1W5IpWS3Zk8ND5aZvcopASpi5VsfkMiSzMQATlqfdf_4/export?format=csv&gid=574570074"

    data = pd.read_csv(url, names=['timestamp', 'name'] + list(range(50)), skiprows = [0])
    data = data[data.name == personal_key]

    X = data[data.columns[2:]]
    X.columns = [str(i) for i in X.columns]

    prediction = modelo.predict(X)[0]

    if prediction in (0, 2): prediction += 2
       
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(port=4000, debug=True)



