# from flask import Flask, render_template, request, redirect, url_for, flash, session
# import psycopg2  # PostgreSQL driver
# from psycopg2.extras import RealDictCursor  # To fetch query results as dictionaries


# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'  # Required for session management

# # ✅ PostgreSQL Database Configuration
# DB_HOST = "localhost"  # Change if using a remote server
# DB_NAME = "mydatabase"
# DB_USER = "postgres"
# DB_PASSWORD = "postgres"

# # ✅ Function to connect to PostgreSQL
# def get_db_connection():
#     try:
#         conn = psycopg2.connect(
#             host=DB_HOST,
#             database=DB_NAME,
#             user=DB_USER,
#             password=DB_PASSWORD
#         )
#         return conn
#     except Exception as e:
#         print("Database connection error:", e)
#         return None

# @app.route("/", methods=["GET", "POST"])
# def hello_world():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
# # 
#         conn = get_db_connection()
#         if conn is None:
#             flash("Database connection failed!", "danger")
#             return render_template("index.html")

#         cursor = conn.cursor(cursor_factory=RealDictCursor)

#         # ✅ Query to check if user exists
#         cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
#         user = cursor.fetchone()

#         cursor.close()
#         conn.close()

#         if user:
#             flash("Login successful!", "success")
#             session["user"] = user["username"]  # Store username in session
#             return redirect(url_for("dashboard"))
#         else:
#             flash("Invalid username or password", "danger")

#     return render_template("index.html")

# @app.route("/dashboard")
# def dashboard():
#     if "user" in session:
#         return f"<h1>Welcome, {session['user']}!</h1> <a href='/logout'>Logout</a>"
#     return redirect(url_for("hello_world"))

# @app.route("/logout")
# def logout():
#     session.pop("user", None)  # Remove user session
#     flash("Logged out successfully", "info")
#     return redirect(url_for("hello_world"))

# if __name__ == "__main__":
#     app.run(debug=True, port=900)
import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  

try:
    cred = credentials.Certificate("firebase_config.json")  
    firebase_admin.initialize_app(cred)
except Exception as e:
    print("Firebase initialization error:", e)

# api integration
FIREBASE_WEB_API_KEY = "AIzaSyDf01kIREXdWSCQg_MBP2CGTef8teeHUUc"
# login

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Please enter both email and password", "danger")
            return render_template("index.html")

        try:
        #  firebase integration
            login_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_WEB_API_KEY}"
            data = {"email": email, "password": password, "returnSecureToken": True}

            response = requests.post(login_url, json=data)
            result = response.json()

            if "idToken" in result:
                session["user"] = result["email"]
                flash("Login successful!", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Invalid email or password", "danger")

        except Exception as e:
            flash(f"Error: {str(e)}", "danger")

    return render_template("index.html")

# register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        if not username or not email or not password:
            flash("All fields are required!", "danger")
            return render_template("register.html")

        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return render_template("register.html")

        try:
            # new user
            user = auth.create_user(
                email=email,
                password=password,
                display_name=username
            )
            flash("Account created successfully! You can now log in.", "success")
            return redirect(url_for("hello_world"))
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")

    return render_template("register.html")

# Dashb
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return f"<h1>Welcome {session['user']}!</h1> <a href='/logout'>Logout</a>"
    return redirect(url_for("hello_world"))

# logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully", "info")
    return redirect(url_for("hello_world"))

if __name__ == "__main__":
    app.run(debug=True, port=900)
