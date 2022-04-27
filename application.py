import os

from flask import Flask,flash, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
from helper import login_required


load_dotenv()

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgresql://guoakllcseoxhk:c668ba40006b4d6122f65751cf2b3df659f02b284534809fa11af022a58109a2@ec2-18-215-96-22.compute-1.amazonaws.com:5432/d96asn15oirh76")
db = scoped_session(sessionmaker(bind=engine))


#usuarios

@app.route("/")
@login_required
def index():
    return render_template("layout.html")

@app.route("/iniciosecion" ,methods=["POST" , "GET"])
def inisiosecion():
    if request.method == "POST":

        if not request.form.get("nombre"):
            flash("Llenar todos los campos")
            return render_template("iniciosecion.html")

        usuarios = request.form.get("nombre")
        print(usuarios)
        
        if not request.form.get("contraseña"):
            flash("Llenar todos los campos")
            return render_template("iniciosecion.html")

        password = request.form.get("contraseña")
        print(password)

        consult = db.execute("SELECT nombre, contraseña FROM usuarios WHERE nombre = usuarios").fetchone()

        session["user_id"] = consult[0]
        return render_template("layout.html")

    else:
        return render_template("iniciosecion.html")


@app.route("/registro", methods = ["POST", "GET"])
def registro():
    if request.method == "POST":
        rusuario = request.form.get("rusername")
        print(rusuario)

        rcontraseña = request.form.get("rpassword")
        print(rcontraseña)

        rconfirmacion = request.form.get("rconfirmation")
        print(rconfirmacion)

        if rcontraseña != rconfirmacion:
            flash("la contraseña no coincide")
            return render_template("registro.html") 

        db.execute('Insert into usuarios (usuario , contraseña) values(:rusuario, :rcontraseña)', {'rusuario': rusuario, 'rcontraseña': rcontraseña})
        db.commit()
        return render_template("layout.html")

        if consult == 0 :
            flash("El usuario no existe")
        else:
           return render_template("layout.html")
           
    else:
        return render_template("registro.html")
      

@app.route("/layout", methods = ["POST", "GET"])
def busqueda():
     if request.method == "POST":
        buscar = request.form.get("busqueda")
        print(busqueda)

        return "no se"