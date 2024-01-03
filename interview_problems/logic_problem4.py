query = 'a=2&b=23&name=prakash'
query.split('&')
new_li=[]
for ele in query.split('&'):
    new_li.append(ele.split('='))
print(new_li)