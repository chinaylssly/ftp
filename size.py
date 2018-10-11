# coding: utf-8

import os
import logging
from command import Command


# if __name__=='__main__':

#     logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
#                     # filename=u'e:/psftp/voice/voice.log',
#                     # filemode='w'
#                     ) 

class Size(object):

    @classmethod
    def get_local_size(self,local_path=u'sftp.py'):

        size=os.path.getsize(local_path)
   
        putty_size=self.putty_size(size)

        log=u'get %s size=%s'%(local_path,putty_size)
        print log
        logging.info(log)

        return size

    @classmethod
    def get_server_size(self,command,server_path):

        query='ls -l "%s"'%server_path
        out=command.execute(query=query)
        line=out[0].strip()

        size=line.split(' ')[4]
        size=int(size)
        putty_size=self.putty_size(size)

        log=u'get %s size=%s'%(server_path,putty_size)
        print log
        logging.info(log)

        return size

    @classmethod
    def putty_size(self,size=1233333):

        ksize=size*1.0/1024
        if ksize<1024:

            if ksize<1:
                extend='B'
                size=size

            else:
                extend='K'
                size=ksize

        else:

            msize=ksize/1024
            extend='M'
            size=msize

            if msize>=1024:

                gsize=msize/1024
                extend='G'
                size=gsize

        return u'%.2f%s'%(size,extend)

    @classmethod
    def compare_size(self,server_size,local_size):

        diff_size=abs(server_size - local_size)

        return diff_size




def test():

    Size.get_local_size()
    size=Size()
    # size.get_local_size()
    command=Command()
    server_path=u'/python/aastory/story/玄幻/武修道统/第6回 破阵破敌.txt'
    out=size.get_server_size(command=command,server_path=server_path)


def test_putty():

    sizes=[500,1024,1600,1048576,1300000,1111111111,11111111111111]

    for size in sizes:

        print Size.putty_size(size)

if __name__=='__main__':

    # test_putty()
    test()
    



    