#!/usr/bin/env python
# coding: utf-8
import paramiko 
from config import host,user,password
import logging
from traceback import format_exc

class Command(object):

    def __init__(self,):

        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(host, 22, user, password)

    def execute(self,query='ls /python'):

        log=u'execute command : "%s"'%query
        print log
        logging.info(log)

        try:
            std_in, std_out, std_err = self.ssh_client.exec_command(query)

            out=std_out.readlines()
            err=std_err.readlines()

            std_out.close()
            std_err.close()


            log=u'std_out=%s,\nstd_err=%s'%(out,err)
            print log
            logging.info(log)

            return out
            ##std_out为可迭代对象,std_out，相当于文件

        except:

            print format_exc()
            logging.info(format_exc())

    def close_ssh(self,):

        self.ssh_client.close()

        log=u'successfully close ssh_client connect'
        print log
        logging.info(log)



def test():

    command=Command()
    command.execute()
    command.close_ssh()


if __name__ =='__main__':

    test()