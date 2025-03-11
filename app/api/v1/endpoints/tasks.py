from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session 
from app.db.session import get_db 
from app.schemas.taskSchema import TaskCreate,TaskResponse
from app.db.repository.tasks import createTask,getTasks,get_taskBy_id,deleteTask


router = APIRouter()

@router.post("/",response_model=TaskResponse)
def create(task:TaskCreate,db:Session=Depends(get_db)):
    return createTask(db,task)

@router.get("/all",response_model=list[TaskResponse])
def getAll(db:Session=Depends(get_db)):
    return getTasks(db)


@router.get("/{task_id}",response_model=TaskResponse)
def getTask(task_id:int,db:Session=Depends(get_db)):
    task = get_taskBy_id(db,task_id)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task 

@router.delete("/{task_iid}")
def remove(task_id:int,db:Session=Depends(get_db)):
    if not deleteTask(db,task_id):
        raise HTTPException(status_code=404,detail="Task is not found or already deleted")
    return {"message":"Task is deleted"}