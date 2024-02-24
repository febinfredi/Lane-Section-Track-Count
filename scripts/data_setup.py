import sys
import os
import zipfile
import random

train_im_path = "/yolov8/data/images/train"
train_lbl_path = "/yolov8/data/labels/train"
val_im_path = "/yolov8/data/images/val"
val_lbl_path = "/yolov8/data/labels/val"

src_path = os.path.dirname(os.getcwd()) + "/yolov8/datasets/"    # folder with zip files
tgt_im = os.path.dirname(os.getcwd()) + train_im_path    # folder to save the extracted file images
tgt_lbl = os.path.dirname(os.getcwd()) + train_lbl_path   # folder to save the extracted file labels

train_split = 0.80;

cntr = 0

def uid(id_str):
    """
    id_str: <str> string to be usd for id
    """
    # print(id_str)
    uniqueid = id_str.split(".")[0]
    return uniqueid

def zipextract(zip_file, src_folder, dest_folder_path, train_split, dest_folder_img, dest_folder_lbl):
    
    print('reading zip: {}'.format(zip_file))
    myzip = zipfile.ZipFile(os.path.join(src_folder, zip_file),'r')    # open zip file object
    for zf_file_name in sorted(myzip.namelist()):    # iterate through each file name   
        if zf_file_name[3]=="_":    # make sure file isn't ".data" or ".names" or "train.txt" file
            filename = os.path.basename(zf_file_name) 
            extension = os.path.splitext(filename)[1]
            
            # if extension is .PNG, send it to images folder else to labels folder
            if random.random() < (1-train_split):
                if extension==".PNG":
                    destination = os.path.abspath(dest_folder_path + val_im_path)
                if extension==".txt":
                    destination = os.path.abspath(dest_folder_path + val_lbl_path)
            else:
                if extension==".PNG":
                    destination = os.path.abspath(dest_folder_path + train_im_path)
                if extension==".txt":
                    destination = os.path.abspath(dest_folder_path + train_lbl_path)        
            # if extension==".PNG":
            #      destination = os.path.abspath(dest_folder_img)
            # if extension==".txt":
            #      destination = os.path.abspath(dest_folder_lbl)     
            print("file name: " + filename)
            print("uid: " + uid(id_str=zip_file))
            print("destination: " + destination)
            print("extension: " + extension)

            # add id to each file name
            extract_to = destination + '/' + uid(id_str=zip_file) + "_" + filename.split(".")[0]
            if extension:   
                extract_to = extract_to + extension
                print("file extract path: " + extract_to + "\n")    

            if not filename:
                continue

            print("extracting: '{}' to '{}'".format(filename, extract_to))
            data = myzip.read(zf_file_name)
            output = open(extract_to, 'wb') # exporting to given location one by one
            output.write(data)
            output.close()
            #data.close()
    myzip.close()

for f in os.listdir(src_path):
        if f.endswith(".zip"):
            # print(f)
            zipextract(zip_file=f, src_folder=src_path, dest_folder_path=os.path.dirname(os.getcwd()), train_split=train_split, dest_folder_img=tgt_im, dest_folder_lbl=tgt_lbl)

# execute only if run as a script
# if __name__ == "__main__":
#     # get command line arguments (0 is the command called, e.g. your script)  
#     zip_file = sys.argv[1]
#     to_folder = sys.argv[2]

#     dir_name = 'C:\\Users\\Efste\\Desktop\\Test'
#     os.chdir(dir_name) # change directory from working dir to specified
#     for f in os.listdir(dir_name):
#         if f.endswith(".zip"):
#             zipextract(f, to_folder)

