from flask import Flask, render_template, request
from pow_core import evaluatePowREPL
import logging
import re
import traceback

logger = logging.getLogger(__name__)
FORMAT = "🐛 [%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route('/')
def home():
    return render_template('index.html')

def log(msg):
    logger.log(logging.DEBUG, msg)

def verify_input(unpure):
    _buffer = ''
    for x in unpure.split(' '):
        log(f'SPLIT: {unpure.split(' ')}')
        #_buffer += x
        log(f'BUFFER: {_buffer}')
        
        if re.search(r'\+', x):
            _buffer += '+'
            continue
        elif re.search('-', x):
            _buffer += '-'
            continue
        elif re.search(r'\*', x):
            _buffer += '*'
            continue
        elif re.search('/', x):
            _buffer += '/'
            continue
        elif re.search(r'\(', x):
            _buffer += '('
            continue
        elif re.search(r'\)', x):
            _buffer += ')'
            continue
        if re.search(r'%>', x):
            _buffer += '%>'
            continue
        if re.search(r'\d+', x):
            _buffer += x
            continue
        else:
            raise SyntaxError('Invalid syntax')
    return _buffer

@app.route('/eval', methods=['POST'])
def eval():
    data = request.get_json()
    log(f'Data coming in: {data}')

    log(f'Evaluating...: {data.get('expr')}')
    _verified_evaluated = None

    try:
        _verified_evaluated = evaluatePowREPL(verify_input(data.get('expr').strip()))
        log(f'Evaluated correctly!')
    except:
        log(f'There was a goddamn error evaluating')
        print(traceback.format_exc())
    
    return {"res": _verified_evaluated or 'ERR'}, 200

if __name__ == '__main__':
    app.run(debug=True)