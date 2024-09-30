import logging

log = logging.getLogger('main.demo_log2')

def foo(x):
    log.info('x=%r' % x)
    return 3 * x

def goo(x):
    log = logging.getLogger('main.demo_log2.goo')
    log.info('x=%r' % x)
    log.debug('x=%r' % x)
    return 5 * x**2

def hoo(x):
    log = logging.getLogger('main.demo_log2.hoo')
    log.info('x=%r' % x)
    return 7 * x + 1
