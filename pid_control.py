#! /usr/bin/env python
import sys
import os
import signal
import logging
import psutil


"""
   pid_control.py A Python tool to control processes in Unix like systems by PID.
   Aug, 2015 Steven D Irvin 
"""


def pid_control(pids):
    """
        control processes in unix like systems by PID
    """
    for process_id in pids:
        try:
            p = psutil.Process(int(process_id))
            p.terminate()  #or p.kill()
            logger.info('Stopped process PID {0}'.format(process_id))
        except OSError:
            logger.error('ERROR: Could not kill PID {0}'.format(process_id))

def get_pids():
    """
        get PIDs for processes on Unix like systems.
    """
    try:
        pids = os.system('./list_pids.sh')
    except OSError:
        logger.error('ERROR: Could not get list of PIDs.')
    with open ("ceilometer.pid", 'rt') as pid_file:
        pid_list = []
        for process_id in pid_file.read().splitlines():
            pid_list.append(process_id)
    print('Found PID list {0}'.format(', '.join(pid_list)))
    return pid_list


if __name__ == "__main__":

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    logger = logging.getLogger('pid_control')
    pid_control(get_pids())