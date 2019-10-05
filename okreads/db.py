import psycopg2


class Db:
    def execute(sql, *args, **kwargs):
        conn = psycopg2.connect("dbname=okreads user=test password=test host=db")
        cur = conn.cursor()
        cur.execute(sql, *args, **kwargs)
        cur.close()
        conn.close()

    def fetchAll(sql):
        conn = psycopg2.connect("dbname=okreads user=test password=test host=db")
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result
