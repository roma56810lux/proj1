from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/404')
def error_404():
    return '404 Not Found', 404

@app.route('/phone')
def phone():
    return render_template('phone.html')

@app.route('/tablet')
def tablet():
    return render_template('tablet.html')

clicked = False

@app.route('/api/click', methods=['POST'])
def trigger_click():
    global clicked
    clicked = True
    return jsonify({"status": "ok"})

@app.route('/api/click/status')
def click_status():
    global clicked
    if clicked:
        clicked = False
        return jsonify({"clicked": True})
    else:
        return jsonify({"clicked": False})

if __name__ == '__main__':
    app.run(debug=True)