from flask import *
from flask_socketio import *
import os
app = Flask(__name__, static_folder="static")
app.config["SECRET_KEY"] = 'secret!'
socket = SocketIO(app)
@socket.on('connected')
def connected():
    print('recived message: 123abc')
    
@app.route("/")
def index():
    return render_template('SpaceGame.html')

@app.route("/starblast.html")
def game():
    return render_template('starblast.html')
if __name__ == "__main__":
        print("sever start")
        print("client loaded")
        port = int(os.environ.get("PORT", 5000))
        socket.run(app, debug=False, host='0.0.0.0', port=port)
