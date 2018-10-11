#!/usr/bin/env python
# coding: utf-8
import paramiko   
from traceback import format_exc
import logging

  
import paramiko

def sftp_exec_command(command):

    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, 22, user, password)
        std_in, std_out, std_err = ssh_client.exec_command(command)
        for line in std_out:
            print line.strip("\n")
        ssh_client.close()
    except Exception, e:
        print e


def sftp_down_file(server_path, local_path):
    try:
        t = paramiko.Transport((host, 22))
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(server_path, local_path)
        t.close()
    except Exception, e:
        print e


def sftp_upload_file(server_path, local_path):
    try:
        t = paramiko.Transport((host, 22))
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_path, server_path)
        t.close()
    except Exception, e:
        print e


def test_exec():

    querylist=[]

    # query='ps -el'
    # querylist.append(query)

    query='ls -F /python/voice| grep /$'  
    querylist.append(query)

    for query in querylist:

        sftp_exec_command(query)


if __name__ == '__main__':

    test_exec()
