
from flask import Flask, render_template, jsonify
import mysql.connector

sqlDatabase = mysql.connector.connect(host='localhost', database='PronoteRemake', user='root', password='31#nigi2')

cursor = sqlDatabase.cursor(dictionary=True)
cursor.execute("USE PronoteRemake")

app = Flask(__name__)
app.config["DEBUG"] = True

app.route('/api/v1/resources/students/get_student/<student_id>', methods=['GET'])
def api_get_student(student_id: int):
    cursor.execute("SELECT * FROM Student WHERE STUDENT_ID = %s", (student_id,))
    result = cursor.fetchall()
    return jsonify(result)