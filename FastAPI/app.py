from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app=FastAPI()

"""
Below end point accepts get request in the mentioned path
with a default response code to be 200.
Note that in function def we define input argument of type order that
that we defined using pydantic in schema.py file
"""

@app.get("/getstatus")
def returnstatus(details: order):
    data=details.dict()
    try:
        #prepare query from the input and fetch report from db
        qry=f"select status from ordertable where customerId={data['CCustomerId']} \
	      and OrderId={data['Orderdetails'][0]['OrderId']} and Orderdate={data['Orderdetails'][0]['OrderDate']} "
        # Mimcing the db response for demo
        response,code= "Despatched" ,200
    except Exception as e:
        response,code="Exception occured due to "+  str(e),500 # internal error
    response=jsonable_encoder({"message":response})
    return JSONResponse(content=response,status_code=code)




