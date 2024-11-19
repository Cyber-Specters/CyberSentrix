import requests
import os
import requests as ak
import requests as khir
import jwt
from flask import Flask, render_template, request, request, make_response
import requests as nya
import requests as sa
from playwright.sync_api import sync_playwright, Playwright, TimeoutError as PlaywrightTimeoutError
from urllib.parse import urlparse
import requests as da
import socket
import time
import logging
import random
import hashlib
import requests as rjga
import secrets
import requests as request_super_faster_then_others


secret = secrets.token_hex(20)
app = Flask(__name__, template_folder='views')
flag = os.getenv("flag") or "flag{flag}"


def check_if_its_google(host):
    try:
        google_host_ip = socket.gethostbyname('google.com')
        google_prefix = ".".join(google_host_ip.split(".")[:3])
        real_host = host
        if host.startswith("http"):
            hostb = urlparse(host).hostname
            # logging.warning('bandingin aja si', hostb)
            real_host = socket.gethostbyname(str(hostb).replace('www.', ''))
        real_prefix = ".".join(real_host.split(".")[:3])

        logging.warning(f"Resolved IP for given host: {real_host} with google {google_host_ip}")
        if real_prefix == google_prefix:
            return True
        return False
    except Exception as e:
        logging.warning(f"Error resolving host: {e}")
        return False

# Research make ur skill up to date
@app.route('/hosts', methods = ['GET', 'POST', 'DELETE'])
def go_ping():
    if request.method == 'GET':
        wpop = request.args.get('pop')
        if wpop:
            if wpop.strip() == '':
                logging.warning(f'{request.remote_addr}: {wpop}')
                return render_template('hacker.html', ip=request.remote_addr) 
            if wpop.count('http') > 1:
                logging.warning(f'{request.remote_addr}: {wpop}')
                return render_template('hacker.html', ip=request.remote_addr) 
            host = wpop.split("http")      
            if len(host) > 1:
                if len(wpop) > 11 or len(host[1]) > 4: 
                    logging.warning(f'{request.remote_addr}: {wpop}')
                    return render_template('hacker.html', ip=request.remote_addr) 
        else:
            wpop = 'https://google.com'
        return render_template('index.html', wpop=wpop)
    elif request.method == 'POST':
        host = request.form.get('host')
        if 'google' in host:
            logging.warning(f'{request.remote_addr}: {wpop}')
            return render_template('hacker.html', ip=request.remote_addr)
        svc = socket.gethostbyname(host)
        if check_if_its_google(svc):
            resp = make_response(render_template('index.html'))
            enc_jwt = jwt.encode({"simulate_admin": "ofcourse"}, secret, algorithm="HS256")
            enc_jwt_str = enc_jwt.decode('utf-8') if isinstance(enc_jwt, bytes) else enc_jwt
            resp.set_cookie('jwt2', enc_jwt_str)
            return resp
        else: 
            return {
                'error':'Not allowed ping outside of a master IP'
            }
        
# Research make ur skill up to date
@app.route('/requests', methods = ['GET', 'POST', 'DELETE'])
def go_request():
    if request.method == 'GET':
        try:
            whead = request.args.get('head')
            val = request.args.get('val')
            if "\n" in whead or "\r" in whead:
                logging.warning(f'{request.remote_addr}: {whead}: {val}')
                return render_template('hacker.html', ip=request.remote_addr) 
            if "\n" in val:
                logging.warning(f'{request.remote_addr}: {whead}: {val}')
                return render_template('hacker.html', ip=request.remote_addr) 
            if "1" in request.args.debug:
                r = request.get(request.args.get('serper_side_request_kedong_oan'), headers={whead: val})
                if r.status_code == request.args.get('lah_kata_kedong_oan'):
                    return {"gotcha":"you are a real hacker isnt? lets submit your CVE.","this your prize":r.text}
                else:
                    logging.warning(f'{request.remote_addr}: {whead}: {val}')
                    return render_template('hacker.html', ip=request.remote_addr) 
            elif "2" in request.args.debug:
                r = rjga.get("https://google.com", headers={whead: val})
                if r.status_code == request.args.get('lah_kata_kedong_oan'):
                    return {"gotcha":"you are a real hacker isnt? lets submit your CVE.","this your prize":r.text}
                else:
                    logging.warning(f'{request.remote_addr}: {whead}: {val}')
                    return render_template('hacker.html', ip=request.remote_addr) 
        except:
            pass
        return render_template('index.html')
    elif request.method == 'POST':
        url = request.form.get('url')
        if not url.startswith("http://youtube.com"):
            logging.warning(f'{request.remote_addr}: {whead}: {val}')
            return render_template('hacker.html', ip=request.remote_addr) 
        if url.startswith("http://youtube.com@"):
            logging.warning(f'{request.remote_addr}: {whead}: {val}')
            return render_template('hacker.html', ip=request.remote_addr) 
        if url.startswith("http://youtube.com?"):
            return {'error':'You sure u are a hacker? not skilled enough.'}
        if "flag" in url:
            return {'error':'You sure u are a hacker? not skilled enough.'}
        req = requests.get(url, timeout=3)
        if check_if_its_google(req.url):
            resp = make_response(render_template('index.html'))
            enc_jwt = jwt.encode({"simulate_admin": "yes"}, secret, algorithm="HS256")
            enc_jwt_str = enc_jwt.decode('utf-8') if isinstance(enc_jwt, bytes) else enc_jwt
            resp.set_cookie('jwt', enc_jwt_str)
            return resp
        else: 
            return {
                'error':'Not allowed ping outside of a master IP'
            }
            
