import os
os.chdir("C:\Oracle\instantclient_12_1")
import cx_Oracle

orcl=cx_Oracle.connect('system/tyger@localhost')
print('Connected to:'+orcl.version)
c2=orcl.cursor()


def createTable():
    query = 'create table practice3(id int,firstname varchar(20),lastname varchar(20),salary int)'

    try:
        c2.execute(query)
        orcl.commit()
        print('Table created.....')

    except:
        print('Error')

def insertValues():
    try:
        query = 'insert into practice3 values(:1,:2,:3,:4)'

        '''emp = [(101, "Suraj", "Gaikwad", 25000), (102, "Chaitanya", "Bandaru", 30000), (103, "Sachin", "Bandal", 35000),
               (104, "Shubham", "Pasar", 25000)]
        '''
        n=int(input('Enter the number of entries you want:'))
        emp=[]
        for i in range(n):
            id=int(input('Enter id:'))
            firstname=input('Enter firstname:')
            lastname = input('Enter lastname:')
            salary=int(input('Enter salary:'))
            emp.extend((id,firstname,lastname,salary))
            print(emp)
            c2.execute(query,emp)
            print('Record inserted.....')
            orcl.commit()
            emp.clear()

    except Exception as e:
        print(e)

    else:
        print('Insert completed.....')

def updateValues():
    try:
        while(True):
            print('1.Update Firstname\n2.Update Lastname\n3.Update salary')
            ch = int(input('Enter your choice'))

            if ch==1:
                id = int(input('Enter the id:'))
                firstname = input('Enter the new firstname:')
                query='update practice3 set firstname=:f where id=:i'
                c2.execute(query,{'f': firstname, 'i': id})

                print('Record updated successfully.....')
                orcl.commit()

            elif ch==2:
                id = int(input('Enter the id:'))
                lastname = input('Enter the new lastname:')
                query = 'update practice3 set lastname=:l where id=:i'
                c2.execute(query, {'l': lastname, 'i': id})

                print('Record updated successfully.....')
                orcl.commit()

            elif ch==3:
                id = int(input('Enter the id:'))
                salary = int(input('Enter the new salary:'))
                query = 'update practice3 set salary=:s where id=:i'
                c2.execute(query, {'s': salary, 'i': id})

                print('Record updated successfully.....')
                orcl.commit()

            else:
                print('Invalid choice.......')

            print('Do you want to continue?? press 1')
            choice = input()

            if choice != '1':
                break

    except Exception as e:
        print(e)

def deleteRecord():
    try:
        id=int(input('Enter the id for the record you want to delete:'))

        query='delete from practice3 where id=:i'
        c2.execute(query,{'i':id})
        print('Record deleted.....')
        orcl.commit()

    except Exception as e:
        print(e)

def searchRecord():
    try:
        id=int(input('Enter the id for the record you want to search:'))
        query='select*from practice3 where id=:i'
        print(type(c2.execute(query,{'i':id})))

        print('Record found.....')

        for row in c2:
            print(row)

    except Exception as e:
        print(e)

def displayall():
    try:
        query='select*from practice3'
        c2.execute(query)
        for row in c2:
            print(row)

    except Exception as e:
        print(e)

while(True):
    print('1.Create table\n2.Insert records\n3.Update record\n4.Delete record\n5.Search record\n6.Display all records')
    ch=int(input('Enter your choice'))

    if(ch==1):
        createTable()

    elif ch==2:
        insertValues()

    elif ch==3:
        updateValues()

    elif ch==4:
        deleteRecord()

    elif ch==5:
        searchRecord()

    elif ch==6:
        displayall()

    else:
        print('Invalid choice.......')

    print('Do you want to continue on the main menu?? press 1')
    choice=input()

    if choice!='1':
        break