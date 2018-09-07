from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/test')
def test():
    return "test"

@app.route('/xymon', methods=['POST','GET'])
def xymon():
        if request.method=='GET':
                return "get"
        if request.method=='POST':
#               return str(request.get_json(force=True))
#               returndata=request.content_length
                #return str(request.form.get('param1'))
                app.logger.debug( str(request.get_data()))
                return str(request.get_data())

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
