from fastapi import FastAPI
from helperModule import students,response,StudentItem

app = FastAPI()

# default route
@app.get('/')
async def read_root():
     return {'message':'Hello, FastAPI!'}


# get all students route
@app.get('/students')
async def getStudents():
    return response(True,students,'successfully get all students')


# get specific students route
@app.get('/students/{student_id}')
async def getStudents(student_id):
        
   def find_student_by_id(student_id):
     for student in students:
        if student["studentId"] == int(student_id):
            return student
     return None 
    
   foundStudent = find_student_by_id(student_id)

   if foundStudent != None:
        return response(True,foundStudent,"successfully student found")
   else:
        return response(False,{},"student not found with this student_id")
       
       
# add new student
@app.post('/students/add')
async def addStudent(student:StudentItem):
    
    length = len(students)
    student.studentId = length
    
    students.append(student)
    
    return response(True,students,"Updated Students List")


# delete student
@app.delete('/students/delete/{student_id}')
async def addStudent(student_id):
    
    def studentExist():
        for student in students:
            if student["studentId"] == int(student_id):
                return student
            else:
                return None
            
    if studentExist() != None:       
        filtered_list = filter(lambda a: a["studentId"] != int(student_id) ,students) 
        return response(True,list(filtered_list),"Deleted successfully")
    else:
        return response(False,[],"student not found with this student_id")


# update a student
@app.put('/students/update/{student_id}')
async def updateStudent(student_id,student:StudentItem):
        
    def find_student_index_by_id(target_id):
        for index, student in enumerate(students):
            if student["studentId"] == int(target_id):
                return index
        return -1
    
    foundIndex = find_student_index_by_id(student_id)
    if foundIndex != -1:
        updated_student = student 
        updated_student.studentId = int(student_id)
        students[foundIndex] = updated_student
        return response(True,updated_student,"Updated student successfully")
    else:
        return response(False,{},"student not found with this student_id")