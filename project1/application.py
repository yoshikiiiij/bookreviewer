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
    return render_template("login.html", message ="Successfully logged in")
      
                  
# Logout
@app.route("/logout")
def logout():
 
# Search
@app.route("/booklist", method=["POST"])
def booklist():
    if "user_email" not in session:
        return render_template("login.html", message="Login first")
        
    book_column = request.form.get("Book_column")
    query = request.form.get("Query")              
        
    if book_column == "year":
        book_list = db.execute("SELECT * FROM books WHERE year =:query", {"query" :query}.fetchall()              
    else:
        book_list = db.execute("SELECT * FROM books WHERE                        
                               
                               
# Book page
@app.route("/detail/<int:book_id>", methods=["GET","POST"])
def detail(book_id):
    if "user_email" not in session:
        return render_template("login.html", message="Login first")
    
    book = db.execute("SELECT * FROM books WHERE id = :book_id", {"book_id" :book_id}).fetchone()
    if book is None:
        return render_template("error.html", message = "No book with that id")
                  
    #Review subimission
    if request.method == "POST":
        user_id = session["user_id"]
        rating = request.form.get("Rating")
        comment = request.form.get("Comment")
    if db.execute("SELECT id FROM reviews WHERE user_id =:user_id AND book_id =;book_id",{"user_id" :user_id, "book_id" :book_id}==None:
        db.execute("INSERT INTO reviews(user_id, book_id, rating, comment) VALUES(:user_id, :book_id, :rating, :comment)"{"user_id" :user_id, "book_id" :book_id, "rating" :rating, "comment" :comment})
    else:
        db.execute("UPDATAE reviews SET comment =:comment, rating =:rating WHERE user_id =:user_id AND book_id =;book_id",{"comment" :comment, "rating" :rating, "user_id" :user_id, "book_id" :book_id}=           
    db.commit
                   
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
    
# Process json data
import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Sii3jAsM7OI56b4UFhCCw", "isbns": "9781632168146"})

rating_count = res["rating_count"]
average_rating = res["average_rating"]
reviews = db.execute("SELECT * FROM reviews WHERE book_id =:book_id", {"book_id" :book_id})fetchall()
users = []
for review in reviews:
    email = db.execute("SELECT email FROM users WHERE id =:user_id", {"user_id" :review.user_id}).fetchone()                   
    users.append(email, review)

return render_template("detail.html", book=book, users=users, rating=rating, ratings_count=ratings_count, average_rating=average_rating, user_email=session["user_email"])                  
