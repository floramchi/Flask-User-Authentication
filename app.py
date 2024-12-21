from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from datetime import datetime
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb+srv://t23157:Florina@cluster0.ifbuv.mongodb.net/myDatabase?retryWrites=true&w=majority"  # MongoDB Atlas URI
mongo = PyMongo(app)

# Test MongoDB connection
try:
    mongo.db.command("ping")
    print("MongoDB connection successful")
except Exception as e:
    print("MongoDB connection failed:", e)

# User collection
users_collection = mongo.db.users

@app.route('/')
def home():
    username = session.get('username')
    if username:
        user = users_collection.find_one({"username": username})
        user_posts = mongo.db.posts.find({"username": username})  # assuming you have posts
        return render_template('home.html', user=user, posts=user_posts)
    else:
        return render_template('home.html', user=None, posts=None)



@app.route('/profile')
def profile():
    # Check if the user is logged in
    if 'username' not in session:
        flash('You must be logged in to view your profile', 'warning')
        return redirect(url_for('login'))

    # Fetch user data from MongoDB
    user = users_collection.find_one({"username": session['username']})
    
    # If user is found, render the profile page with user details
    if user:
        return render_template('profile.html', user=user)
    
    # If user is not found, redirect to login
    flash('User not found', 'danger')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users_collection.find_one({"username": username})
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session['username'] = username
            # Update last login time
            users_collection.update_one(
                {"username": username},
                {"$set": {"last_login": datetime.now()}}
            )
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form.get('email')  # Use .get() instead of directly accessing it

        # Check if the username already exists in MongoDB
        if users_collection.find_one({"username": username}):
            flash('Username already exists', 'danger')
        else:
            # Hash the password before saving it
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            # Save the user with email
            users_collection.insert_one({"username": username, "password": hashed_password, "email": email})
            flash('Sign-up successful! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, threaded=False)