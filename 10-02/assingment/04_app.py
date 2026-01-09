from mysql.connector import connect

class DB:
    mysqldb = connect(
        host = '127.1.1.0', 
        user = 'root', 
        password ='P@ssw0rd', 
        buffered = True, 
        database = 'RealState'
    )

    def create_connection (self):
        """ Create Conncetion to RDBMS and return a cursor"""
        cursor = self.mysqldb.cursor()
        return cursor
    
    
    def excute_featch_all(self, qre: str, params: tuple = tuple()) -> list:
        """Execute a query and fetch all rows. Optional params for parameterized queries."""
        cursor = self.create_connection()
        if params:
            cursor.execute(qre, params)
        else:
            cursor.execute(qre)
        return cursor.fetchall()

class App: 
    def fast_query(self, qre: str): 
        db = DB()
        respose = db.excute_featch_all(qre)
        for row in respose: 
            print(row)

    def show_office_summary(self): 
        qre = "SELECT * FROM office_summary;"
        print("-"*20, "Office Summary",  "-" * 20)
        self.fast_query(qre)
        print("-" * 55)

    def show_offices(self):
        print("-"*20, "Current Officies",  "-" * 20)
        q = "SELECT office_id, location FROM SalesOffice;"
        self.fast_query(q)
        print("-" * 55)


    def properities_ownership(self):
        print("-"*20, "Properties Ownership",  "-" * 20)
        qre = "SELECT * FROM PropertyOwner;"
        self.fast_query(qre)
        print("-" * 55)


if __name__ == '__main__': 
    app = App()
    app.show_office_summary()
    app.show_offices()
    app.properities_ownership()



