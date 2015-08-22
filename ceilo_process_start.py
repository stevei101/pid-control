#! /usr/bin/env python
import sys
import os
import signal
import logging
import psutil
import subprocess
import shlex


"""
   process_list_restart.py A Python tool to control processes in Unix like systems by PID.
   Aug, 2015 Steven D Irvin 

   WARNING: You need to install psutil on the system and run this as $ sudo python pid_control.py
"""


def process_list_restart(pids):
    """
        control processes in unix like systems by PID
    """
    for process_id in pids:
        try:
            args = shlex.split(process_id)
            logger.info(args)
            p = subprocess.Popen(args) # Success!
            logger.info('Restart process {0}'.format(process_id))
        except OSError:
            logger.error('ERROR: Could not restart {0}'.format(process_id))

def retrieve_processes():
    """
        retrieve PIDs for processes on Unix like systems.
    """
    with open ("ceilo.processes", 'rt') as pid_file:
        pid_list = []
        for process_id in pid_file.read().splitlines():
            pid_list.append(process_id)
    logger.info('Found PID list {0}'.format(', '.join(pid_list)))
    return pid_list

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    logger = logging.getLogger('pid_control')
    process_list_restart(retrieve_processes())