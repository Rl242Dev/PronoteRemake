import mysql.connector

def hash_password(inputPassword: str) -> int:
    return hash(inputPassword)

def check_password_hash(inputPassword: str, student_id: int, sqlConnection: mysql.connector.connect) -> bool:
    cursor = sqlConnection.cursor(dictionary=True)
    cursor.execute("USE PronoteRemake")

    statement = "SELECT PASSWORD FROM Student WHERE STUDENT ID = %s", (student_id,)
    cursor.execute(statement)
    result = cursor.fetchall()

    if result["PASSWORD"] == hash(inputPassword):
        return True
    else:
        return False
    
    return None

