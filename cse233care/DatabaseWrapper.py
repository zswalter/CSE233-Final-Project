import sqlite3


class DatabaseWrapper:

    def __init__(self, databasename):
        self.databasename = databasename
        self.dconn = sqlite3.connect(self.databasename, isolation_level=None)
        self.conn = self.dconn.cursor()
        try:
            self.conn.execute("""
            CREATE TABLE CLIENTS (
            SOCIALSECURITYNUMBER NUMERIC(9,0) NOT NULL UNIQUE,
            USERNAME VARCHAR(50) NOT NULL UNIQUE,
            NAME VARCHAR(50),
            PASSWORD VARCHAR(30),
            EMAIL VARCHAR(30),
            AGE NUMERIC(3,0),
            STATE VARCHAR(20),
            SMOKER BOOLEAN,
            GENDER VARCHAR(6),
            BODYMASSINDEX NUMERIC(5,0),
            PROFESSION VARCHAR(50),
            MARITALSTATUS BOOLEAN,
            PREVIOUSLYUNINSURED BOOLEAN,
            PRECONDITIONS NUMERIC(10,0),
            FAMILYHISTORY NUMBERIC(10,0),
            )""")

            self.conn.execute("""
            CREATE TABLE PLANS (
            OWNER NUMERIC(9,0) NOT NULL UNIQUE,
            COSTPERMONTH NUMERIC(5,0),
            EXPIRATIONDATE DATE,
            BALANCEOWED NUMERIC(6,0),
            )""")

            self.conn.execute("""
            CREATE TABLE CLAIMS (
            OWNER NUMERIC(9,0) NOT NULL UNIQUE,
            DATE DATE,
            CONDITION VARCHAR(1000),
            AMOUNT NUMERIC(10,0),
            )""")

        except sqlite3.OperationalError:
            #Database already exists
            print("Database already exists")

    def __del__(self):
        self.conn.close()
        self.dconn.close()

    def insertclient(self, username, password, socialsecuritynumber, name, email, age,
                     state, smoker, gender, bodymassindex, profession, maritalstatus,
                     previouslyuninsured, preconditions, familyhistory):
        try:
            self.conn.execute("""
            INSERT INTO CLIENTS (USERNAME, PASSWORD, SOCIALSECURITYNUMBER, NAME, EMAIL,
            AGE, STATE, SMOKER, GENDER, BODYMASSINDEX, PROFESSION, MARITALSTATUS,
            PREVIOUSLYUNINSURED, PRECONDITIONS, FAMILYHISTORY)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, [username, password, socialsecuritynumber, name, email, age, state, smoker,
                  gender, bodymassindex, profession, maritalstatus, previouslyuninsured,
                  preconditions, familyhistory])
        except sqlite3.IntegrityError:
            #Client already exisits in database
            print("Client already exists")

    def insertclaim(self, owner, date, condition, amount):
        try:
            self.conn.execute("""
            INSERT INTO CLAIMS (OWNER, DATE, CONDITION, AMOUNT)
            VALUES (?, ?, ?, ?)
            """, [owner, date, condition, amount])
        except sqlite3.IntegrityError:
            #claim already exists, owner can only have one claim at a time
            print("Client already has a claim")

    def insertplan(self, owner, costpermonth, expirationdate, balanceowed):
        try:
            self.conn.execute("""
            INSERT INTO PLANS (OWNER, COSTPERMONTH, EXPIRATIONDATE, BALANCEOWED)
            VALUES (?, ?, ?, ?)
            """, [owner, costpermonth, expirationdate, balanceowed])
        except sqlite3.IntegrityError:
            #plan already exists, owner can only have one plan at a time
            print("Client already has a plan")

    def listclients(self):
        #Returns list of clients
        self.conn.execute("""SELECT * FROM CLIENTS""")
        while True:
            v = self.conn.fetchone()
            if v is None:
                break
            return v

    def listplans(self):
        #Returns list of plans
        self.conn.execute("""SELECT * FROM PLANS""")
        while True:
            v = self.conn.fetchone()
            if v is None:
                break
            return v

    def listclaims(self):
        #Returns list of claims
        self.conn.execute("""SELECT * FROM CLAIMS""")
        while True:
            v = self.conn.fetchone()
            if v is None:
                break
            return v

    def updateclient(self, username, password, socialsecuritynumber, name, email, age,
                     state, smoker, gender, bodymassindex, profession, maritalstatus,
                     previouslyuninsured, preconditions, familyhistory):
        self.conn.execute("""UPDATE CLIENTS SET USERNAME = ?, PASSWORD = ?,
        NAME = ?, EMAIL = ?, AGE = ?, STATE = ?, SMOKER = ?, GENDER = ?, BODYMASSINDEX = ?,
        PROFESSION = ?, MARITALSTATUS = ?, PREVIOUSLYUNINSURED = ?, PRECONDITIONS = ?,
        FAMILYHISTORY = ? WHERE SOCIALSECURITYNUMBER = ?
        """, [username, password, name, email, age, state, smoker, gender, bodymassindex,
              profession, maritalstatus, previouslyuninsured, preconditions, familyhistory,
              socialsecuritynumber])

    def updateclaim(self, owner, date, condition, amount):
        self.conn.execute("""UPDATE CLAIMS SET DATE = ?, CONDITION = ?, AMOUNT =?
        WHERE OWNER = ?""", [date, condition, amount, owner])

    def updateplan(self, owner, costpermonth, expirationdate, balanceowed):
        self.conn.execute("""UDPATE PLANS SET COSPERMONTH = ?, EXPIRATIONDATE = ?, BALANCEOWED = ?
        WHERE OWNER = ?""", [costpermonth, expirationdate, balanceowed, owner])

    def deleteclient(self, socialsecuritynumber):
        self.conn.execute("""DELETE FROM CLIENTS WHERE SOCIALSECURITYNUMBER = ? """, [socialsecuritynumber])

    def deleteclaim(self, owner):
        self.conn.execute("""DELETE FROM CLAIMS WHERE OWNER = ?""", [owner])

    def deleteplan(self, owner):
        self.conn.execute("""DELETE FROM PLANS WHERE OWNER = ?""", [owner])