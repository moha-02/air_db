from tkinter import Image
import psycopg2
import io
from PIL import Image

conn = psycopg2.connect(
    host="localhost",
    database="air_db",
    user="postgres",
    password="simo123",
    port="5432")

cur = conn.cursor()
cur.execute("SELECT plain_image FROM planes WHERE matricula='EH-RGY'")
img_data=cur.fetchone()[0]
img=Image.open(io.BytesIO(img_data))
img.show()
cur.close()
conn.close()
