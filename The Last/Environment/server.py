from flask import Flask, request, render_template_string, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Setup SQLite database and create a users table
def init_db():
    conn = sqlite3.connect('flaskvault.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS secrets (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, secret TEXT)')
    c.execute('INSERT INTO users (username, password) VALUES ("admin", "admin")')
    c.execute('INSERT INTO secrets (user_id, secret) VALUES (1, "dGVjaG5vdmF0ZXtmbDRza19zcWwxXzFuajNjdDEwbn0=")')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('flaskvault.db')
        c = conn.cursor()

        # SQL query vulnerable to SQL injection
        c.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        user = c.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        else:
            return "Login Failed. Please try again."
    
    return '''
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']
        conn = sqlite3.connect('flaskvault.db')
        c = conn.cursor()
        c.execute(f"SELECT secret FROM secrets WHERE user_id={user_id}")
        secret = c.fetchone()
        conn.close()

        if secret:
            return f"Welcome to your dashboard! Your secret is: {secret[0]}"
        else:
            return "No secrets found for your user."
    else:
        return redirect(url_for('login'))

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9992, debug=True)

