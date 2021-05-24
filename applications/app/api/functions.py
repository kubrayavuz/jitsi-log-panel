import logging
import logging.handlers
import os


def getLogger(logname, logdir, logsize=500*1024, logbackup_count=4):
    if not os.path.exists(logdir):
        os.makedirs(logdir)

    logfile='%s/%s.log' % (logdir, logname)
    loglevel = logging.INFO
    logger = logging.getLogger(logname)
    logger.setLevel(loglevel)

    if logger.handlers is not None and len(logger.handlers) >= 0:
        for handler in logger.handlers:
            logger.removeHandler(handler)
        logger.handlers = []

    loghandler = logging.handlers.RotatingFileHandler(
        logfile, maxBytes=logsize, backupCount=logbackup_count)
    formatter = logging.Formatter(
        '%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    loghandler.setFormatter(formatter)
    logger.addHandler(loghandler)

    return logger
