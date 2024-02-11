from flask import Flask, request

app = Flask(__name__)

# Обработка GET-запроса
@app.route('/', methods=['GET'])
def handle_get():
    return 'Hello, World! (GET)'

# Обработка POST-запроса
@app.route('/receive-post', methods=['POST'])
def handle_post():
    data = request.form if request.form else request.json
    return f'Hello, World! (POST)\nReceived data: {data}'

if __name__ == '__main__':
    app.run(debug=True)
