import psycopg2
import psycopg2.extras

DB_URL = 'postgres://gah_db_user:ULeYl2ZDZ9yHDij2Dda1YItLLZ16EYbO@dpg-chgun2bhp8u065rbmv40-a/gah_db'

def sql(query, parameters=[]):
    connection = psycopg2.connect(DB_URL)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results
