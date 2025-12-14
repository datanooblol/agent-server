from pydantic import BaseModel
from typing import Any

class PlotlyData(BaseModel):
    data:Any
    layout:Any