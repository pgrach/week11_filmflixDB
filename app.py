from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

import sqlite3 as sql
# Function to get a new connection to the database
def get_db_connection():
    dbCon = sql.connect("filmflix_new.db")
    dbCursor = dbCon.cursor()
    return dbCon, dbCursor

# Ensure the table exists before starting the app
conn, cursor = get_db_connection()
cursor.execute("""
CREATE TABLE IF NOT EXISTS "tblfilms" (
"filmID" INTEGER NOT NULL UNIQUE, 
"title" TEXT, 
"yearReleased" INTEGER,
"rating" TEXT,
"duration" INTEGER,
"genre"TEXT,
PRIMARY KEY (filmID AUTOINCREMENT)
)""")
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

# Add Films
# Delete Films
# Update Films
# View All Films

@app.route('/add', methods=['GET','POST'])
def add_film():
    if request.method == 'POST':
        filmTitle = request.form['title']
        filmYear = int(request.form['year'])
        filmRating = request.form['rating']
        filmDuration = int(request.form['duration'])
        filmGenre = request.form['genre']
# Get a new database connection and cursor
        dbCon, dbCursor = get_db_connection()
        dbCursor.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)", 
                         (filmTitle, filmYear, filmRating, filmDuration, filmGenre))
        dbCon.commit()
        dbCon.close()

        return redirect(url_for('index'))  # Redirect to the main page after adding
    
    return render_template('add_film.html')

@app.route('/films')
def view_films():
    dbCon, dbCursor = get_db_connection()  # Using the get_db_connection() function set up above to connect to  DB
    dbCursor.execute("SELECT * FROM tblfilms")
    films = dbCursor.fetchall()
    dbCon.close()
    
    return render_template('films.html', films=films)

@app.route('/delete', methods=['GET', 'POST'])
def delete_film():
    if request.method == 'POST':
        film_id = request.form['film_id']

# Get a new database connection and cursor
        dbCon, dbCursor = get_db_connection()
        dbCursor.execute("DELETE FROM tblfilms WHERE filmID = ?", 
                         (film_id,))
        dbCon.commit()
        dbCon.close()

        return redirect(url_for('index'))  # Redirect to the main page after adding
    
    return render_template('delete_film.html')


@app.route('/update', methods=['GET', 'POST'])
def update_select():
    if request.method == 'POST':
        film_id = request.form['film_id']
        return redirect(url_for('update_film', film_id=film_id))
    return render_template('update_select.html')

@app.route('/update/<film_id>', methods=['GET', 'POST'])
def update_film(film_id):
    dbCon, dbCursor = get_db_connection()
    if request.method == 'POST':
        # Getting form data
        title = request.form.get('title')
        yearReleased = request.form.get('yearReleased')
        rating = request.form.get('rating')
        duration = request.form.get('duration')
        genre = request.form.get('genre')

        # Update database record
        dbCursor.execute("UPDATE tblfilms SET title=?, yearReleased=?, rating=?, duration=?, genre=? WHERE filmID=?", 
                         (title, yearReleased, rating, duration, genre, film_id))
        dbCon.commit()
        dbCon.close()

        return redirect(url_for('view_films'))

    # Fetch the current details of the film using film_id
    dbCursor.execute("SELECT * FROM tblfilms WHERE filmID=?", (film_id,))
    film_details = dbCursor.fetchone()
    dbCon.close()

    return render_template('update_film.html', film_details=film_details)

if __name__ == '__main__':
    app.run(debug=True)