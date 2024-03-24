from flask_socketio import SocketIO
from ppy_common import Console
from pweb_extra.pws.pweb_socket_conf import PwebSocketConf


class PWebSocket:
    web_socket: SocketIO = None
    config: PwebSocketConf = None

    @staticmethod
    def register(pweb_app, config: PwebSocketConf = None):
        PWebSocket.web_socket = SocketIO(app=pweb_app)
        PWebSocket().__init_configuration(PWebSocket.web_socket, config=config)
        Console.info("Registered PWebSocket", system_log=True)

    def __init_configuration(self, web_socket: SocketIO, config: PwebSocketConf = None):
        self.config = config

        # Manage Errors
        web_socket.default_exception_handler = self.on_unhandled_error
        web_socket.exception_handlers["/"] = self.on_slash_error
        self.register_error(web_socket.exception_handlers)

    def on_unhandled_error(self, errors):
        Console.error(f"PWebSocket Unhandled Errors: {errors}")
        if self.config and self.config.on_unhandled_error:
            self.config.on_unhandled_error(errors)

    def on_slash_error(self, errors):
        Console.error(f"PWebSocket Slash Errors: {errors}")
        if self.config and self.config.on_slash_error:
            self.config.on_slash_error(errors)

    def register_error(self, exception_handlers):
        pass
