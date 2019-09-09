from flask import Flask, render_template, request, redirect, session
import random, datetime	

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')         
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['message'] = ""
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])         
def process_money():
    which_form = request.form['which_form']

    if which_form == "farm":
        num = random.randint(10, 20)
        session['gold'] += num 
        session['message'] = "<li>Earned {} golds from the {} ({})</li>".format(num, which_form, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')) + session['message']
    elif which_form == "cave":
        num = random.randint(5, 10) 
        session['gold'] += num
        session['message'] = "<li>Earned {} golds from the {} ({})</li>".format(num, which_form, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')) + session['message']
    elif which_form == "house":
        num = random.randint(2, 5) 
        session['gold'] += num
        session['message'] = "<li>Earned {} golds from the {} ({})</li>".format(num, which_form, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')) + session['message']
    elif which_form == "casino":
        num = random.randint(-50, 50)
        session['gold'] += num
        if num < 0:
            session['message'] = "<li class='red'>Entered a casino and lost {} golds ... Ouch ({})</li>".format(num, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')) + session['message']
        else:
            session['message'] = "<li>Entered a casino and earned {} golds ({})</li>".format(num, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')) + session['message']

    return redirect("/")

@app.route('/reset')
def clear_session():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again"

if __name__=="__main__":   
    app.run(debug=True)    