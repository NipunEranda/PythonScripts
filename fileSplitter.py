import os
import glob

#get list of files
arr = os.listdir('/home/neo/Workplace/WhatsApp/Media/WhatsApp_Stickers')

#Creating directories
path = os.getcwd()
try:
    for x in range(1, (int(len(arr)/30)+2)):
        os.mkdir(path + "/sticker_pack/FmwhatsappStickers" + str(x))
except OSError:
    print ("Creation of the directory %s failed" % path + "/sticker_pack")
else:
    print ("Successfully created the directory %s " % path + "/sticker_pack")


forpath = path + "/sticker_pack/FmwhatsappStickers"
folderCount = 1
count = 1
for i in arr:
    os.system('cp /home/neo/Workplace/WhatsApp/Media/WhatsApp_Stickers/' + str(i) + ' ' + forpath + str(folderCount))  
    count = count + 1
    if(count == 31):
        folderCount = folderCount + 1
        count = 1