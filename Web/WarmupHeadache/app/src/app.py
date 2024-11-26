from flask import Flask, render_template, request, request, make_response
import logging

app = Flask(__name__, template_folder='views', static_folder='static')


def is_malicious(base: str):
    banned = [ ";", "//", "../", "<", ">", "script", "on", "+", "-"]
    if any(b in base for b in banned):
        logging.info('banned word detected: ' + base)
        return True
    return False

@app.after_request
def apply_csp(response):
    if request.remote_addr != "1.3.3.7":
        response.headers['Content-Security-Policy'] = "default-src 'self';script-src 'self'"
    return response

@app.route('/', methods = ['GET'])
def index():
    img = request.args.get('img_url')
    if not img:
        img = "/static/frwhite.png"
    cfo = request.args.get('cfo')
    if cfo:
        if is_malicious(cfo):
            return render_template('index.html', image=img, custom_function_output="")
    return render_template('index.html', image=img, custom_function_output=cfo)

@app.errorhandler(404)
def page_not_found(e):
    path = request.path
    return f"/{path} page was not found on this server."

if __name__ == '__main__':
   logging.basicConfig(level=logging.INFO)
   logging.warning('Starting server... at port 1871')
   app.run(host='0.0.0.0',port=1871, debug=True)