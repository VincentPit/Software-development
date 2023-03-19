from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "super_secret_key"

DATABASE = 'database.db'

# create a users table in the database
def create_table():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")

# login endpoint
@app.route('/login', methods=['GET'])
def login():
    username = request.json['username']
    password = request.json['password']

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    # check if the user exists
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cursor.fetchone()

        if not row:
            return jsonify({'message': 'User not found. Please sign up!'}), 404

        # check if the password is correct
        if password == row[2]:
            return jsonify({'message': 'Login successful.'}), 200
        else:
            return jsonify({'message': 'Incorrect password.'}), 401


# sign up endpoint
@app.route('/login/signup', methods=['GET','POST'])
def signup():
    username = request.json['username']
    password = request.json['password']

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    # check if the username is already in use
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cursor.fetchone()

        if row:
            return jsonify({'message': 'Username already exists.'}), 400

        # create the new user
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connection.commit()

        return jsonify({'message': 'User created successfully.'}), 201



if __name__ == '__main__':
    create_table()
    app.run(debug=True)
