import {SIOConnect, SocketIO} from "../common/reexport";
import {RapidException} from "react-rapid-app";

export interface SocketIOWSConf {
    url?: string
    path?: string
    connect?: () => void
    disconnect?: () => void
    setGetEvent?: (socketIO: SocketIO) => void
}

export default class SocketIOWS {
    private socketIO!: SocketIO;
    private readonly config!: SocketIOWSConf

    constructor(config?: SocketIOWSConf) {
        if (config) {
            this.config = config
        }
        this.socketIO = SIOConnect(this.getUrl(), {
            path: this.getPath()
        })
        this.initCallBack()
        if (this.config && this.config.setGetEvent) {
            this.config.setGetEvent(this.socketIO)
        }
    }

    private getUrl() {
        let url: any = process.env["WS_URL"] || this.config.url;
        if (!url) {
            throw new RapidException("Websocket URL Not found")
        }
        return url
    }

    private initCallBack() {
        this.socketIO.on("connect", () => {
            if (this.config && this.config.connect) {
                this.config.connect()
            }
        })

        this.socketIO.on("disconnect", () => {
            if (this.config && this.config.disconnect) {
                this.config.disconnect()
            }
        })
    }

    private getPath() {
        if (this.config && this.config.path) {
            return this.config.path
        }
        return "/pweb-socket"
    }

}