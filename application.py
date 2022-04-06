import os

from flask import Flask, session, render_template, request
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
        return render_template("layout.html")
    return render_template("iniciosecion.html")