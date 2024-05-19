import codepost
import os
from dotenv import load_dotenv

load_dotenv()

#Code to get the comments forma a specific submission
api_key = os.getenv('API_KEY')

#API Token
codepost.configure_api_key(api_key)

#All avaiable courses
all_courses = codepost.course.list_available()

#Get the course Id
group_id = all_courses[0].id

#Retrieve the course
my_course = codepost.course.retrieve(id=group_id)
#print(my_course)

#Get the Id of one assignment
assignment_id = my_course.assignments[0]
#print("\n")

#Get all the submissions for that assignment
my_submissions = codepost.assignment.list_submissions(id=assignment_id.id)

#Get the submission of 1 student
sub_id = my_submissions[0].id
student_submission = codepost.submission.retrieve(id=sub_id)
print(student_submission)
print("\n")

#Get the student emial for later
student_email = student_submission.students[0]

#Get the file of that submission
file_id = student_submission.files[0]
print(file_id.id)
my_file = codepost.file.retrieve(id=file_id.id)
print(my_file)
print("\n")

#Get the comments object from that submission
comments_ids = my_file.comments

#Print all the comments of that submission file
print("Student " + student_email)
for i in range(0,len(comments_ids)):
    print("Line " + str(comments_ids[i].startLine) + ": " + comments_ids[i].text)



