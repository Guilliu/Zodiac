import string, random
from flask import Flask, render_template

abc = list(string.ascii_letters) + list(string.digits)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def prueba(): 
    return render_template('index.html')

@app.route('/', methods=['POST'])
def random_key():
    personal_key = ''
    for i in range(10):
        personal_key += abc[random.randint(0, len(abc)-1)]
    return render_template('index.html', personal_key=personal_key)

if __name__ == '__main__':
    app.run(port=3000, debug=True)

