from flask import Flask, render_template, request, redirect,url_for, jsonify
from bd import conexion

app = Flask(__name__)

@app.route("/agenda", methods=["GET", "POST"])
def agenda():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        telefono = request.form["telefono"]
        agregar(nombre, apellido, telefono)
        return redirect(url_for("agenda")) 
      
    contactos = listar() 
    return render_template("index.html", contactos=contactos)

def agregar(nombre, apellido, telefono):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO registro (nombre, apellido, telefono) VALUES (%s, %s, %s)", (nombre, apellido, telefono))
        conn.commit()
    conn.close()

def listar():
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("SELECT*FROM registro")
        contactos = cursor.fetchall()  #Recupera todas las filas de la consulta ejecutada y las devuelve como una lista de tuplas.
        conn.commit()
    conn.close()
    return contactos

@app.route("/eliminar",methods=["POST"])
def eliminar():
    id_contacto = request.form['id']
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM registro WHERE id=%s",(id_contacto,))
        conn.commit()
    conn.close()  
    return redirect(url_for("agenda")) 

@app.route("/actualizar", methods=["POST"])
def actualizar():
    data = request.json
    id_contacto = data.get("id")
    nombre = data.get("nombre")
    apellido = data.get("apellido")
    telefono = data.get("telefono")
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE registro SET nombre=%s, apellido=%s, telefono=%s WHERE id=%s",
            (nombre, apellido, telefono, id_contacto)
        )
        conn.commit()
        
    conn.close()
    return jsonify({"status": "success"})
   
     

if __name__ == "__main__":
    app.run(debug=True)