@app.route('/debug', methods = ['GET'])
def debug():

    data = random.getrandbits(32)
    if request.args.get('debug'):
        return {"hash":data}
    logging.warning('hash: ',data)
    client_ip = request.remote_addr
    if client_ip == '1.3.3.7' or data == int(request.args.get('hash')):
        hash_flag = request.args.get('flag')
        if hash_flag == hashlib.md5(flag.encode()).hexdigest():
            return flag
        else:
            return "Access Denied: Wrong Flag"
    else:
        return "Access Denied: Not local IP"



@app.route('/check', methods = ['GET', 'POST', 'DELETE'])
def check():
    if request.method == 'POST':
        if request.cookies.get('jwt'):
            if request.cookies.get('jwt2'):
                try:
                    decoded_jwt = jwt.decode(request.cookies.get('jwt'), secret, algorithms=['HS256'])
                    decoded_jwt2 = jwt.decode(request.cookies.get('jwt2'), secret, algorithms=['HS256'])
                    simulate_admin_status = decoded_jwt.get("simulate_admin")
                    simulate_admin_status2 = decoded_jwt2.get("simulate_admin")
                except:
                    return render_template('hacker.html', ip=request.remote_addr)
                if simulate_admin_status == "yes" and simulate_admin_status2 == "ofcourse":
                    with sync_playwright() as p:
                        # why it firefox? dont seem sus? 
                        browser = p.firefox.launch(headless=True, args=[
                            '--disable-dev-shm-usage',
                            '--no-sandbox',
                            '--disable-setuid-sandbox',
                            '--disable-gpu',
                            '--no-gpu',
                            '--disable-default-apps',
                            '--disable-translate',
                            '--disable-device-discovery-notifications',
                            '--disable-software-rasterizer',
                            '--disable-xss-auditor'
                        ])
                        context = browser.new_context()
                        context.add_cookies([{
                            'name': 'jwt',
                            'httpOnly': False,
                            'value': hashlib.md5(flag.encode()).hexdigest(),
                            'url': 'http://localhost:1811'
                        }])
                        if request.form.get('timeout') is None:
                            default_timeout = 15000 # milliseconds 15000ms jadi  15 seconds
                        else :
                            default_timeout = int(request.form.get('timeout'))
                        if default_timeout > 60000:
                            return "maksimal 1 menit aja ya bang"
                        context.set_default_timeout(default_timeout)
                        context.set_extra_http_headers({'X-Auth': os.getenv('X-Auth')})
                        page = context.new_page()
                        try:

                            page.goto('http://localhost:1811/hosts?pop='+request.form.get('pop_rdi'), wait_until='load', timeout=10 * 1000)

                            page.locator('#headache-category').fill(request.form.get('category')) 
                            page.locator('#my-headache').fill(request.form.get('my-headache'))  
                            page.locator('#your-headache').fill(request.form.get('your-headache')) 

                            page.locator('#number-selector').fill(request.form.get('number-selector'))  
                            page.locator('#number-happy').fill(request.form.get('number-happy'))

                            page.locator('button:has-text("Submit my headache")').click()
                            # page.close(run_before_unload=True)
                        except PlaywrightTimeoutError:  
                            context.close()
                            browser.close()
                            return "visited! and timeout already achieved!"
                        # time.sleep(5000)
                        context.close()
                        browser.close()
                        return "sukses visit nya bang"
                
                else:
                    
                    return render_template('hacker.html', ip=request.remote_addr)
        else:
            return "you are not an authenticated user"   
    else:
        if request.cookies.get('jwt'):
            try:
                decoded_jwt = jwt.decode(request.cookies.get('jwt'), secret, algorithms=['HS256'])
                simulate_admin_status = decoded_jwt.get("simulate_admin")
                if simulate_admin_status == "yes":
                    return render_template('simulate_admin.html')
                else:
                    return "this feature is not available for you"
            
            except jwt.ExpiredSignatureError:
                return "Token has expired, please log in again."
            except jwt.InvalidTokenError:
                return "Invalid token, please log in again."
        else:
            return render_template("hacker.html")
    
        
if __name__ == '__main__':
   logging.basicConfig(level=logging.INFO)
   logging.warning('Starting server... at port 1811')
   app.run(host='0.0.0.0',port=1811, debug=False)