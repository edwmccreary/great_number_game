from flask import Flask, render_template,session,redirect,request
from random import randint

app = Flask(__name__)
app.secret_key = 'my secret key'

@app.route('/')
def index():
    if not 'number' in session:
        session['number'] = randint(1,100)
    if not 'guess' in session:
        session['guess'] = 0
    if not 'tries' in session:
        session['tries'] = 5
    print('the number is ' + str(session['number']))
    if session['tries'] == 0:
        return redirect('/game_over')
    return render_template("index.html",number=session['number'],guess=session['guess'],tries=session['tries'])

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    print(request.form)
    session['guess'] = int(request.form['guess_number'])
    session['tries'] -= 1
    return redirect('/')

@app.route('/game_over')
def game_over():
    return render_template("game_over.html",number=session['number'])

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)