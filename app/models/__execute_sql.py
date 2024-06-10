import os
import psycopg2
from psycopg2 import extras
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Database:
    @staticmethod
    def get_connection():
        """
        Establishes a connection to the database using environment variables.
        Returns a connection object.
        """
        return psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            options=f'-c search_path={os.getenv("POSTGRES_SCHEMA")}'
        )

    @staticmethod
    def fetchall(query, params=None):
        """
        Fetches all rows from a query.
        """
        conn = None
        try:
            conn = Database.get_connection()
            with conn.cursor(cursor_factory=extras.DictCursor) as cursor:
                cursor.execute(query, params or ())
                records = cursor.fetchall()
                return records
        finally:
            if conn:
                conn.close()

    @staticmethod
    def fetchone(query, params=None):
        """
        Fetches the first row from a query.
        """
        conn = None
        try:
            conn = Database.get_connection()
            with conn.cursor(cursor_factory=extras.DictCursor) as cursor:
                cursor.execute(query, params or ())
                record = cursor.fetchone()
                return record
        finally:
            if conn:
                conn.close()

    @staticmethod
    def execute(query, params=None):
        """
        Executes a query such as INSERT, UPDATE, DELETE.
        """
        conn = None
        try:
            conn = Database.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                conn.commit()  # Ensure you commit to save the changes
        except Exception as e:
            if conn:
                conn.rollback()  # Rollback in case of error
            raise e
        finally:
            if conn:
                conn.close()

    @staticmethod
    def execute_returning_id(query, params=None):
        """
        Executes a query and returns the id of the inserted or updated row.
        Typically used with RETURNING in SQL.
        """
        conn = None
        try:
            conn = Database.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                id_of_new_row = cursor.fetchone()[0]
                conn.commit()
                return id_of_new_row
        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if conn:
                conn.close()
