import os

os.chdir(r'C:\Users\student\jinho\SSAFY지원자')

for filename in os.listdir("."):         
    end_name = filename.replace("SAMSUNG_","SSAFY")
    os.rename(filename,end_name)