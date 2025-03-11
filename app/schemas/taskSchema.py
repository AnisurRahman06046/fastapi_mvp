from pydantic import BaseModel 
from typing import Optional 

class TaskCreate(BaseModel):
    title:str 
    description:Optional[str]=None
    completed:bool=False
    
class TaskResponse(TaskCreate):
    id:int 
    class Config:
        orm_mode=True