import uvicorn
from fastapi import FastAPI
from loandataset import loandataset
import pickle
from keras.models import model_from_json
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_loan(data:loandataset):
    data = data.dict()
    Gender=data['Gender']
    Married=data['Married']
    Dependent=data['Dependent']
    Education=data['Education']
    Self_Employed=data['Self_Employed']
    ApplicantIncome=data['ApplicantIncome']
    CoapplicantIncome=data['CoapplicantIncome']
    LoanAmount=data['LoanAmount']
    Loan_Amount_Term=data['Loan_Amount_Term']
    Credit_History=data['Credit_History']
    Property_Area=data['Credit_History']
    prediction = classifier.predict([[Gender,Married,Dependent,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
    if(prediction[0]==1):
        prediction="Loan can be Sanctioned"
    else:
        prediction="Loan can not be Sanctioned"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)