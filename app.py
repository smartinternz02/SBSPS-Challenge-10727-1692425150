from flask import Flask, render_template, request,session
app = Flask(__name__)
app.secret_key ='a'

print("Flask running")

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/analytics')
def analytics():
    return render_template('analytics.html')
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/story')
def story():
    return render_template('story.html')

if __name__ =='__main__':
    app.run( debug = True)
