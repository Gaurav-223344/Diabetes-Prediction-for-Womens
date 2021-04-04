from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Pregnancies=int(request.form['pregnant'])
        Glucose=int(request.form['glucose'])
        BloodPressure=int(request.form['bloodpressure'])
        SkinThickness=int(request.form['thickness'])
        Insulin=float(request.form['insulin'])
        weight=float(request.form['weight'])
        height=float(request.form['height'])
        BMI=weight/height**2
        DiabetesPedigreeFunction=int(request.form['pedigree'])
        Age=int(request.form['age'])
        
        
        prediction=model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        output=(prediction[0])
        if output==0:
            return render_template('index.html',prediction_texts="You Don't Have Diabetes")
        else:
            return render_template('index.html',prediction_texts="You Have Diabetes")
    
        
        
    else:
        return render_template('index.html')

    
    
if __name__=="__main__":
    app.run(debug=True)
    
    
# if __name__=="__main__":
#     app.run(host='0.0.0.0',port=8080)
        
