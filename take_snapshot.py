import dropbox
import cv2
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True

    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+ str(number)+ ".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
        
    return img_name
    print("Snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.AvdCn99qe8Y2bRrxbrBnv9QsWyX1K8IgBezkJ4L-ITVUi_7CQqmR7kvLZeNS9CsjW7G-nAYv5XvZC8nr6JVn4HiHnYIkO-9M_ZElubf0wWeg6-Akw4-iI0_xpUO9Zpe99hwnJwY"
    file=img_name
    file_from=file
    file_to="/NewFolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)




main()
    

