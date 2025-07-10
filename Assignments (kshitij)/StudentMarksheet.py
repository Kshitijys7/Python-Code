Rollno=int(input('Enter student roll number:'))
Name=input('Enter name of student:')
sub1=int(input('Enter marks for subject 1:'))
sub2=int(input('Enter marks for subject 2:'))
sub3=int(input('Enter marks for subject 3:'))

total=sub1+sub2+sub3
perct=(total/300)*100

print('Roll number:',Rollno)
print('Name:',Name)
print('Maths:',sub1)
print('Science:',sub2)
print('English',sub3)

print('Percentage:',perct)

if perct<40:
    Grade=''
elif perct>=40 and perct<=50:
    Grade='C'
elif perct>50 and perct<=65:
    Grade='B'
elif perct>65 and perct<80:
    Grade='B+'
elif perct>=80 and perct<=90:
    Grade='A'
elif perct>90:
    Grade='A+'

print('Roll Number\t\tName\t\tMaths\t\tElectrical\t\tComputer\t\tTotal\t\tPerct\t\t\tGrade')
print({Rollno},'\t\t',{Name},'\t\t',{sub1},'\t\t',{sub2},'\t\t',{sub3},'\t\t',{total},'\t\t',{perct},'\t\t\t',{Grade})