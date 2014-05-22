#!/bin/bash
ps -fe|grep 'log2mq.py' |grep -v grep
if [ $? -ne 0 ]
then
   `nohup /publish/env/bin/python /publish/flume-ansible/sbin/log2mq.py 2>&1 &`	
else
echo "runing....."
fi
