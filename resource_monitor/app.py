from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

@app.route('/api/resources')
def get_resources():
    cpu_usage = psutil.cpu_percent(interval=0.5)
    ram_usage = psutil.virtual_memory().percent
    return jsonify({'cpu': cpu_usage, 'ram': ram_usage})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
