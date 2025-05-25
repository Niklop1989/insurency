
import sqlite3
from dataclasses import dataclass

from typing import Optional,Dict,List

ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON"

DATA_CARS = [
    {'id':0,'brand_car':'BMV','owner':1},
    {'id':1,'brand_car':'AUDI','owner':2}
]
DATA_OWNERS = [
    {'owner_id':1,'first_name':'Ivan','last_name':'Haris','middle_name':'Ivanov'},
    {'owner_id':2,'first_name':'Aaaa','last_name':'Bbb','middle_name':'Ccc'}
]
DATABASE_NAME = 'table_car.db'
CAR_TABLE_NAME = 'cars'
OWNER_TABLE_NAME = 'owner'

@dataclass
class Car:
    brand_car:str
    owner:int
    id:Optional[int] = None
    def __getitem__(self, item):
        return getattr(self,item)

@dataclass
class Owner:
    first_name:str
    last_name:str
    middle_name:Optional[str] = None
    owner_id:Optional[int] = None
    def __getitem__(self, item):
        return getattr(self,item)

def init_db(initial_records_cars:List[Dict],initial_records_owners:List[Dict]):
    with sqlite3.connect(DATABASE_NAME)as conn:
        cursor = conn.cursor()

        cursor.execute(f"""SELECT name FROM sqlite_master 
                            WHERE type = 'table' AND name = '{CAR_TABLE_NAME}'
                                """
                       )
        exists = cursor.fetchone()

        if not exists:
            cursor.executescript(f"""
                CREATE TABLE IF NOT EXISTS '{OWNER_TABLE_NAME}' (
                owner_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name VARCHAR(50) NOT NULL, 
                last_name VARCHAR(50) NOT NULL, 
                middle_name VARCHAR(50)
                );
            """)
            cursor.executemany(f"""
                
                INSERT INTO '{OWNER_TABLE_NAME}' 
                (first_name, last_name, middle_name) VALUES (?, ?, ?)
                """,[(item['first_name'],item['last_name'],item['middle_name'])
                     for item in initial_records_owners])
        if not exists:
            cursor.executescript(f"""
                CREATE TABLE IF NOT EXISTS '{CAR_TABLE_NAME}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                brand_car VARCHAR(50) NOT NULL, 
                owner INTEGER NOT NULL REFERENCES owner(owner_id) ON DELETE CASCADE
                );
            """)
            cursor.executemany(f"""

                INSERT INTO '{CAR_TABLE_NAME}' 
                (brand_car, owner) VALUES (?, ?)
                """,[(item['brand_car'],item['owner'])
                     for item in initial_records_cars])


def _get_car_object_from_row(row:tuple) -> Car:
    return Car(id=row[0],brand_car=row[1],owner=row[2])

def _get_owner(row:tuple) ->Owner:
    return Owner(owner_id=row[0],first_name=row[1],last_name=row[2],middle_name=row[3])

def get_all_cars():
    with sqlite3.connect(DATABASE_NAME)as conn:
        cursor = conn.cursor()
        all_cars = cursor.execute(f"""
            SELECT * FROM {CAR_TABLE_NAME}
            """).fetchall()
        return [_get_car_object_from_row(row)for row in all_cars]

def get_all_owner() -> List[Owner]:
    with sqlite3.connect(DATABASE_NAME)as conn:
        cursor = conn.cursor()
        all_owner = cursor.execute(f"""
            SELECT * FROM {OWNER_TABLE_NAME}    
            """).fetchall()
        return [_get_owner(row)for row in all_owner]

def add_owner(owner:Owner) -> Owner:
    with sqlite3.connect(DATABASE_NAME)as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            INSERT INTO '{OWNER_TABLE_NAME}' 
            (first_name, last_name, middle_name) VALUES (?, ?, ?)
        """,(owner.first_name, owner.last_name, owner.middle_name))
        owner.owner_id = cursor.lastrowid
        return owner

def delete_owner_by_id(owner_id:int):
    with sqlite3.connect(DATABASE_NAME)as conn:
        cursor = conn.cursor()
        cursor.execute(ENABLE_FOREIGN_KEY)
        cursor.execute(f"""
        DELETE FROM {OWNER_TABLE_NAME} 
        WHERE owner_id = ?
        """,(owner_id,))

def get_car_by_owner(owner_id):
    with sqlite3.connect(DATABASE_NAME)as conn:
        cursor = conn.cursor()
        cursor.execute(f"""SELECT * FROM {CAR_TABLE_NAME} 
        WHERE owner = ? 
            """,(owner_id,))
        car  = cursor.fetchall()
        return [_get_car_object_from_row(row)for row in car]

def add_car(car:Car) -> Car:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            INSERT INTO '{CAR_TABLE_NAME}' 
            (brand_car, owner) VALUES(?, ?)
            """,(car.brand_car,car.owner))

def get_car_by_id(car_id):
    with sqlite3.connect(DATABASE_NAME)as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT * FROM '{CAR_TABLE_NAME}' WHERE 
            id = ?
        """,(car_id,))
        car = cursor.fetchone()
        if car:
            return _get_car_object_from_row(car)


def update_car_by_id(car:Car):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
               UPDATE {CAR_TABLE_NAME} 
                SET brand_car = ?, owner = ? 
                WHERE id = ?
           """,(car.brand_car,car.owner,car.id))
        conn.commit()

def delete_car_by_id(car_id):
    with sqlite3.connect(DATABASE_NAME)as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            DELETE * FROM '{CAR_TABLE_NAME}' 
            WHERE id = ?
        """,(car_id,))
        conn.commit()


























