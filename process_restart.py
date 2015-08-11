#! /usr/bin/env python
import sys
import os
import signal
import logging
import psutil
import subprocess
import shlex


"""
   pid_control.py A Python tool to control processes in Unix like systems by PID.
   Aug, 2015 Steven D Irvin 

   WARNING: You need to install psutil on the system and run this as $ sudo python pid_control.py
"""


def processes_restart(pids):
    """
        control processes in unix like systems by PID
    """
    for process_id in pids:
        try:
            if not 'api' in process_id:
                command_line = 'sudo /usr/bin/python ' + process_id +
                               ' --config-file /etc/ceilometer/ceilometer.conf'
            else:
                command_line = 'sudo /usr/bin/python ' + process_id +
                            ' -d -v --log-dir=/var/log/ceilometer-api' +
                            ' --config-file /etc/ceilometer/ceilometer.conf'
            args = shlex.split(command_line)
            print(args)
            p = psutil.Process(int(process_id))
            p = subprocess.Popen(args) # Success!
            logger.info('Restart process PID {0}'.format(process_id))
        except OSError:
            logger.error('ERROR: Could not kill PID {0}'.format(process_id))

def retrieve_processes():
    """
        retrieve PIDs for processes on Unix like systems.
    """
    with open ("ceilometer.processes", 'rt') as pid_file:
        pid_list = []
        for process_id in pid_file.read().splitlines():
            pid_list.append(process_id)
    print('Found PID list {0}'.format(', '.join(pid_list)))
    return pid_list

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    logger = logging.getLogger('pid_control')
    processes_restart(retrieve_processes())