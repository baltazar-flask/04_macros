from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Control structures - for
@app.route("/for")
def cs_for():
    comments = ['Odlično', 'Ne razumijem', 'Nije loše']
    return render_template('cs-for.html',comments=comments)
# http://localhost:5000/for/

# Control structures - macros
@app.route("/macro-alone")
def cs_macro_alone():
    comments = ['Odlično', 'Ne razumijem', 'Nije loše']
    return render_template('cs-macro-alone.html',comments=comments)
# http://localhost:5000/macro-alone/

# Control structures - import, macros
@app.route("/macro-import/")
def cs_macro_import():
    comments = ['Odlično', 'Ne razumijem', 'Nije loše']
    return render_template('cs-macro-import.html',comments=comments)
# http://localhost:5000/macro-import/

# Control structures - import, macros
@app.route("/macro-gumb/")
def cs_macro_gumb():    
    return render_template('cs-macro-gumb.html')
# http://localhost:5000/macro-gumb/
