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


#     # Integrate your code to fetch all films from the database
#     # For now, we'll use a placeholder list
#     films = [("1", "Film1", "2000", "G", "120", "Action"), ("2", "Film2", "2005", "PG", "150", "Drama")]
#     return render_template('films.html', films=films)

# @app.route('/update', methods=['GET', 'POST'])
# def update_select():
#     if request.method == 'POST':
#         film_id = request.form['film_id']
#         return redirect(url_for('update_film', film_id=film_id))
#     return render_template('update_select.html')

# @app.route('/update/<film_id>', methods=['GET', 'POST'])
# def update_film(film_id):
#     if request.method == 'POST':
#         # Here, integrate your updateFilms code to update the film details in the database
#         return redirect(url_for('view_films'))  # Redirect to the films page after updating
#     # Fetch the current details of the film using film_id and pass them to the template
#     # For now, we'll use placeholder details
#     film_details = ("Film1", "2000", "G", "120", "Action")
#     return render_template('update_film.html', film_details=film_details)

# @app.route('/delete', methods=['GET', 'POST'])
# def delete_film():
#     if request.method == 'POST':
#         film_id = request.form['film_id']
#         # Here, integrate your deleteFilms code to delete the film from the database
#         return redirect(url_for('view_films'))  # Redirect to the films page after deleting
#     return render_template('delete_film.html')


if __name__ == '__main__':
    app.run(debug=True)