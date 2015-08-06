#!/bin/bash
ps -ef | grep '/usr/bin/ceilometer' | grep -v grep | awk '{print $2 > "ceilometer.pid"}'