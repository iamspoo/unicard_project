import mysql.connector as mc
class backend:
    def connectt(self):
        mydb=mc.connect(host="localhost",user="root",passwd="",database="unicard")
        mycursor=mydb.cursor()
        return mydb,mycursor
    
    '''ob=backend()
    conn,mycursor=ob.connectt()
    mycursor.execute("insert into person values('0000000009','2019-08-23','sammeksha','vipul','j l b','dharvad','karnataka','2345','9090904567',null,null)")
    conn.commit()'''

    def close(self,mydb,mycursor):
        mydb.close()
        mycursor.close()

    def person_insert(self,dob,fn,ln,adds,addc,addst,addp,ph,bg):
        mydb,mycursor=self.connectt()
        mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
        mydb.commit()
        mycursor.execute("insert into person values(%s,%s,%s,%s,%s,%s,%s,%s,%s,null,null,%s,null)",("default",dob,fn,ln,adds,addc,addst,addp,ph,bg))
        mydb.commit()
        self.close(mydb,mycursor)

        
    ''' add family members ration_id in person'''
    def ration_insert(self,huid,typee,nop,num):
         mydb,mycursor=self.connectt()
         mycursor.execute("insert into ration values(%s,%s,%s,%s)",("default",huid,typee,nop))
         mydb.commit()
         mycursor.execute("update person set person.p_ration_id=(select ration_id from ration where huid=%s)where uid=%s",(huid,huid))
         mydb.commit()
         '''num is a list of family members'''
         for i in range(len(num)):
             mycursor.execute("update person set person.p_ration_id=(select ration_id from ration where huid=%s)where uid=%s",(huid,i))
             mydb.commit()
         self.close(mydb,mycursor)

    '''def add_family_ration_id(self,num,'''

    '''ob=backend()
    ob.ration_insert(15,"BPL",2)'''
     

    def food_insert(self,huid,cost,doi,rq,wq,sq,oq):
         mydb,mycursor=self.connectt()
         mycursor.execute("insert into food_grains values((select ration_id from ration where huid=%s),%s,%s,%s,%s,%s,%s)",(huid,cost,doi,rq,wq,sq,oq))
         mydb.commit()
         self.close(mydb,mycursor)

    '''ob=backend()
    ob.food_insert(13,90,"2016-04-03",4,3,5,1)'''

    def transport_insert(self,uid,sp,fp,doi,doe):
        mydb,mycursor=self.connectt()
        mycursor.execute("insert into transport values(default,%s,%s,%s,%s,%s)",(uid,sp,fp,doi,doe))
        mydb.commit()
        self.close(mydb,mycursor)

    '''ob=backend()
    ob.transport_insert(13,"adhichunchunagiri stop","cbs","2019-03-23","2020-03-23")'''

    def licence_insert(self,uid,tol):
        mydb,mycursor=self.connectt()
        mycursor.execute("insert into licence values(default,%s,%s)",(uid,tol))
        mydb.commit()
        self.close(mydb,mycursor)

    '''ob=backend()
    ob.licence_insert(13,1111)'''

    def vehicle_insert(self,uid,rn,ty,y,m,mo):
        mydb,mycursor=self.connectt()
        mycursor.execute("insert into vehicle(registration_num,licence_num,type,year,make,model)values(%s,(select licence_num from licence where uid=%s),%s,%s,%s,%s)",(rn,uid,ty,y,m,mo))
        mydb.commit()
        self.close(mydb,mycursor)

    '''ob=backend()
    ob.vehicle_insert(13,"TH-08 RT-2345","four wheeler","2019","renault","vento")'''

    def lpg_insert(self,doi,dp,dc,dn,da,huid):
        mydb,mycursor=self.connectt()
        mycursor.execute("insert into lpg values(default,%s,%s,%s,%s,%s,%s)",(doi,dp,dc,dn,da,huid))
        mydb.commit()
        self.close(mydb,mycursor)

    '''ob=backend()
    ob.lpg_insert("2015-09-09",50000,1245,"kumar","adhichunchunagiri road,mysore",13)'''

    def lpg_record_insert(self,ct,dd,huid):
        mydb,mycursor=self.connectt()
        mycursor.execute("insert into lpg_record values(%s,%s,default,(select lpg_id from lpg where huid=%s))",(ct,dd,huid))
        mydb.commit()
        self.close(mydb,mycursor)

        
    '''ob=backend()
    ob.lpg_record_insert(810,"2020-09-04",13)'''


    def health_insert(self,huid,np,amount,ty,num):
        mydb,mycursor=self.connectt()
        mycursor.execute("insert into health values(default,%s,%s,%s,%s)",(huid,np,amount,ty))
        mydb.commit()
        mycursor.execute("update person set person.p_health_id=(select health_id from health where huid=%s)where uid=%s",(huid,huid))
        mydb.commit()
        ''' num is list of uid of family memebers'''
        for i in range(len(num)):
            mycursor.execute("update person set person.p_health_id=(select health_id from health where huid=%s)where uid=%s",(huid,i))
            mydb.commit()
        self.close(mydb,mycursor)

    '''ob=backend()
    ob.health_insert(14,5,500000,"BPL")'''

    def pan_insert(self,top,uid):
        mydb,mycursor=self.connectt()
        mycursor.execute("insert into pan_card values(default,%s,%s)",(top,uid))
        mydb.commit()
        self.close(mydb,mycursor)

    '''ob=backend()
    ob.pan_insert("B",14)'''

    def income_insert(self,uid,y,inc,ta,tds):
        mydb,mycursor=self.connectt()
        mycursor.execute("insert into income_tax values((select pan_num from pan_card where uid=%s),%s,%s,%s,%s)",(uid,y,inc,tds,ta))
        mydb.commit()
        self.close(mydb,mycursor)


    '''ob=backend()
    ob.income_insert(13,"2016",1200000,36500,12000)'''

    '''def fpan_insert(self,c,cid,name):
        self.pan_insert("F","null")
        mydb,mycursor=self.connectt()
        mycursor.execute()'''

    def update_person_add(self,adds,addc,addst,addp,uid):
        mydb,mycursor=self.connectt()
        mycursor.execute("update person set address_street=%s , address_city=%s , address_state=%s , address_pin=%s where uid=%s",(adds,addc,addst,addp,uid))
        mydb.commit()
        self.close(mydb,mycursor)

    '''ob=backend()
    ob.update_person_add("N R Mohalla","mysore","karnataka","570007",13)'''

    def update_person_ph(self,ph,uid):
         mydb,mycursor=self.connectt()
         mycursor.execute("update person set phone=%s where uid=%s",(ph,uid))
         mydb.commit()
         self.close(mydb,mycursor)

    '''ob=backend()
    ob.update_person_ph("7045678323",13)'''

    '''
    1.delete person,
    2.delete head of a ration card or
    3.health card or
    4.lpg card and make user defined head'''

    def delete(self,uid):
        mydb,mycursor=self.connectt()

        mycursor.execute("select licence_num from licence where uid=%s",(uid,))
        ln=mycursor.fetchall()
        mycursor.execute("select * from licence where licence_num=%s",(ln[0][0],))
        vehcount=mycursor.fetchall()
        if(int(vehcount[0][0])>0):
            vo=int(input("Enter the owner for other vehicles:\n"))
        mycursor.execute("update vehicle set licence_num=%s where licence_num=%s",(vo,ln[0][0]))
        mydb.commit()
                
        mycursor.execute("delete from licence where uid=%s",(uid,))
        mydb.commit()

        
        mycursor.execute("delete from pan_card where uid=%s",(uid,))
        mydb.commit()

        
        mycursor.execute("delete from transport where uid=%s",(uid,))
        mydb.commit()


        
        mycursor.execute("select ration_id from ration where huid=%s",(uid,))
        ration_id=mycursor.fetchall()
        mycursor.execute("select type from ration where huid=%s",(uid,))
        typee=mycursor.fetchall()
        mycursor.execute("select no_of_people from ration where huid=%s",(uid,))
        nop=mycursor.fetchall()
        mycursor.execute("delete from ration where huid=%s",(uid,))
        mydb.commit()
        d=mycursor.rowcount
        if d==0:
            mycursor.execute("delete from person where uid=%s",(uid,))
            mydb.commit()
        else:
            n=int(input("Enter other huid:\n"))
            if(n!="no"):
                mycursor.execute("insert into ration values(%s,%s,%s,%s)",(ration_id[0][0],n,typee[0][0],nop[0][0]-1))
                mydb.commit()


        mycursor.execute("select health_id from health where huid=%s",(uid,))
        health_id=mycursor.fetchall()
        mycursor.execute("select amount from health where huid=%s",(uid,))
        amount=mycursor.fetchall()
        mycursor.execute("select no_of_people from health where huid=%s",(uid,))
        nop=mycursor.fetchall()
        mycursor.execute("select type_of_card from health where huid=%s",(uid,))
        toc=mycursor.fetchall()
        mycursor.execute("delete from health where huid=%s",(uid,))
        mydb.commit()
        d=mycursor.rowcount
        if d==0:
            mycursor.execute("delete from person where uid=%s",(uid,))
            mydb.commit()
        else:
            n=int(input("Enter other huid:\n"))
            if(n!="no"):
                mycursor.execute("insert into health values(%s,%s,%s,%s,%s)",(health_id[0][0],n,nop[0][0]-1,amount[0][0],toc[0][0]))
                mydb.commit()



        mycursor.execute("select lpg_id from lpg where huid=%s",(uid,))
        lpg_id=mycursor.fetchall()
        mycursor.execute("select date_of_issue from lpg where huid=%s",(uid,))
        doi=mycursor.fetchall()
        mycursor.execute("select deposit from lpg where huid=%s",(uid,))
        dep=mycursor.fetchall()
        mycursor.execute("select distributer_code from lpg where huid=%s",(uid,))
        dc=mycursor.fetchall()
        mycursor.execute("select distributer_name from lpg where huid=%s",(uid,))
        dn=mycursor.fetchall()
        mycursor.execute("select distributer_address from lpg where huid=%s",(uid,))
        da=mycursor.fetchall()
        mycursor.execute("delete from lpg where huid=%s",(uid,))
        mydb.commit()
        d=mycursor.rowcount
        if d==0:
            mycursor.execute("delete from person where uid=%s",(uid,))
            mydb.commit()
        else:
            n=int(input("Enter other huid:\n"))
            if(n!="no"):
                mycursor.execute("insert into lpg values(%s,%s,%s,%s,%s,%s,%s)",(lpg_id[0][0],doi[0][0],dep[0][0],dc[0][0],dn[0][0],da[0][0],n))
                mydb.commit()
        self.close(mydb,mycursor)
        
    #ob=backend()
    #ob.person_insert("1998-10-28","pooja","nagbhushan","vijayanagar","mysore","karnataka","57890","123","AB+")
