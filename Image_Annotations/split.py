# -*- coding:utf-8 -*
import os
import random

import os
import shutil


def data_split(full_list, ratio):
    """
    Dataset splitting: Divide the list full_list into 2 sub-lists in proportion (sublist_1 and sublist_2 )
    :param full_list: dataset list
    :param ratio:     child list1
    """
    n_total = len(full_list)
    offset = int(n_total * ratio)
    if n_total == 0 or offset < 1:
        return [], full_list

    random.shuffle(full_list)
    sublist_1 = full_list[:offset]
    sublist_2 = full_list[offset:]
    return sublist_1, sublist_2


train_p="./train"
val_p="./val"
imgs_p="images"
labels_p="labels"


if not os.path.exists(train_p):
    os.mkdir(train_p)
tp1=os.path.join(train_p,imgs_p)
tp2=os.path.join(train_p,labels_p)
print(tp1,tp2)
if not os.path.exists(tp1):
    os.mkdir(tp1)
if not os.path.exists(tp2):  
    os.mkdir(tp2)

if not os.path.exists(val_p):
    os.mkdir(val_p)
vp1=os.path.join(val_p,imgs_p)
vp2=os.path.join(val_p,labels_p)
print(vp1,vp2)
if not os.path.exists(vp1):
    os.mkdir(vp1)
if not os.path.exists(vp2):
    os.mkdir(vp2)

# dataset path
path1="./images"
path2="./labels"

proportion_ = 0.9 # train ratio

total_file = os.listdir(path1)

num = len(total_file)  # count all labels
list_=[]
for i in range(0,num):
    list_.append(i)

list1,list2=data_split(list_,proportion_)

for i in range(0,num):
    file=total_file[i]
    print(i,' - ',total_file[i])
    name=file.split('.')[0]
    if i in list1:
        jpg_1 = os.path.join(path1, file)
        jpg_2 = os.path.join(train_p, imgs_p, file)
        txt_1 = os.path.join(path2, name + '.txt')
        txt_2 = os.path.join(train_p, labels_p, name + '.txt')
        shutil.copyfile(jpg_1, jpg_2)
        shutil.copyfile(txt_1, txt_2)

    elif i in list2:
        jpg_1 = os.path.join(path1, file)
        jpg_2 = os.path.join(val_p, imgs_p, file)
        txt_1 = os.path.join(path2, name + '.txt')
        txt_2 = os.path.join(val_p, labels_p, name + '.txt')
        shutil.copyfile(jpg_1, jpg_2)
        shutil.copyfile(txt_1, txt_2)

print("Dataset split complete: total: ",num," train: ",len(list1)," val: ",len(list2))

