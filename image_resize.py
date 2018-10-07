from PIL import Image

basewidth=[480,1000]
file_name="test2"
#img.save('%s_%s.jpg' %(file_name,int(img.width)))
for i in range (len(basewidth)):
	img = Image.open('%s.jpg' %file_name)
	wpercent = (basewidth[i]/float(img.width))
	hsize = int((float(img.height)*float(wpercent)))
	img = img.resize((basewidth[i],hsize), Image.LANCZOS)
	img.save('%s_%s.jpg' %(file_name,basewidth[i]),'jpeg',icc_profile=img.info.get('icc_profile'))

img.close()