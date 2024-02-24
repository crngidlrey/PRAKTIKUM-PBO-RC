studentGrade = {} #create empty dictionary
numberOfStudent = int(input("masukkan jumlah mahasiswa: "))

#looping for input the student data
for i in range (numberOfStudent):
    name = input ("nama: ")
    grade = int(input ("grade: "))
    #add the new entry to dictionary
    #name = key
    #grade = value
    studentGrade[name] = grade

print (studentGrade)