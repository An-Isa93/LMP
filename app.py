from flask import Flask, render_template, request, redirect,url_for
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
        cursor.execute("SELECT nombre, apellido, telefono FROM registro")
        contactos = cursor.fetchall()  #Recupera todas las filas de la consulta ejecutada y las devuelve como una lista de tuplas.
        conn.commit()
    conn.close()
    return contactos



if __name__ == "__main__":
    app.run(debug=True)
