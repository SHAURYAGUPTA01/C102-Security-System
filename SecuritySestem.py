import dropbox
import cv2
import random
import time

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    cvobj=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=cvobj.read()
        img_name= "profile"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result=False
    return img_name
    print("Snapshot Taken")
    cvobj.release()
    cv2.destroyAllWindows()
    
def upload_file(img_name):
    access_token = "sl.BGR6bUqc1q-p683g_JB5MQ__HLbkd8CORkMsxeWMJqERz9BczoGAJ0KeeRXl-C7jTVOC0j4RErAmE5ZdXvco0XcvmjiY37WskaH36ABSTY42W_3KSg2AA-GpvOj9h3QsnEijT8QjSTA"
    file=img_name
    fileFrom=file
    fileTo="/SecuritySystem/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(fileFrom,"rb") as f:
        print('test')
         # to resolve the path errors last parameter is added
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if( (time.time() - start_time  ) >=5):
            name=take_snapshot()
            upload_file(name)
    
main()