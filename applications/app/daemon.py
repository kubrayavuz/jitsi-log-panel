#!/usr/bin/python3
# -*- coding:utf-8 -*-

from app.mydaemon import Daemon
from app.api.functions import getLogger
from subprocess import  run, TimeoutExpired
import atexit
import datetime
import sys
import os

LOG_PATH = '/tmp/log'
DAEMON_NAME = 'My Background Process (id: #ID#)'
DAEMON_STOP_TIMEOUT = 10
PIDFILE = '/tmp/process_#ID#.pid'
RUNFILE = '/tmp/process_#ID#.run'
DEBUG = 0


def get_args():
    try:
        uniq_id = sys.argv[1]
        command = sys.argv[2]
        command_list = sys.argv[3:]
    except Exception as e:
        logger.error('args error')
        return (None, None, None, None)
    return (uniq_id, command, command_list)


class ProcessDaemon(Daemon):
    def createPath(self):
        path = '/tmp/log/' + command + '/'
        if not os.path.exists(path):
            os.mkdir(path)
        print(command_list)
        # path += command_list[2]

        return path

    def runSubprocess(self, out, cmd):
        try:
            p = run(cmd, stdout=out, stderr=out)
            returncode = p.returncode
        except TimeoutExpired:
            out.write('process ran too long')
            returncode = None
        return returncode


    def run(self):
        atexit.register(self.delrun)
        while os.path.exists(RUNFILE):
            path = self.createPath()
            # out = open(path, 'w+')

            # break


if __name__ == '__main__':
    try:
        logger = getLogger('script', LOG_PATH)
        # Get arguments.
        (uniq_id, command, command_list) = get_args(

        # Create daemon object.
        DAEMON_NAME = DAEMON_NAME.replace('#ID#', uniqId)
        PIDFILE = PIDFILE.replace('#ID#', uniqId)
        RUNFILE = RUNFILE.replace('#ID#', uniqId)

        logger.info('Started %s script daemon' % (command))
        d = ProcessDaemon(name=DAEMON_NAME, pidfile=PIDFILE, runfile=RUNFILE,
                   stoptimeout=DAEMON_STOP_TIMEOUT, debug=DEBUG)
        d.start()
        sys.exit(0)
    except Exception as err:
        logger.info('Exception' % str(err))
        if DEBUG:
            raise
        else:
            sys.stderr.write('%s\n' % err)

        sys.exit(1)