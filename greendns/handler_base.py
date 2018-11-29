# -*- coding: utf-8 -*-
from greendns import session


class HandlerBase(object):
    def __init__(self):
        pass

    def add_arg(self, parser):
        pass

    def parse_arg(self, parser, remaining_argv):
        pass

    def init(self, io_engine):
        return []

    def parse_addr(self, s):
        addr = s.split(':')
        if len(addr) == 1:
            return (addr[0], 53)
        else:
            return addr[0], int(addr[1])

    def get_session(self):
        return session.Session()

    def on_client_request(self, sess):
        return (True, None)

    def on_upstream_response(self, sess, addr):
        return None

    def on_timeout(self, sess):
        return None
