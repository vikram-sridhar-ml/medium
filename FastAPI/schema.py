from datetime import datetime
from pydantic import BaseModel

from typing import (
	List
)

class OrderDetails(BaseModel):
	OrderId: str
	OrderDate: datetime

class order(BaseModel):
	CustomerId :  int
	Orderdetails: List[OrderDetails]
