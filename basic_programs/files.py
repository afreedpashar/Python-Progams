#copying data of one file to  another
# with open('text.txt','r') as rf:
#     with open('test1.txt','w') as wf:
#         for line in rf:
#             wf.write(line)    

#to copy a image

with open('laser.jpg','rb') as rf:
    with open('laser.copy.jpg','wb') as wf:
        for pic in rf:
            wf.write(pic)