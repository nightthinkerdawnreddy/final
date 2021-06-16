import pafy
import os
url = "https://www.youtube.com/watch?v=VImfmwHaP3E"
video = pafy.new(url)
audiostream=video.audiostreams
for i in audiostream:
    print('bitrate : %s,ext:%s,size:%0.2fmb'%(i.bitrate,i.extension,i.get_filesize()/1024/1024))
print(os.getcwd())
audiostream[1].download(filepath =  os.getcwd())
os.system('mv {}/*.webm {}/working.webm'.format(os.getcwd(),os.getcwd()))
import speech_recognition as sr
