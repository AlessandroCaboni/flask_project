from flask import Flask,render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from database import mydb
app = Flask(__name__)

@app.route("/")
# def hello():
#     return "Hello, World!"

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username'] 
    email = request.form['email']
    password = request.form['password']

    # Hash the password before storing in database
    password_hash = generate_password_hash(password)

    mycursor = mydb.cursor()
    sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    val = (username, email, password_hash)
    mycursor.execute(sql, val)
    mydb.commit()

    flash('You have successfully registered!')
    return redirect(url_for('login'))

  return render_template('register.html')

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['Username']
    password = request.form['Password']

    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE username = %s"
    val = (username,)
    mycursor.execute(sql, val)
    user = mycursor.fetchone()

    # Check if user exists and the password is correct
    if user and check_password_hash(user[3], password):
      session['user_id'] = user[0]
      session['username'] = user[1]
      return redirect(url_for('dashboard'))
    else:
      flash('Invalid username or password')

  return render_template('login.html')

# User dashboard
@app.route('/dashboard')
def dashboard():
  if 'user_id' in session:
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM posts")
    posts = mycursor.fetchall()

    return render_template('dashboard.html', username=session['username'], posts=posts)
  else:
    flash('You need to login first')
    return redirect(url_for('login'))

# User logout
@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('login'))






if __name__ == "__main__":
    app.run(debug=True)
