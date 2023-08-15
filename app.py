from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'open1234App'  # This key is used for session security.

@app.route('/', methods=['GET', 'POST'])
def main_menu():
    # If user submits the form
    if request.method == 'POST':
        choice = request.form.get('choice')
        
        if choice == '1':
            return redirect(url_for('add_film'))
        elif choice == '2':
            return redirect(url_for('delete_film'))
        elif choice == '3':
            return redirect(url_for('update_film'))
        elif choice == '4':
            return redirect(url_for('list_films'))
        else:
            return "Goodbye!"
    
    return render_template('main_menu.html')

@app.route('/films')
def list_films():
    from printAll import print_all
    films = print_all()
    return render_template('films.html', films=films)
