import json
from threading import Thread
from ws4py.client.threadedclient import WebSocketClient
import cache
from apps.requests.tracker import track_recv


class DummyClient(WebSocketClient):
    def opened(self):
        self.is_open = True

    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    def received_message(self, m):
        print(m)
        if m.is_text:
            recv = m.data.decode('utf-8')
            request = json.loads(recv)
            track_recv(request)
        if len(m) == 175:
            self.close(reason='Bye bye')

ws = DummyClient('ws://127.0.0.1:9001/')

try:
    is_open = ws.is_open
except AttributeError:
    is_open = False

if not is_open:
    ws.connect()
    t = Thread(target=ws.run_forever)
    t.start()
    cache.ws = ws
