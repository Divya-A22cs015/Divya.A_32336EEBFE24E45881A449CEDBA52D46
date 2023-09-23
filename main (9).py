#Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.

class Student:
  def __init__(self, name,roll_number, cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

def sort_students(student_list):
  Sorted_Students=sorted(student_list,
                      key=lambda student: student.cgpa,
                      reverse=True)
  return Sorted_Students
students=[Student("Mahalakshmi", "A123", 9.7),
         Student("Gayathri", "A126", 8.5),
         Student("Divya", "A125", 9.5),
         Student("Lavanya", "A126", 8.7)]
Sorted_Students=sort_students(students)

#print the sorted llist of students:
for student in Sorted_Students:
  print("Name: {}, Roll Number: {}, CGPA:{}".format(student.name, student.roll_number, student.cgpa))
