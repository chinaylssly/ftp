# coding: utf-8


from command import Command
from sftp import Sftp
from size import Size



def test_ftp_put():

    local_path=u'c:/users/sunzhiming/desktop/books.html'
    server_floder=u'/python'
   
    size=Size().get_local_size(local_path)

    ftp=Sftp()
    ftp.put(local_path=local_path,server_floder=server_floder,filesize=size)

    ftp.close_ftp()



test_ftp_put()



def test_ftp_get():

    server_path=u'/python/books.html'
    
    command=Command()
    ftp=Sftp()
    size=Size().get_server_size(command=command,server_path=server_path)
    ftp.get(server_path=server_path,filesize=size)

    ftp.close_ftp()


test_ftp_get()







def test_get_server_size():

    command=Command()
    server_path=u'/python/voice/1/1.mp3'
    size=Size().get_server_size(command=command,server_path=server_path)
    command.close_ssh()


