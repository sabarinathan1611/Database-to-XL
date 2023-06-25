import pandas as pd
import sqlite3
import os 
    
def createXL():
            APP_ROOT = os.path.dirname(os.path.abspath(__file__))
            
            saveFolder = os.path.join(APP_ROOT, 'static/XLfile/')
                
            
            
            sqlite_file = 'website/database.db'    # name of the sqlite database file
            conn = sqlite3.connect(sqlite_file)

            # Read SQLite query results into a pandas DataFrame
            event1 = pd.read_sql_query("SELECT * FROM event1",conn)
            event2 = pd.read_sql_query("SELECT * FROM event2",conn)
            event3 = pd.read_sql_query("SELECT * FROM event3",conn)
            event4 = pd.read_sql_query("SELECT * FROM event4",conn)
            event5 = pd.read_sql_query("SELECT * FROM event5",conn)
            event6 = pd.read_sql_query("SELECT * FROM event6",conn)
            event7 = pd.read_sql_query("SELECT * FROM event7",conn)
            event8 = pd.read_sql_query("SELECT * FROM event8",conn)
            event9 = pd.read_sql_query("SELECT * FROM event9",conn)
            
            # Save Query Result to Excel File
            event1.to_excel("{}event1.xlsx".format(saveFolder))
            event2.to_excel("{}event2.xlsx".format(saveFolder))
            event3.to_excel("{}event3.xlsx".format(saveFolder))
            event4.to_excel("{}event4.xlsx".format(saveFolder))
            event5.to_excel("{}event5.xlsx".format(saveFolder))
            event6.to_excel("{}event6.xlsx".format(saveFolder))
            event7.to_excel("{}event7.xlsx".format(saveFolder))
            event8.to_excel("{}event8.xlsx".format(saveFolder))
            event9.to_excel("{}event9.xlsx".format(saveFolder))