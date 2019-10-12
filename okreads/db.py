from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Db:
    def execute(sql, values=None):
        db = Db._get_connection()
        if values:
            sql = text(sql)
            db.execute(sql, values)
        else:
            db.execute(sql)
        # @TODO figure out how to close the connection

    def fetchAll(sql):
        db = Db._get_connection()
        result = db.connect().execute(sql)
        return result

    @staticmethod
    def _get_connection():
        DB_NAME = 'okreads'
        DB_USER = 'test'
        DB_PASS = 'test'
        DB_HOST = 'db'
        DB_PORT = '5432'

        return create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
