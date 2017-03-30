#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import logging
import logging.config


def openAppLogger():
    logging.config.fileConfig("conf/logger.conf")
    logger = logging.getLogger("example01")
    return logger

def openHttpLogger():
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)

if __name__ == '__main__':
    log = openAppLogger()
    log.error('fuck')
    log.info("nimamaipi")