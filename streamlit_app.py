from sqlalchemy import create_engine
import streamlit as st
import pandas as pd

driver = 'SQL Server Native Client 11.0'

conn = create_engine("mssql+pyodbc://dbadmin:Barcelona2020@bdigital.database.windows.net/DemoBudget?driver=ODBC+Driver+17+for+SQL+Server")
#conn = create_engine('mssql+pyodbc://(localdb)\ProjectsV12/MainTest1?driver=SQL+Server+Native+Client+11.0', echo=True)
SQL_Query = pd.read_sql('SELECT [Customer Group],[Importe] FROM [dbo].[FGastosCliente]', conn)


st.write("My First App")
df = pd.DataFrame(SQL_Query, columns=['Customer Group','Importe'])
st.line_chart(df)
