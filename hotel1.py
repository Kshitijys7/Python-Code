#rice=[{"Jira Rice":100},{"Veg Biryani":200},{"Plane Rice":300}]
#paneer=[{"Paneer Tikka":100},{"Paneer Mutter":200},{"Alu Paneer":300}]
#rice1=[{"Chicken Biryani":200},{"Anda Rice":100},{"abc":300}]
#dfr=[{"qwe":100},{"pqr":100},{"stu":300}]

menu={
        "veg":
            {
                "rice":{"Jira Rice":100,"Veg Biryani":200,"Plane Rice":300},
                "paneer":{"Paneer tikka":100,"Paneer Mutter":200,"Alu Paneer":300}
            },
        "non-veg":{
                "rice1":{"Chicken Biryani":200,"Anda Rice":100,"Shezwan Rice":300},
                "dfr":{"qwe":100,"pqr":100,"stu":300}
        }
}
list=[]
list1=[]
list.append(menu)
num=[1,2,3]
total=0
while 'true':
    for i in menu:
        print(i,"\t",menu[i].items())
    ch=int(input("Enter choice"))
    if ch==1:
        print(list[0].get("veg"))
        c=int(input("Enter veg choice"))
        if c==1:
            print(list[0].get("veg").get("rice"))
            ch1=int(input("Enter rice choice"))
            if ch1==1:
                list1.append(list[0].get("veg").get("rice").get("Jira Rice"))
            elif ch1==2:
                list1.append(list[0].get("veg").get("rice").get("Veg Biryani"))
            elif ch1==3:
                list1.append(list[0].get("veg").get("rice").get("Plane Rice"))
        elif c==2:
            print(list[0].get("veg").get("paneer"))
            ch1 = int(input("Enter panner choice"))
            if ch1 == 1:
                list1.append(list[0].get("veg").get("paneer").get("Paneer tikka"))
            elif ch1 == 2:
                list1.append(list[0].get("veg").get("paneer").get("Paneer Mutter"))
            elif ch1 == 3:
                list1.append(list[0].get("veg").get("paneer").get("Alu Paneer"))
    if ch==2:
        print(list[0].get("non-veg"))
        c = int(input("Enter non-veg choice"))
        if c == 1:
            print(list[0].get("non-veg").get("rice1"))
            ch1 = int(input("Enter non-veg rice choice"))
            if ch1 == 1:
                list1.append(list[0].get("non-veg").get("rice1").get("Chicken Biryani"))
            elif ch1 == 2:
                list1.append(list[0].get("non-veg").get("rice1").get("Anda Rice"))
            elif ch1 == 3:
                list1.append(list[0].get("non-veg").get("rice1").get("Shezwan Rice"))
        elif c == 2:
            print(list[0].get("non-veg").get("dfr"))
            ch1 = int(input("Enter dfr choice"))
            if ch1 == 1:
                list1.append(list[0].get("non-veg").get("dfr").get("qwe"))
            elif ch1 == 2:
                list1.append(list[0].get("non-veg").get("dfr").get("pqr"))
            elif ch1 == 3:
                list1.append(list[0].get("non-veg").get("dfr").get("stu"))
    f = int(input("Continue"))
    if f != 1:
        break
j=len(list1)
for i in range(j):
    total=total+list1[i]
print("Total price is",total)






