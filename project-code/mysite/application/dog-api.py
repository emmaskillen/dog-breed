from flask import Flask
import requests

app = Flask(__name__)
    
@app.route('/fact')
def test():
    response = requests.get("https://dogapi.dog/api/v2/facts")
    if response.status_code == 200:
        return response.json()
    else:
        print("Error making request!")
     
    
if __name__ == '__main__':
    #app.run(debug = True)
    app.run(port=8004)