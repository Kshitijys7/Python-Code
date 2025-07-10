import os
os.chdir("C:\Oracle\instantclient_12_1")
import cx_Oracle

orcl=cx_Oracle.connect('system/tyger@localhost')
print('Connected to:'+orcl.version)
c2=orcl.cursor()


def createTable():
    query = 'create table practice2(id int,firstname varchar(20),lastname varchar(20),salary int)'

    try:
        c2.execute(query)
        orcl.commit()
        print('Table created.....')

    except:
        print('Error')

def insertValues():
    try:
        query = 'insert into practice2 values(:1,:2,:3,:4)'
        emp = [(101, "Suraj", "Gaikwad", 25000), (102, "Chaitanya", "Bandaru", 30000), (103, "Sachin", "Bandal", 35000),
               (104, "Shubham", "Pasar", 25000)]
        c2.executemany(query,emp)
        orcl.commit()

    except Exception as e:
        print(e)

    else:
        print('Insert completed.....')

def updateValues():
    try:
        query='update practice2 set salary=40000 where id=102'
        c2.execute(query)

        print('Record updated successfully.....')
        orcl.commit()

    except Exception as e:
        print(e)

def deleteRecord():
    try:
        query='delete from practice2 where id=104'
        c2.execute(query)
        print('Record deleted.....')
        orcl.commit()

    except Exception as e:
        print(e)

def searchRecord():
    try:
        query='select*from practice2 where id=101'
        c2.execute(query)
        print(c2)
        for row in c2:
            print(row[1])

    except Exception as e:
        print(e)

def verification(id,firstname):
    try:
        query='select firstname from practice2 where id=:id'
        c2.execute(query,{'id':id})
        row=c2.fetchone()
        cust_name=row[0]

        if cust_name==firstname:
            print('Valid.....')

        else:
            print('Invalid id or name.....')

    except Exception as e:
        print(e)

def displayall():
    try:
        query='select*from practice2'
        c2.execute(query)
        for row in c2:
            print(row)

    except Exception as e:
        print(e)

while(True):
    print('1.Create table\n2.Insert records\n3.Update record\n4.Delete record\n5.Search record\n6.Display all records\n7.Verify')
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

    elif ch==7:
        id=int(input('Enter id:'))
        firstname=input('Enter firstname:')
        verification(id,firstname)

    else:
        print('Invalid choice.......')

    print('Do you want to continue?? press 1')
    choice=input()

    if choice!='1':
        break