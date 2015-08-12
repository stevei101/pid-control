#!/bin/bash
ps -ef | grep '/usr/local/bin/ceilometer' | grep -v grep | awk '{print $2 > "ceilometer.pid"}'
ps -ef | grep '/usr/local/bin/ceilometer' | grep -v grep | awk '{$1=$2=$3=$4=$5=$6=$7=""; print $0 > "ceilometer.processes"}'