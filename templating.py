# import the required libs
import glob
import os
import shutil
from PIL import Image
import random
import yaml
import pathlib2

#Define relative data directory
data_dir="../website_data"
output_dir="../website_push"

# load the file path names in the directory
f = []
for (dirpath, dirnames, filenames) in os.walk(data_dir):
	# filter hiden folders out of the list
	dirnames[:] = [d for d in dirnames if not d[0] == '.']
	break

print(dirnames)

# make a card tag in the respective html file for each of the sub folders in that file
for i in range(len(dirnames)):
	print(dirnames[i])
	# get all the subfolders in each main folder
	temp=[]
	for (dirpath_temp, album_dir, filenames_temp) in os.walk("%s/%s" %(data_dir,dirnames[i])):
		temp.extend(filenames_temp)
		break
	# print(filenames_temp)

	# init the card_tag variable
	card_tag=str("")
	for j in range(len(album_dir)):
		print("--%s" %album_dir[j])
		# make the image list from the current directory for resizing
		# img_list=glob.glob("%s/%s/%s/*.jpg" %(data_dir,dirnames[i],album_dir[j]))

		# open the album info yaml file and read into a stream
		with open('%s/%s/%s/info.yaml' %(data_dir,dirnames[i],album_dir[j]),'r') as stream:
			info=yaml.load(stream)
		cover_path=str("%s/%s/%s" %(dirnames[i],album_dir[j],info['cover']))
		# append a tag for each subfolders
		card_tag+=str('<div class="album">\n<div class="photo">\n<a href="%s/%s.html"><img class="b-lazy" src="/tiny.gif" data-src="%s_1920.jpg" data-src-small="%s_480.jpg" data-src-med="%s_1000.jpg"></a>\n</div>\n<div class="description">\n<p>%s</p>\n</div>\n</div>\n'
			%(dirnames[i],album_dir[j].replace(" ",""),cover_path,cover_path,cover_path,info['description']))

		#make the output directory if it does not exist
		pathlib2.Path('%s/%s/%s' %(output_dir,dirnames[i],album_dir[j])).mkdir(parents=True, exist_ok=True) 
		#define image widths for resize
		basewidth=[480,1000,1920]
		for x in range (len(info['order'])):
			for y in range (len(basewidth)):
				img = Image.open('%s/%s/%s/%s.jpg' %(data_dir,dirnames[i],album_dir[j],info['order'][x]))
				wpercent = (basewidth[y]/float(img.width))
				hsize = int((float(img.height)*float(wpercent)))
				img = img.resize((basewidth[y],hsize), Image.LANCZOS)
				img.save('%s/%s/%s/%s_%s.jpg' %(output_dir,dirnames[i],album_dir[j],info['order'][x],basewidth[y]),'jpeg',icc_profile=img.info.get('icc_profile'),quality=90)
			img.close()

		# init the image_tag var and make the tags
		image_tag=str("")
		for k in range(len(info['order'])):
			img_path=str("%s/%s" %(album_dir[j],info['order'][k]))
			image_tag+=str('<img class="b-lazy" src="/tiny.gif" data-src="%s_1920.jpg" data-src-small="%s_480.jpg" data-src-med="%s_1000.jpg">\n' %(img_path,img_path,img_path))

		# replace the image placeholder with generated images tags
		f = open('album_template.html','r')
		filedata = f.read()
		f.close()
		replace_image = filedata.replace("<!-- #images_go_here -->",image_tag)
		replace_title=replace_image.replace("#album_title",album_dir[j])
		f = open('%s/%s/%s.html' %(output_dir,dirnames[i],album_dir[j].replace(" ","")),'w')
		f.write(replace_title)
		f.close()

	# open the respective file and append the new card tags to the file
	f = open('index_template.html','r')
	filedata = f.read()
	f.close()
	replace_card = filedata.replace("<!-- #card_tag_here -->",card_tag)
	f = open('%s/index.html' %(output_dir),'w')
	f.write(replace_card)
	f.close()

#copies latest CSS and JS to push directory
# shutil.copytree('css','../website_push/css')
# shutil.copytree('js','../website_push/js')