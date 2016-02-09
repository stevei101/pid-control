#!/bin/bash
ps auwx | grep cassandra| grep -v grep | awk '{print $2 > "cassandra.pid"}'
