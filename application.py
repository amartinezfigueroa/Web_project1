import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

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



@app.route("/iniciosecion", METHODS=["POST","GET"])
def iniciosecion():

    if request.methods == "POST": 
        name = request.form.get("nombre")
        password = request.form.get("contraseña")
    
    else: 
        return render_template("iniciosecion.html")
