################################################################################
##########################         import packages         #####################
################################################################################
import ibm_db
from flask_login import current_user

class ibm_call:
    def __init__(self):
        dsn_hostname = "fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud" # e.g.: "54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
        dsn_uid = "ywq96131"        # e.g. "abc12345"
        dsn_pwd = "CqClOdpSOlcNGlDg"      # e.g. "7dBZ3wWt9XN6$o0J"

        dsn_driver = "{IBM DB2 ODBC DRIVER}"
        dsn_database = "BLUDB"            # e.g. "BLUDB"
        dsn_port = "32731"                # e.g. "32733" 
        dsn_protocol = "TCPIP"            # i.e. "TCPIP"
        dsn_security = "SSL"              #i.e. "SSL"
        dsn = (
            "DRIVER={0};"
            "DATABASE={1};"
            "HOSTNAME={2};"
            "PORT={3};"
            "PROTOCOL={4};"
            "UID={5};"
            "PWD={6};"
            "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)
        try:
            self.conn = ibm_db.connect(dsn, "", "")
            # print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
            print("connected")
        except:
            print ("Unable to connect: ", ibm_db.conn_errormsg() )


    def insert_row(self,email, name, password,typeofuser,table_name='USER'):
        try:
            insertQuery="""insert into %s (email, name, password,typeofuser) values ('%s', '%s', '%s','%s'); """ %(table_name, email, name, password,typeofuser)
            insertStmt = ibm_db.exec_immediate(self.conn, insertQuery)
        except:
            pass
        print('Row inserted')


    def get_data(self,email):
        try:
            selectQuery = "select * from USER where email= ('%s');" %(email)
            selectStmt = ibm_db.exec_immediate(self.conn, selectQuery)
            user=ibm_db.fetch_both(selectStmt)
            if user:
                del user[0]
                del user[1]
                del user[2]
                del user[3]
                del user[4]
        except:
            pass
        return (user)

    def insert_farmer_data(self,state,district,crop,price,crop_qty):
        try:
            insertQuery="""insert into FARMER (farm_id,state,district,crop,crop_min_price,crop_prod_qty,avai_prod_qty) values ('%d', '%s', '%s','%s','%d','%f','%f'); """ %(current_user.id, state, district, crop,int(price),float(crop_qty),float(crop_qty))
            # print(insertQuery)
            insertStmt = ibm_db.exec_immediate(self.conn, insertQuery)
        except:
            pass
    def update_farmer_data(self):
        
        # print('hello')
        selectQuery="""Select *  from FARMER where farm_id = '%d'; """ %(current_user.id)
        res= ibm_db.exec_immediate(self.conn,selectQuery)
        dic={}
        while True:
            try:
                row=ibm_db.fetch_assoc(res)
                dic[row['UNIQUE_ID']]=row
                if not row:
                    break
            except:
                break
        return dic

    def buyergetdata(self):
        selectQuery="""Select *  from FARMER; """
        res= ibm_db.exec_immediate(self.conn,selectQuery)
        dic={}
        while True:
            try:
                row=ibm_db.fetch_assoc(res)
                dic[row['UNIQUE_ID']]=row
                if not row:
                    break
            except:
                break
        return dic
    def buyergetdatabystate(self,state):
        selectQuery="""Select *  from FARMER where state='%s'; """%(state)
        res= ibm_db.exec_immediate(self.conn,selectQuery)
        dic={}
        while True:
            try:
                row=ibm_db.fetch_assoc(res)
                dic[row['UNIQUE_ID']]=row
                if not row:
                    break
            except:
                break
        return dic

    def buyerformupdate(self,ref_id,farm_id,crop,price,crop_qty,ph_no):
        try:

            insertQuery="""insert into BUYER (buyer_id,FARM_CROP_ID,farm_unique_id,crop,price,crop_quantity,ph_no,approved) values ('%d','%d','%d','%s','%d','%d','%d','%s'); """ %(current_user.id, int(ref_id),int(farm_id),crop,float(price),float(crop_qty),int(ph_no),'N')
            print(insertQuery)
            insertStmt = ibm_db.exec_immediate(self.conn, insertQuery)
        except:
            pass
        # print(insertQuery)
    
    def responsedatafrombuyer(self):
        selectQuery="""Select *  from BUYER where farm_unique_id = '%d' and approved='%s'; """ %(current_user.id,"N")
        res= ibm_db.exec_immediate(self.conn,selectQuery)
        dic={}
        while True:
            try:
                row=ibm_db.fetch_assoc(res)
                dic[row['UNIQUE_ID']]=row
                if not row:
                    break
            except:
                break
        return dic
    def updatebothtable(self,buyer_id,farm_id,crop_qty):
        try:

            updatequery="""update BUYER SET APPROVED='Y' WHERE BUYER_ID='%d'""" %(int(buyer_id))
            res= ibm_db.exec_immediate(self.conn,updatequery)
            print(updatequery)
            updatequery="""update FARMER SET AVAI_PROD_QTY=AVAI_PROD_QTY-'%d' WHERE UNIQUE_ID='%d'""" %(int(crop_qty),int(farm_id))
            res= ibm_db.exec_immediate(self.conn,updatequery)
            print(updatequery)
        except:
            pass
    def getsoldcrop(self):
        selectQuery="""Select *  from BUYER where farm_unique_id = '%d' and approved='%s'; """ %(current_user.id,"Y")
        res= ibm_db.exec_immediate(self.conn,selectQuery)
        dic={}
        while True:
            try:
                row=ibm_db.fetch_assoc(res)
                dic[row['UNIQUE_ID']]=row
                if not row:
                    break
            except:
                break
        return dic
    
    def approvedcrop(self):
        selectQuery="""Select *  from BUYER where buyer_id = '%d' and approved='%s'; """ %(current_user.id,"Y")
        res= ibm_db.exec_immediate(self.conn,selectQuery)
        dic={}
        while True:
            try:
                row=ibm_db.fetch_assoc(res)
                dic[row['UNIQUE_ID']]=row
                if not row:
                    break
            except:
                break
        return dic

    def for_approval(self):
        selectQuery="""Select *  from BUYER where buyer_id = '%d' and approved='%s'; """ %(current_user.id,"N")
        res= ibm_db.exec_immediate(self.conn,selectQuery)
        dic={}
        while True:
            try:
                row=ibm_db.fetch_assoc(res)
                dic[row['UNIQUE_ID']]=row
                if not row:
                    break
            except:
                break
        return dic
            


    def  __del__(self):
        ibm_db.close(self.conn)

ibm_ob=ibm_call()