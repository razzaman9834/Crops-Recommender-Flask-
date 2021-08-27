from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('C://Users//KIIT//Desktop//dspr//deploy-ml-model-flask//model.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def home():
    data1 = float(request.form['a'])
    data2 =float(request.form['b'])
    data3 = float(request.form['c'])
    data4 = float(request.form['d'])
    data5 =float(request.form['e'])
    data6 =float(request.form['f'])
    data7 =float(request.form['g'])

    arr = np.array([[data1, data2, data3, data4, data5,data6,data7]])
    pred = model.predict(arr)
    print(pred[0])
    return render_template('home.html', data=pred[0])


if __name__ == "__main__":
    app.run(debug=True)















