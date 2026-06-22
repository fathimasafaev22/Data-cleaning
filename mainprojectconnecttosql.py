import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="host",
    user="user",
    password="pass"
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS cleaned_appointments")

mydb = mysql.connector.connect(
    host="host",
    user="user",
    password="pass",
    database="cleaned_appointments"
)

cursor = mydb.cursor()

df = pd.read_csv("cleaned_appointments.csv")

df = df.rename(columns={
    "hipertension": "hypertension",
    "handcap": "handicap"
})

cols = [
    "patientid", "gender", "age", "neighbourhood",
    "hypertension", "diabetes", "alcoholism",
    "handicap", "sms_received", "no_show", "waiting_days"
]

df = df[cols]
cursor.execute("""
CREATE TABLE IF NOT EXISTS cleaned_appointments (
    patientid BIGINT,
    gender VARCHAR(10),
    age INT,
    neighbourhood VARCHAR(100),
    hypertension INT,
    diabetes INT,
    alcoholism INT,
    handicap INT,
    sms_received INT,
    no_show INT,
    waiting_days INT
)
""")

sql = """
INSERT INTO cleaned_appointments (
patientid, gender, age, neighbourhood,
hypertension, diabetes, alcoholism,
handicap, sms_received, no_show, waiting_days
) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

cursor.executemany(sql, df.values.tolist())

mydb.commit()


cursor.execute("SELECT * FROM cleaned_appointments LIMIT 5")

for row in cursor:
    print(row)

