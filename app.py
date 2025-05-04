from flask import Flask, render_template, request
from pow_core import evaluatePowREPL
import logging

logger = logging.getLogger(__name__)
FORMAT = "🐛 [%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/eval', methods=['POST'])
def eval():
    data = request.get_json()
    print(f' {data}')
    return {"res": evaluatePowREPL(data.get('expr'))}, 200

if __name__ == '__main__':
    app.run(debug=True)