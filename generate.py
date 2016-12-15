import os

template=open("template.html","r")
output=open("index.html","w")
data_path='dataset/'

files = os.listdir(data_path)
files.sort()

ins=""
for path in files:
	f=open(os.path.join(data_path+path))
	val=[]
	for line in f:
		splited=line[:-1].split(',')
		val.append(str(int(splited[0])/100000.0)+','+(str(int(splited[1])/100000.0)))
	ins=ins+'path["'+path+'"]="'+':'.join(val)+'";\n'

output.write(template.read().replace("//insert",ins))
template.close()
output.close()

