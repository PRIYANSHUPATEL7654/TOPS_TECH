# %pip install -U mcp 
# %pip install -U langchain-google-genai 
# %pip install -U langchain-mcp-adapters 
# %pip install -U python-dotenv 
# %pip install -U mysql-connector-python

from mcp.server.fastmcp import FastMCP
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
mcp = FastMCP("Student Database")

@mcp.tool() # instead of writing tools we write mcp.tool because we want to access tool through mcp server
def get_student_data():
    """Get all student data from MySQL database."""

    db = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        port=int(os.getenv("MYSQL_PORT"))
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM STUDENT_DETAILS")
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    
    return rows

if __name__ == "__main__":
    mcp.run()