import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv(postgres://eizfomgehbacpg:0d504f6b79986fd0e9208e453bbde7c2f94a6e1e5c913c7f3e840a2667e4f82f@ec2-107-20-177-161.compute-1.amazonaws.com:5432/df39fc6m3qcg8m):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

#Register 

#Login
@app.route("/login", method=["POST"])
def login():
    email = request.get.form("Email")
    
    # Make sure the user with the email does not exist
    if db.execute("SELECT id FROM users WHERE email = :email", {"email": email}.fetchone() is not None:
        return render_template("error.html", message = "The email is already registered")
    
    password = request.from.get("Password")
    db.execute("INSERT INTO users(email, password) VALUES(:email, :password)", {"email" :email, "password" :generate_password_hash(password)})
    db.commit
    return render_template("login.html", message ="Successfully loged in")
      
                  
#Logout
@app.route("/logout")
          

#Search
  @app.route("/flights")
  def flights():
      flights = db.execute("SELECT * FROM flights").fetchall()
      return render_template("flights.html", flights=flights)

           
           
@app.route("/")
  def index():
      flights = db.execute("SELECT * FROM flights").fetchall()
      return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
      # Get form information.
      name = request.form.get("name")
      try:
          flight_id = int(request.form.get("flight_id"))
      except ValueError:
          return render_template("error.html", message="Invalid flight number.")

      # Make sure the flight exists.
      if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
          return render_template("error.html", message="No such flight with that id.")
      db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
              {"name": name, "flight_id": flight_id})
      db.commit()
      return render_template("success.html")
           
  @app.route("/flights/<int:flight_id>")
  def flight(flight_id):
      # Make sure flight exists.
      flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).fetchone()
      if flight is None:
          return render_template("error.html", message="No such flight.")

      # Get all passengers.
      passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                              {"flight_id": flight_id}).fetchall()
      return render_template("flight.html", flight=flight, passengers=passengers)

           
           
           
#Book pag

#Review subimission

#Goodreads review

#API access
@app.route("/api/<ISBN>", method=["GET"])
def api(ISBN):
    book = db.execute("SELECT * FROM books WHERE isbn = :ISBN", {"ISBN":ISBN}).fetchone()
    if book is None;
        return render_template("error.html", error_message="Invalid ISBN")
    
    reviews = db.execute("SELECT * FROM reviews WHERE book_id = :book_id", {"book_id": book_id}).fetchall()
    count = 0
    ratiing = 0
    for review in reviews:
        count += 1
        rating += review.rating
    if count:
        average_rating = rating / count
    else:
        average_rating = 0
        
    return jsonify(
        title = book.title,
        author = book.aouthor,
        year = book.year,
        isbn = book.isbn,
        review_count = count,
        average_score = average_rating
    )

if__name__=="__main__":
    app.run(debug=TRUE)
    

import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Sii3jAsM7OI56b4UFhCCw", "isbns": "9781632168146"})
print(res.json())
