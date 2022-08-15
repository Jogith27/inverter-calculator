def view():
	if(len(l)==0):
		print("no item available")
	else:
		for i in range(len(l)):
			print(i+1,")",end="",sep="")
			print(l[i][0],"of",l[i][1],"with",l[i][2],"watts")
	print("------------------------------------------------------------------------------")	
def delete(l,delitem):
	del l[delitem-1]
	print("del success")
	view()
def update():
	a=input("enter the name: ").strip()
	flag=False
	for i in range(len(l)):
		if a in l[i]:
			chan=int(input("enter 1 to change in numbers \nenter 2 change in watts\n"))
			if(chan==1):
				tem=l[i][1]
				l[i][1]=int(input("enter the numbers: "))
			elif(chan==2):
				tem=l[i][2]
				l[i][2]=int(input("enter the watts: "))
			flag=True
			break
	if(flag):
		print("success")
		loadcal()
	else:
		print("failed")
def additem(load,item):
	for i in range(item):
		obj,nos,watt=list(map(str,input().split()))
		#load=load+int(nos)*int(watt)
		#print(load)
		l.append([obj,int(nos),int(watt)])
	
def loadcal():
	load=0
	for i in range(len(l)):
		load=load+int(l[i][1])*int(l[i][2])
	return load
def battery(bat):
	if(len(l)==0):
		print("add items")
		return
	load=loadcal()
	con=0
	for i in range(len(bat)):
		if(bat[i]>=load):
			con=i
			break
	vol=12
	current=load/12
	print("choose your battery capacity from below")
	for i in range(con,len(bat)):
		print(bat[i])
	ah=int(input("enter: "))
	if(ah in bat[con:]):
		batterybackuptime=round((ah/current)*0.7,2)
		temp=str(batterybackuptime).split(".")
		mins=int(temp[1])
		dum=ah
		if(mins*6>60):
			lk=mins%60
			extra=(mins-lk)//60
			temp[0]=int(temp[0])+extra
			mins=lk
		print(int(temp[0]),"hours",mins*6,"mins backup for",ah,"AH battery",)
		a=(dum*0.1)+1
		t2=dum*0.4
		t=(ah+t2)/a
		print("charging time",round(t),"hrs","\n----------------------------------------------------------------------")
		return [load,ah,int(temp[0]),mins*6,int(t)]
	else:
		print("invalid input")

print("                         Welcome to inventor calculator\n\n")
bat=[20,40,75,100,120,150,200]
l=[];load=0 #["bulb",2,15],["tube",2,35]
while(True):
	print("1)Enter 1 to add items \n2)Enter 2 to update the item\n3)enter 3 to delete\n4)enter 4 to view \n5)enter 5 to calculate battery\nenter 0 to exit")
	k=int(input())
	match k:
		case 1:
			item=int(input("enter the no of items: "))
			load=additem(load,item)
		
		case 4:
			view()
		case 2 :
			update()
			load=loadcal()
		case 3:
			view()
			delitem=int(input("enter the item number to delete: "))
			if(delitem-1<len(l)):
				delete(l,delitem)
		case 5:
			batchoose=battery(bat)
		case 6:
			l.clear()
		case 0:
			break
print("battery for load",batchoose[0],"is",batchoose[1],"according to your choice has backup time of ",batchoose[2],"hours and",batchoose[3],"minutes which takes",batchoose[4],"hrs to recharge")
