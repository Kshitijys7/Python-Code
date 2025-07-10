import os
os.chdir("C:\Oracle\instantclient_12_1")
import cx_Oracle
orcl = cx_Oracle.connect('system/tyger@localhost')
print("Connected to Oracle: " + orcl.version)
print('Hi')

c1=orcl.cursor()


try:
    qry = "INSERT INTO empp values('Kshitij','Singanjude')"
    c1.execute(qry)
    orcl.commit()
    print('Record inserted')

    qry = "INSERT INTO empp values('Suraj','Gaikwad')"
    c1.execute(qry)
    orcl.commit()
    print('Record inserted')

    qry = "select * from empp"
    c1.execute(qry)
    orcl.commit()
    for row in c1:
        print(row)

    qry="update empp set FIRSTNAME='Yadao' where LASTNAME='Singanjude'"
    c1.execute(qry)
    orcl.commit()
    print('Record updated successfully..........')

    qry = "select * from empp"
    c1.execute(qry)
    orcl.commit()
    for row in c1:
        print(row)

    qry="delete from empp where lastname='Gaikwad'"
    c1.execute(qry)
    orcl.commit()
    print('Record deleted successfully...........')


    qry = "select * from empp"
    c1.execute(qry)
    orcl.commit()
    for row in c1:
        print(row)


except:
    orcl.rollback()

print('Complete.....')




orcl.close()