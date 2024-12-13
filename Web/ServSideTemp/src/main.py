from flask import Flask, render_template, render_template_string, request
import os

app = Flask(__name__)

def filter(string):
    blacklist = ['_', '"', '[', ']','%','%25','self','base','config', 'mro', ',', 'join', 'application', 'read', 'os', 'popen', 'txt', "init", "subprocess", "config", "update", "subclasses", "class", "+", "getitem", "globals", "import", "builtins", "attr", "render_template"]
    for i in blacklist:
        if i in string:
            return False
    return True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/succes")
def succes():
    pesan = request.args.get('pesan') 
    if pesan is None:
        return "No message provided."
    
    pesan = pesan.lower()
    try:
        if not filter(pesan):
            return render_template("fail.html")
        return render_template('succes.html', pesan=render_template_string(pesan))
    except:
        return "internal server error"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
