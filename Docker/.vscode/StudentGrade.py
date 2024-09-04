#Asignment-2 Student result (Grading)
school_name: str = "        IMCB I-10/2, Islamabad        "
student_name: str = "Imtiaz Alam"
student_rollno: int = "Roll No:         12560"
class_name: str = "Class :       9th"
English : float = 93
Urdu : float = 91
Physics : float = 94
Chemistery : float =86.6
Pakstudy : float = 92
print(F"School Name= {school_name} \nStudent Name = {student_name}\n{student_rollno}\n{class_name}\nEnglish =  {English}\nUrdu =  {Urdu}\nPhysics =  {Physics}\nChemistery =  {Chemistery}\nPakstudy =  {Pakstudy}\n")
Total_Marks = 500
Obtaine_Marks = English+Urdu+Physics+Chemistery+Pakstudy
print("Total Marks = ",Total_Marks)
print(f"Obtaine_Marks = {Obtaine_Marks} ")
average = float((Obtaine_Marks/Total_Marks)*100)
print("Average =" ,average)
if average >=90:
  print("Grade =", 'A+')
if average <90  >80 :
  print("Grade =", 'A')
if average <80 :
  print("Grade =", 'B')