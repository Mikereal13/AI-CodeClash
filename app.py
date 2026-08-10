# Gemma agent for AI Powered Super Hero Clashing Simulator
#Will be used to pull stats on two selected super heros and 
#create a story simulating their battle 

#IMPORTS Dependencies 
from flask import Flask, render_template

app = Flask(__name__,template_folder='Pages', static_folder='static')
app.config['APP_NAME'] = 'Super Hero Duke Out'


#pages
@app.route("/")
def login():
    return render_template("home.html")

#Boot The Server
def run():
    if __name__ == '__main__':
        app.run(debug=True)
run()



