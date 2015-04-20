import json
import cache
from apps.requests.tracker import track_send


def request_send(topic, args, async=True, debug=False, token=None):

    request = {
        'topic': topic,
        'args': args,
        'async': 'true' if async else 'false',
        'debug': 'true' if debug else 'false'
    }

    if token:
        request.update({'token': token})

    track_send(request)

    payload = json.dumps(request).encode()

    cache.ws.send(payload)
