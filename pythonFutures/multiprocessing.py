import concurrent.futures
import time
import requests
import json

def task(x):
    #Assume that you have deployed your model in your local computer as a flask kind of application. All predictions will happen in local only
    url="http://localhost:8000/prediction"
    headers = {"content-type": "application/json"}
    data=json.dumps({"input":x})
    #Assume the model is deployed and an API is there to listen the incoming request in post entry point
    prediction = requests.post(url, headers=headers, data=data)
    return prediction


#sameple inputs for prediction. Consider the length of the list is 50.
values=["Alexa switch on the tv","Hey alexa, play a song","Alexa call Anna"," ", " "]
prediction=[]
with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    #submit returns a future object. It is a acknowledgement about exectution of tasks in multithread
    futures=[executor.submit(task,value) for value in values]
    #as_completed is used to fetch the results as when each input is completed.
    for future in concurrent.futures.as_completed(futures):
        prediction.append(future.results())