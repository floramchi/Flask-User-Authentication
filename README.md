# Flask Authentication App

This is a simple **Flask** web application that demonstrates user authentication (signup, login, logout) and displays user profiles. It is connected to **MongoDB** for storing user data and provides features like password hashing and session management.

## Features
- **User Registration (Sign-up)**: Users can create an account with a username, password, and email.
- **User Authentication (Login/Logout)**: Users can log in using their credentials and access the home page. After logging out, they are redirected to the home page.
- **Profile Management**: Logged-in users can view and manage their profiles.
- **MongoDB Integration**: The app is connected to MongoDB Atlas for storing user data.
- **Password Hashing**: Passwords are hashed using `bcrypt` for security.
- **Session Management**: Flask sessions are used to keep track of logged-in users.

## Prerequisites
Make sure you have the following installed on your machine:

- **Python 3.x**
- **Flask** (Python web framework)
- **Flask-PyMongo** (MongoDB integration)
- **bcrypt** (for hashing passwords)
- **python-dotenv** (for managing environment variables)

## Setup and Installation

### Clone the repository
```bash
git clone git clone https://github.com/floramchi/flask-auth-app.git
cd flask-auth-app


