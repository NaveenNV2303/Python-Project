from flask import Flask

app = Flask(__name__)

@app.route("/")
def testConnection():
 return("Connection is established successfully on dev")
  
if __name__ == "__main__":
 app.run(host='0.0.0.0', port='8080', ssl_context=('cert.pem', 'privkey.pem'))
