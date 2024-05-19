import codepost
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

#Code to get the comments from all the submissions from a specific assignment

#API Token
codepost.configure_api_key(api_key)

#All avaiable courses
all_courses = codepost.course.list_available()

#Get the courses ids and names for the professor to choose
"""for i in range(0,len(all_courses)):
    print(str(all_courses[i].id) + " " + all_courses[i].name)"""

#Get the course Id
group_id = all_courses[0].id

#Retrieve the course
my_course = codepost.course.retrieve(id=group_id)
#print(my_course)

#Get the Id and names of the assignments
assignment_id = my_course.assignments[0]
for i in range(0,len(my_course.assignments)):
    print(str(my_course.assignments[i].id) + " " + my_course.assignments[i].name)
    
#print("\n")
#Get the assignment the specific assignemt
choice = int(input("Choose an assignment: "))
my_assignment = codepost.assignment.retrieve(id=choice)
print("Assignment " + str(choice) + " " + my_assignment.name)

#Get the submissions from that assignment
submissions = codepost.assignment.list_submissions(id=choice)
#print("\n")
#print(submissions)

#Get the submissions code, file id and student email
submissions_codes = []
students_emails = []
files = []
for i in range(0,len(submissions)):
    submissions_codes.append(submissions[i].id)
    students_emails.append(submissions[i].students)
    files.append(submissions[i].files[0].id)

"""print(submissions_codes)
print(files)
print(students_emails)"""

#Get the comments from each file
for i in range(0, len(files)):
    emails = ""

    for j in range(0,len(students_emails[i])):
        #print("Student " + students_emails[i][j])
        emails = emails + students_emails[i][j] + " "

    filename = f"Comentarios_{emails}.txt"

    my_file = codepost.file.retrieve(id=files[i])
    comments_ids = my_file.comments

    sorted_comments = sorted(comments_ids, key=lambda comment: comment.startLine)

    with open(filename, 'w', encoding='utf-8') as file:
            for comment in sorted_comments:
                line = f"Line {comment.startLine}: {comment.text}\n"
                file.write(line)
                #print(line, end="")

    """for comment in sorted_comments:
        print(f"Line {comment.startLine}: {comment.text}")"""

    #print("\n")

print("Comments to txt done")
