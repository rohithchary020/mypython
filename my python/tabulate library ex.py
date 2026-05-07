# tabulate library

from tabulate import tabulate
title=["Name","Age","Department"]
data=[["Rohith",21,"CSM"],
      ["Anand",24,"CSM"],
      ["Shiva",34,"Civil"],
      ["Arun",60,"Mech"]]
res=tabulate(data,headers=title,tablefmt="github")
print(res)
