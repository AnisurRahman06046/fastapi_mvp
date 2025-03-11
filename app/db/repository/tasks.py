from sqlalchemy.orm import Session 
from app.models.task import Task
from app.schemas.taskSchema import TaskCreate


def createTask(db:Session,task:TaskCreate):
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def getTasks(db:Session):
    return db.query(Task).all()

def get_taskBy_id(db:Session,task_id:int):
    return db.query(Task).filter(Task.id==task_id).first()

def deleteTask(db:Session,task_id:int):
    task = db.query(Task).filter(Task.id==task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return True 
    return False