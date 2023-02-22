import joblib
import os
import json
import sklearn
import pandas as pd

"""
Deserialize fitted model using model_fn
"""
def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "scikit_model.pkl"))
    return model

"""
input_fn
    request_body: The body of the request sent to the model.
    request_content_type: (string) specifies the format/variable type of the request
"""
def input_fn(request_body, request_content_type):
    if request_content_type == 'application/json':
        request_body = json.loads(request_body)
        inpVar = request_body
        return inpVar
    else:
        raise ValueError("This model only supports application/json input")

"""
predict_fn
    input_data: returned array from input_fn above
    model (sklearn model) returned model loaded from model_fn above
"""
def predict_fn(input_data, model):
    cols=[]
    for i in range(0,3):
        columns=model.named_steps['preprocessor'].transformers_[i][2]
        cols = cols+columns
    df=pd.DataFrame(input_data['Input'],columns=input_data['Headers'])
    df_score=df[cols].copy()
    return model.predict_proba(df_score)

"""
output_fn
    prediction: the returned value from predict_fn above
    content_type: the content type the endpoint expects to be returned. Ex: JSON, string

"""

def output_fn(prediction, content_type):
    res = prediction.tolist()
    respJSON = {'Output': res}
    return respJSON