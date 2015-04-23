import cache
import re


def track_recv(log):

    if '[DEBUG]' not in log:
        print('Bad bad bad:', log)
        return

    uuid = re.compile("[0-F]{8}-[0-F]{4}-[0-F]{4}-[0-F]{4}-[0-F]{12}",
                      re.I).findall(log[:90])

    if not uuid:
        print('Log', log, 'has no uuid')

    request_id = uuid[0]

    if request_id not in cache.__logs__:
        cache.__logs__[request_id] = [log]
    else:
        cache.__logs__[request_id].append(log)

    cache.call('request').requests_recv.update(log, request_id)
