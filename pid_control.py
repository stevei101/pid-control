#! /usr/bin/env python
import sys
import os
import signal
import logging

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
            p = psutil.Process(process_id)
            p.terminate()  #or p.kill()
            logger.info('Stopped process PID {0}'.format(process_id))
        except OSError:
            logger.error('ERROR: Could not kill PID {0}'.format(process_id))

def get_pids():
    """
        get PIDs for processes on Unix like systems.
    """
    try:
        pids = os.system(ps -ef | grep '/usr/bin/ceilometer' | grep -v grep | awk '{print $2 > "ceilometer.pid"}')
    except OSError:
        logger.error('ERROR: Could not get list of PIDs.')
    with open ("ceilometer.pid", 'rt') as pid_file:
        pid_list = []
        for processs_id in pid_list.split_lines()
            pid_list.append(process_id)
    return pid_list


if __name__ == "__main__":

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    logger = logging.getLogger('pid_control')
    pid_control(get_pids())