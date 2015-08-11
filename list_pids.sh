#!/bin/bash
ps -ef | grep '/usr/local/bin/ceilometer' | grep -v grep | awk '{print $2 > "ceilometer.pid"}'
ps -ef | grep '/usr/local/bin/ceilometer' | grep -v grep | awk '{print $9 > "ceilometer.processes"}'