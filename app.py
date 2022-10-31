from flask import Flask, jsonify

app = Flask(__name__)

student = [
    {'slackUsername' : 'Musa Dauda',
    'backend' : True,
    'age' : 20,
    'bio' : "I am a passionate programmer and a deligent learner"
    
    }
]

@app.route('/')
def home():
    return jsonify(student)

app.run()