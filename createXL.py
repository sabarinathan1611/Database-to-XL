import pandas as pd
import sqlite3



    
def tech():
            sqlite_file = 'database.db'    # name of the sqlite database file
            conn = sqlite3.connect(sqlite_file)

            # Read SQLite query results into a pandas DataFrame
            df = pd.read_sql_query("SELECT * FROM tech_register",conn)

            # Save Query Result to Excel File
            df.to_excel("tech.xlsx")
def non_tech():
        
            sqlite_file = 'database.db'    # name of the sqlite database file
            conn = sqlite3.connect(sqlite_file)

            # Read SQLite query results into a pandas DataFrame
            df = pd.read_sql_query("SELECT * FROM non_register",conn)

            # Save Query Result to Excel File
            df.to_excel("nontech.xlsx")
tech()
non_tech()