#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File : excuteCmd.py
# @Author :hannoch
import os
import json
import subprocess,signal
from threading import Timer


class excuteCmd(object):
    def __init__(self,cmd,timeout2):
        self.stdout = []
        self.stderr = []
        self.timeout = timeout2
        self.is_timeout = False
        self.cmd = cmd
        

    #同时将timeout_callback函数改成如下就可以了：
    def timeout_callback(self, p):
        self.is_timeout = True
        print('exe time out call back')
        print(p.pid)
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except Exception as e:
            print(e)

    def run(self):
        p = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid,shell=True)
        my_timer = Timer(self.timeout, self.timeout_callback, [p])
        my_timer.start()
        try:
            #print ("start to count timeout; timeout set to be %d \n" % (self.timeout,))
            for line in iter(p.stdout.readline, b''):
                print(line)
                if self.is_timeout:
                    break
            for line in iter(p.stderr.readline, b''):
                print(line)
                if self.is_timeout:
                    break
        finally:
            my_timer.cancel()
            p.stdout.close()
            p.stderr.close()
            p.kill()
            p.wait()
	        
# if __name__ == '__main__':
#     cmd = "python PortScan.py --ip 192.168.52.1 --port 20-65535 -t 100"
#     obj = excuteCmd(cmd,timeout=60)
#     obj.run()
