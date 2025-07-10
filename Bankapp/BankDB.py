import os
os.chdir("C:\Oracle\instantclient_12_1")
import cx_Oracle
orcl=cx_Oracle.connect('system/tyger@localhost')
print('Connected to:'+orcl.version)

c1=orcl.cursor()

class BankDB:
    def insertValues(ano,cname,bal,nameofarg,maxNOT,type):
        try:
            query = 'insert into practice4 values(:1,:2,:3,:4,:5,:6)'

            cust=[]
            cust.extend((ano,cname,bal,nameofarg,maxNOT,type))
            print(cust)
            c1.execute(query,cust)
            print('Record inserted.....')
            orcl.commit()
            cust.clear()

        except Exception as e:
            print(e)

        else:
            print('Insert completed.....')

    def verification(accno,custname):
        try:
            query="select ano from practice4 where cname=:custname"
            c1.execute(query,{'custname':custname})
            row=c1.fetchone()
            accno_db=row[0]

            if(accno_db==accno):
                return True
                #print('Valid.....')

            else:
                return False
                #print('Invalid name or account no.....')

        except Exception as e:
            print(e)


