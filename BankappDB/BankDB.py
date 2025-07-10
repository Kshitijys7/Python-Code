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

    def withdraw_money(accno,amount):
        try:
            query='select bal from practice4 where ano=:accno'
            c1.execute(query,{'accno':accno})
            row=c1.fetchone()
            new_bal=row[0]-amount
            query='update practice4 set bal=:n where ano=:accno'
            c1.execute(query,{'n':new_bal,'accno':accno})
            orcl.commit()
            return new_bal

        except Exception as e:
            print(e)

    def deposit_money(accno,amount):
        try:
            query='select bal from practice4 where ano=:accno'
            c1.execute(query,{'accno':accno})
            row=c1.fetchone()
            new_bal=row[0]+amount
            query='update practice4 set bal=:n where ano=:accno'
            c1.execute(query,{'n':new_bal,'accno':accno})
            orcl.commit()
            return new_bal

        except Exception as e:
            print(e)

    def search(accno):
        try:
            query='select cname from practice4 where ano=:accno'
            c1.execute(query,{'accno':accno})
            row=c1.fetchone()
            cname=row[0]
            return cname

        except Exception as e:
            print(e)

    def transfer_money(ano_sender,ano_receiver,amount):
        try:
            query='select bal from practice4 where ano=:ano_sender'
            c1.execute(query,{'ano_sender':ano_sender})
            row=c1.fetchone()
            bal=row[0]
            new_bal_sender=bal-amount

            query='select bal from practice4 where ano=:ano_receiver'
            c1.execute(query,{'ano_receiver':ano_receiver})
            row=c1.fetchone()
            bal=row[0]
            new_bal_receiver=bal+amount

            query='update practice4 set bal=:new_bal_sender where ano=:ano_sender'
            c1.execute(query, {'new_bal_sender':new_bal_sender,'ano_sender': ano_sender})
            orcl.commit()

            query = 'update practice4 set bal=:new_bal_receiver where ano=:ano_receiver'
            c1.execute(query, {'new_bal_receiver':new_bal_receiver,'ano_receiver': ano_receiver})
            orcl.commit()

            return new_bal_sender

        except Exception as e:
            print(e)

    def display_data(accno):
        try:
            lstdata=[]
            query='select*from practice4 where ano=:accno'
            c1.execute(query,{'accno':accno})
            for row in c1:
                lstdata.append(row)

            return lstdata

        except Exception as e:
            print(e)

    def delete_record(accno):
        try:
            query='delete from practice4 where ano=:accno'
            c1.execute(query,{'accno':accno})
            orcl.commit()
            return True

        except Exception as e:
            print(e)

