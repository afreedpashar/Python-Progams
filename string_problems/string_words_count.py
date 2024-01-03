mystr = " a,a,a,b,b,b,c,c"
mylist = mystr.split(",")
visited_list=[]
final_list=[]

for ch in mylist:
    if ch not in visited_list:
        final_list.append(f"{ch}:{mylist.count(ch)}")
        visited_list.append(ch)
print(",".join(final_list))
