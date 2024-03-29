"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

with psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="germanshtat84"
)as connection:

    with connection.cursor() as cursor:
        with open('north_data/employees_data.csv') as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                send_data = """INSERT INTO employees 
                                VALUES (%s, %s, %s, %s, %s, %s)"""

                cursor.execute(send_data, row)

        with open('north_data/customers_data.csv') as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                send_data = """INSERT INTO customers 
                                VALUES (%s, %s, %s)"""

                cursor.execute(send_data, row)

        with open('north_data/orders_data.csv') as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                send_data = """INSERT INTO orders 
                                VALUES (%s, %s, %s, %s, %s)"""

                cursor.execute(send_data, row)

connection.close()

