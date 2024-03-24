from pydantic import BaseModel
from typing import Optional 


class StudentItem(BaseModel):
    studentId: Optional[int] = None
    name: str
    age: int = None
    grade: int




students = [
    {
        "studentId":0,
        "name":"Ali",
        "age":20,
        "grade":1
    },
        {
        "studentId":1,
        "name":"Ahmad",
        "age":22,
        "grade":5
    },
            {
        "studentId":2,
        "name":"Basit",
        "age":24,
        "grade":4
    },
                {
        "studentId":3,
        "name":"Arham",
        "age":19,
        "grade":8
    },
                    {
        "studentId":4,
        "name":"Bilal",
        "age":18,
        "grade":9
    },
]


def response(success,data,message = ""):
    return {
        "success":success,
        "data":data,
        "message":message
    }