# coding: utf-8

import os
import logging


class Size(object):

    @classmethod
    def get_local_size(self,path=u'sftp.py'):

        size=os.path.getsize(path)

        size=size*1.0/1024
        if size<1024:
            extend='K'
            if size<1:
                size=1
            else:
                size=int(size)   

        else:

            size=size/1024
            extend='M'

            if size<1:
                size=1
            else:
                size=int(size)

        size=u'%s%s'%(size,extend)
        log=u'get %s size=%s'%(path,size)
        print log
        logging.info(log)

        return size

        
    def get_server_size(self,command,server_path):
        ##获取服务器上文件大小

        query='du -h %s'%server_path
        out=command.execute(query=query)
        size=out[0].split('\t')[0]

        log=u'get %s size=%s'%(server_path,size)
        print log
        logging.info(log)

        return size

if __name__=='__main__':

    Size.get_local_size()
    size=Size()
    size.get_local_size()



    