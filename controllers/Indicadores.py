from flask import jsonify, request
from db.db import conn

class Indicador():
    global cur
    cur = conn.cursor()

    def listar():
        lista = []
        cur.execute("SELECT * FROM indicadores")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns, row)
            jsonData = dict(registro)
            lista.append(jsonData)
        return jsonify(lista)
        conn.close
    
    def crear(body):
        data = (body['codigo'], body['nombre'], body['descripcion'], body['tipoIndicador'], body['prioridad'], body['imagen'])
        sql = "INSERT INTO indicadores(codigo, nombre, descripcion, tipoIndicador, prioridad, imagen) VALUES(%s, %s, %s, %s, %s, %s)"
        cur.execute(sql, data)
        conn.commit()
        return {'estado': 'Insertado'}, 200