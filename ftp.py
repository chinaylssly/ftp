# coding: utf-8


from command import Command
from sftp import Sftp
from size import Size

class FTP(Sftp,Command):


    def __init__(self,):

        Sftp.__init__(self)
        Command.__init__(self)

        self.size=Size()


    def get_server_size(self,server_path=u'/python/voice/1/1.mp3'):
        ##获取服务器上文件大小
        
        filesize=self.size.get_server_size(command=self,server_path=server_path)
        return filesize

    def ftp_get(self,server_path=u'/python/books.html',local_floder=u''):
        ##下载服务器文件到本地

        filesize=self.get_server_size(server_path=server_path)
        self.get(server_path=server_path,local_floder=local_floder,filesize=filesize)


    def ftp_put(self,local_path=u'c:/users/sunzhiming/desktop/books.html',server_floder=u'/python'):
        #上传文件到服务器

        filesize=self.size.get_local_size(local_path)
        self.put(local_path=local_path,server_floder=server_floder,filesize=filesize)





def test():

    ftp=FTP()
    ftp.ftp_get(local_floder='data')
    ftp.ftp_put()

    query='ls /python'
    ftp.execute(query)
    


if __name__=='__main__':

    test()
