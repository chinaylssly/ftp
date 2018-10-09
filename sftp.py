# coding: utf-8
import paramiko 
from config import host,user,password
import logging
from traceback import format_exc
from time import time
import os

class Sftp(object):

    ##path建议使用绝对路径

    def __init__(self,):

        self.t = paramiko.Transport((host, 22))
        self.t.connect(username=user, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.t)


    def get(self,server_path, local_floder='',filesize=0):

        ##get方法，未指定local_floder，默认保存在当前路径下



        filename=server_path.rsplit('/',1)[-1]

        if local_floder:

            if not os.path.exists(local_floder):
                ##创建下载目录
                os.makedirs(local_floder)
                log=u'create local_floder=%s'%local_floder
                logging.info(log)

            local_path=u'%s/%s'%(local_floder,filename)

        else:
            local_path=filename

         

        if os.path.exists(local_path):
            ##判断本地文件是否存在，存在则不下载，否则会覆盖本地文件

            log=u'local_path= %s exist'%local_path
            print log
            logging.info(log)

        else:

            try:

                log=u'from %s download %s,filesize=%s'%(server_path,local_path,filesize)
                print log
                logging.info(log)

                t1=time()

                self.sftp.get(server_path, local_path)

                t2=time()

                t=max(int(t2-t1),1)

                log=u'successfully download %s to %s,cost time=%s second'%(server_path,local_path,t)
                print log
                logging.info(log)

            except:

                print format_exc()
                logging.info(format_exc())



    def put(self,local_path,server_floder='/root',filesize=0):

        filename=local_path.rsplit('/',1)[-1]

        if not os.path.exists(server_floder):
            ##创建上传目录
            os.makedirs(server_floder)
            log=u'create server_floder=%s'%server_floder
            logging.info(log)

        server_path=u'%s/%s'%(server_floder,filename)
        ##put方法，默认保存路径在server的/root路径下


        try:

            log=u'put %s to %s,filesize=%s'%(local_path,server_path,filesize)
            print log
            logging.info(log)

            t1=time()

            self.sftp.put(local_path,server_path)

            t2=time()

            t=max(int(t2-t1),1)

            log=u'successfully put %s to %s,cost time=%s second'%(local_path,server_path,t)
            print log
            logging.info(log)

        except:

            print format_exc()
            logging.info(format_exc())



    def close_ftp(self,):


        self.t.close()
        log=u'successfully close ftp connect'
        print log
        logging.info(log)

