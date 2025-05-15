from flask import Flask, render_template, request, session, redirect, url_for, make_response, jsonify, send_from_directory



app = Flask(__name__)

app.secret_key = 'Im@B@ybl@de12309'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)