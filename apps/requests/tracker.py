import cache


def track_recv(request):

    if 'code' not in request:
        print('Bad bad bad:', request)
        return

    if request['code'] == 302:
        cache.__waiting_requests__.append(request['request_id'])
    else:
        cache.__waiting_requests__.remove(request['request_id'])
        cache.__requests__[request['request_id']] = {
            'sent': cache.__pending_requests__.pop(0),
            'recv': request
        }

    cache.call('request').requests_recv.update(request)


def track_send(request):
    cache.__pending_requests__.append(request)

    cache.call('request').requests_sent.update(request)
