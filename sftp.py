# coding: utf-8
import paramiko 
from config import host,user,password
import logging
from traceback import format_exc
from time import time
import os
from size import Size

if __name__=='__main__':

    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    # filename=u'e:/psftp/voice/voice.log',
                    # filemode='w'
                    ) 


class Sftp(object):

    ##path建议使用绝对路径

    def __init__(self,):

        self.t = paramiko.Transport((host, 22))
        self.t.connect(username=user, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.t)


    def sftp_get(self,server_path, local_floder='',filesize='1K'):

        ##get方法，未指定local_floder，默认保存在当前路径下

        filename=server_path.rsplit('/',1)[-1]

        if local_floder:
            local_path=u'%s/%s'%(local_floder,filename)
        else:
            local_path=filename

        if os.path.exists(local_path):

            local_size=Size.get_local_size(local_path)
            server_size=filesize
            diff_size=server_size - local_size

            putty_diff_size=Size.putty_size(size=diff_size)

            log=u'size of server_path= %s - size of local_path= %s is :%s'%(server_path,local_path,putty_diff_size)
            logging.info(log)
            print log

            if diff_size<0:
                ##本地文件大于服务器文件，说明不是同一个文件,暂不做处理
                flag=None
                pass


            elif diff_size < 1024:
                ##说明两个文件差异不大，可以认为文件以及下载完成
                flag=False

            else:
                ##两个文件差异1024B,认为文件未下载完毕
                log=u'local_path= %s exist'%local_path
                print log
                logging.info(log)
                flag=True




        else:
        #文件不存在，文件尚未下载

            flag=True


        if flag:

            ##flag 用于标识是否开启下载

            try:

                putty_server_size=Size.putty_size(server_size)

                log=u'from %s download %s,filesize=%s'%(server_path,local_path,putty_server_size)
                print log
                logging.info(log)

                t1=time()
                self.sftp.get(server_path, local_path)
                t2=time()
                t=t2-t1

                log=u'successfully download %s to %s,cost time=%.2f second'%(server_path,local_path,t)
                print log
                logging.info(log)

            except:

                log=format_exc()
                logging.info(log)
                print log



    def sftp_put(self,local_path,server_floder='/root',filesize=0):

        filename=local_path.rsplit('/',1)[-1]
        server_path=u'%s/%s'%(server_floder,filename)
        ##put方法，默认保存路径在server的/root路径下


        try:

            log=u'put %s to %s,filesize=%s'%(local_path,server_path,filesize)
            print log
            logging.info(log)

            t1=time()

            self.sftp.put(local_path,server_path)

            t2=time()

            t=t2-t1

            log=u'successfully put %s to %s,cost time=%.2f second'%(local_path,server_path,t)
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

