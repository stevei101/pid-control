#! /usr/bin/env python
import sys
import os
import signal
import logging
import psutil


"""
   pid_control.py A Python tool to control processes in Unix like systems by PID.
   Aug, 2015 Steven D Irvin 

   WARNING: You need to install psutil on the system and run this as $ sudo python pid_control.py
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

def pid_control_restart(pids):
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
        get PIDs for processes on Unix like systems and output them to a file.
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

def retrieve_pids():
    """
        retrieve PIDs for processes on Unix like systems.
    """
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
    if sys.argv[1] is None:
        pid_control(get_pids())
    else:
        pid_control_restart(retrieve_pids())