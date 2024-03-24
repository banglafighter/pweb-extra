from abc import ABC


class PwebSocketConf(ABC):
    def on_unhandled_error(self, errors):
        pass

    def on_slash_error(self, errors):
        pass
