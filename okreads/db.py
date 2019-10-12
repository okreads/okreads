import psycopg2


class Db:
    def execute(sql, values=None):
        conn = psycopg2.connect("dbname=okreads user=test password=test host=db")
        conn.autocommit = True
        cur = conn.cursor()

        if values:
            cur.execute(sql, values)
        else:
            cur.execute(sql)
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
