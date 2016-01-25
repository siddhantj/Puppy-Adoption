
from flask import render_template
from myapp import app


@app.route('/')
@app.route('/index.html')
def welcome_page():
    # pdb.set_trace()
    return render_template('index.html')




