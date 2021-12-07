import uvicorn
from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

class loandataset(BaseModel):
    Gender: int 
    Married: int 
    Dependent: int 
    Education: int
    Self_Employed: int 
    ApplicantIncome: int 
    CoapplicantIncome: int 
    LoanAmount: int
    Loan_Amount_Term: int
    Credit_History: int 
    Property_Area: int 
    
@app.get('/')
def msg():
    return {"message":"Hello Everyone"}


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


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)