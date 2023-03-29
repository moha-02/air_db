# air_db

## MAIN OBJECTIVES 🎯

- Integrity constraints
- Referential integrity
- Cascading actions in referential integrity
- Date, time or timestamp data types
- Binary large objects
- Domains
- Indexes
- Users
- Privileges
- Roles

## PREREQUIREMENTS
Python 🐍

Postgresql 🐘

~~~

pip install PILLOW
pip install psycopg2 

~~~

## DATABASE ER DIAGRAM

![base_aerea pgerd (1)](https://user-images.githubusercontent.com/119495982/228653521-aedf1614-9fce-4cf2-a7b4-e025c6b23bb1.png)

## FUNCTIONALITY OF THE DOMAINS

![Captura de pantalla 2023-03-29 220430](https://user-images.githubusercontent.com/119495982/228654651-7b76749f-7f02-4bb7-a2ae-c02bc4e20190.jpg)

THIS IS ONE EXAMPLE, WHERE THE EMAIL IS NOT ACCEPTED BECAUSE IT DOES NOT COMPLY WITH THE DOMAIN SCHEME

## USING BINARY DATA 🛫

### BLOB INSERT

In ouer case we used the following string to insert the images as bytea data in the designed column, we stored images of each plane.

~~~
pg_read_binary_file('C:\Program Files\PostgreSQL\13\pgAdmin 4\plain_images\nostrum.png')::bytea)
~~~
This seemed easier and faster than using python.

### RETRIEVING THE IMAGES

To display the images we used python to convert the binary dta to a file and store it in a variable , we connected to the databasa by using psycopg2 tehn, we transformed the data and stored it by using PILLOW
~~~
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
~~~
By using the PIL librarie, the code seems easier to understand and use.

## INDEXES AND CASCADIAN ACTIONS

These where added in the main script since they help manage the data, the cascadiana ction was used mostly in the foreign and primary key conection.
~~~
CREATE INDEX passengers_last_name_idx ON passengers (last_name);
CREATE INDEX flight_departure_time_idx ON flight (departure_time);
CREATE INDEX planes_capacidad_idx ON planes (capacidad);
CREATE INDEX tripulation_surname_idx ON tripulation (surname);
CREATE INDEX personal_email_idx ON personal (email);

ON UPDATE NO ACTION
    ON DELETE CASCADE
~~~

## USERS ROLES AND PRIVILEGES 👨‍✈️👨‍✈️

The roles and privileges are oriented to the staff maintenance crew. As you can see the administrative_technician is the one with the most privileges. Meanwhile the rest can manage and edite the data depending on their position.

~~~
CREATE USER persona1 WITH PASSWORD 'password1';
CREATE USER persona2 WITH PASSWORD 'password2';
CREATE USER persona3 WITH PASSWORD 'password3';
CREATE USER persona4 WITH PASSWORD 'password4';
CREATE USER persona5 WITH PASSWORD 'password5';

CREATE ROLE  pax; 
GRANT SELECT ON flight TO pax;
GRANT pax TO persona1;

CREATE ROLE  passenger_agent; 
GRANT  SELECT,insert,update ON passengerS TO passenger_agent; 
GRANT passenger_agent TO persona2;

CREATE ROLE  operation_technician;
GRANT  SELECT,insert,update ON flight TO operation_technician;
GRANT operation_technician TO persona3;

CREATE ROLE administrative_technician;
GRANT  ALL PRIVILEGES ON flight,passengers,personal TO administrative_technician; 
GRANT administrative_technician TO persona4;

CREATE ROLE  dispatcher;
GRANT SELECT,update ON flight TO dispatcher;
GRANT dispatcher TO persona5;
~~~

## CONCLUSION 

To sum up its a small example of an airline database, which we used to practice the different sections of the unit and understand how they work. We also used previows knowledge since we had to use many-to-many and one-to-many relationships. Also we used postgres to get used to it, also it was very helpfull due to its large documentation and compatibility.

### By

Mohammed Salhi Biade

Fbian Ossai Ossai

07_09_ASSI_Intermediate_SQL_2

