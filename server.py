from flask import Flask,render_template
from flask_socketio import SocketIO,emit

app=Flask(__name__)

app.config['SECRET_KEY']="b'!\xf7\x9e4\x02\x07\xddd\xa1\x9d\xc0\xc6O\xde\xb8\rz\xea\xb1\xc9\xa5\xa9\x92\x1f'"

socketio=SocketIO(app)


@app.route('/')
def index():
    return render_template("./index.html")

@socketio.on('my event')
def sendToclients(json):
    ##print('received something:'+str(json))
    socketio.emit('my response',json)

if __name__=="__main__":
    socketio.run(app,debug=False)