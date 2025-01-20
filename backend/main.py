from flask import Flask



app = Flask(__name__)
@app.route('/')
def home():
    return '<h3>Hello World</h3>'

@app.route('/api/')
def api():
    return {"message":"Route based API"}

class Home():
    def get(self):
        return {"message":"Class based API"}
@app.route('/home/')
def api():
    return 




if __name__=='__main__':
    app.run(debug=True)