from flask_socketio import SocketIO, Namespace


class PWebSocket(Namespace):
    web_socket: SocketIO = None

    @staticmethod
    def init_app(pweb_app):
        PWebSocket.web_socket = SocketIO(app=pweb_app)
