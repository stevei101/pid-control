#!/bin/bash
ps -ef | grep 'ceilometer-a' | grep -v grep | grep -v 'ceilometer-alarm' | awk '{print $2 > "ceilo.pid"}'
ps -ef | grep 'ceilometer-a' | grep -v grep | grep -v 'ceilometer-alarm' | awk '{$1=$2=$3=$4=$5=$6=$7=""; print $0 > "ceilo.processes"}'