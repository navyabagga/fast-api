# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:06:48 2021

@author: bagga
"""

from pydantic import BaseModel
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