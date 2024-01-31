test_dict = {'afreed':[20,30,40],'tanveer':[30,40,50],'rahman':[90,80,70]}
res = []
for key,val in test_dict.items():
    res.append([key]+val)
print(str(res))

# or

#using list comprehension

res = [[key]+val for key,val in test_dict.items()]
print(res)


#let p1 = new Promise((resolve,reject)=>{
# setTimeOut(()=>{
# },1000);
# });

#let p2 = new Promise((resolve,reject)={
      #setTimeOut(()=>{
      # },2000)
# })

#let p3 = Promise((resolve,rejecr)=>{
#setTimeOut(()=>{
# },3000)
# })


