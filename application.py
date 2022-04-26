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
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


#usuarios

@app.route("/")
@login_required
def index():
    return render_template("layout.html")

@app.route("/iniciosecion" ,methods=["POST" , "GET"])
def inisiosecion():
    if request.method == "POST":
        usuarios = request.form.get("nombre")
        print(usuarios)
        
        password = request.form.get("contraseña")
        print(password)
        return 'ok'
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
            flash("contraseña incorrecta")
            return render_template("registro.html") 

        db.execute('Insert into usuarios (usuario , contraseña) values(:rusuario, :rcontraseña)', {'rusuario': rusuario, 'rcontraseña': rcontraseña})
        db.commit()
        return "bien"
    else:
        return render_template("registro.html")
      
  