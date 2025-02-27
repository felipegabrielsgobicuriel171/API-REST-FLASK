""" 
API REST FLASK
Autor: Felipe Gabriel Sgobi Curiel
"""


from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, text

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

db_connect = create_engine('mysql+mysqlconnector://root@localhost/study')

@app.route('/get', methods=["GET"])
def get():
    try:
        conn = db_connect.connect()
        result = conn.execute(text('SELECT * FROM states ORDER BY id DESC LIMIT 10'))
        users = [dict(zip(result.keys(), row)) for row in result]
        conn.close()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/post', methods=["POST"])
def post():
    try:
        print("dados enviados")
        conn = db_connect.connect()
        name_estado = request.json['name_estado']
        acronym_estado = request.json['acronym_estado']
        conn.execute(text("INSERT INTO states (name_estado, acronym_estado) VALUES (:name_estado, :acronym_estado)"), 
                     {"name_estado": name_estado, "acronym_estado": acronym_estado})
        result = conn.execute(text('SELECT * FROM states ORDER BY id DESC LIMIT 1'))
        conn.commit()
        user = [dict(zip(result.keys(), row)) for row in result]
        conn.close()
        return jsonify(user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/put/<int:id>', methods=["PUT"])
def put(id):
    try:
        conn = db_connect.connect()
        name_estado = request.json['name_estado']
        acronym_estado = request.json['acronym_estado']
        conn.execute(text("""
            UPDATE states
            SET name_estado = :name_estado, acronym_estado = :acronym_estado
            WHERE id = :id
        """), {"name_estado": name_estado, "acronym_estado": acronym_estado, "id": id})
        conn.commit()
        
        result = conn.execute(text('SELECT * FROM states ORDER BY id DESC LIMIT 1'))
        user_put = [dict(zip(result.keys(), row)) for row in result]
        conn.close()
        
        return jsonify(user_put), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/delete/<int:id>', methods=["DELETE"])
def delete(id):
    try:
        conn = db_connect.connect()
        result = conn.execute(text('SELECT * FROM states WHERE id = :id'), {"id": id})
        state_to_delete = [dict(zip(result.keys(), row)) for row in result]
        
        if state_to_delete:
            conn.execute(text('DELETE FROM states WHERE id = :id'), {"id": id})
            conn.commit()
            conn.close()
            return jsonify({"message": "Estado deletado com sucesso"}), 200
        else:
            conn.close()
            return jsonify({"error": "Estado não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)
