# import the required libs
import glob
import os
import random
import yaml
#Define relative data directory
data_dir="../website_push"
output_dir="../website_push"

# load the file path names in the directory
f = []
for (dirpath, dirnames, filenames) in os.walk(data_dir):
	# filter hiden folders out of the list
	dirnames[:] = [d for d in dirnames if not d[0] == '.']
	break

print(dirnames)

# make a html file for every folder in this directory
for i in range(len(dirnames)):
	# open the new file in write and replace the html title
	f = open("album_template.html",'r')
	filedata = f.read()
	f.close()
	replace_title = filedata.replace("#album_title",dirnames[i])
	# remove spaces from the folder name before saving file
	f = open('%s.html' %(dirnames[i].replace(" ","")),'w')
	f.write(replace_title)
	f.close()

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
		# make the image list from the current directory
		# img_list=glob.glob("%s/%s/%s/*.jpg" %(data_dir,dirnames[i],album_dir[j]))

		# open the album info yaml file and read into a stream
		with open('%s/%s/%s/info.yaml' %(data_dir,dirnames[i],album_dir[j]),'r') as stream:
			info=yaml.load(stream)
		cover_path=str("%s/%s/%s" %(dirnames[i],album_dir[j],info['cover']))
		# append a tag for each subfolders
		card_tag+=str('<div class="album">\n<div class="photo">\n<a href="%s/%s.html"><img class="b-lazy" src="tiny.gif" data-src="%s.jpg" data-src-small="%s_480.jpg" data-src-med="%s_1000.jpg"></a>\n</div>\n<div class="description">\n<p>%s</p>\n</div>\n</div>\n'
			%(dirnames[i],album_dir[j],cover_path,cover_path,cover_path,info['description']))

		# init the image_tag var and make the tags
		image_tag=str("")
		for k in range(len(info['order'])):
			image_tag+=str('<img class="b-lazy" src="tiny.gif" data-src="%s.jpg" data-src-small="%s_480.jpg" data-src-med="%s_1000.jpg">\n' %(info['order'][k],info['order'][k],info['order'][k]))

# 		# open the html template and replace the title
# 		f = open("image_template.html",'r')
# 		filedata = f.read()
# 		f.close()
# 		replace_title = filedata.replace("#file_title",album_dir[j])
# 		f = open('%s\%s.html' %(dirnames[i],album_dir[j].replace(" ","")),'w')
# 		f.write(replace_title)
# 		f.close()

# 		# replace the image placeholder with generated images tags
# 		f = open('%s\%s.html' %(dirnames[i],album_dir[j].replace(" ","")),'r')
# 		filedata = f.read()
# 		f.close()
# 		replace_image = filedata.replace("<!-- #images_go_here -->",image_tag)
# 		f = open('%s\%s.html' %(dirnames[i],album_dir[j].replace(" ","")),'w')
# 		f.write(replace_image)
# 		f.close()

# 	#add temp tag to end of str to replace later
# 	card_tag+=str('\n\n#temp_tag')

# 	# open the respective file and append the new card tags to the file
# 	f = open('%s.html' %(dirnames[i].replace(" ","")),'r')
# 	filedata = f.read()
# 	f.close()
# 	replace_card = filedata.replace("<!-- #card_tag_here -->",card_tag)
# 	f = open('%s.html' %(dirnames[i].replace(" ","")),'w')
# 	f.write(replace_card)
# 	f.close()

# 	#replace temp tag so new cards can be appended later
# 	f = open('%s.html' %(dirnames[i].replace(" ","")),'r')
# 	filedata = f.read()
# 	f.close()
# 	replace_tag = filedata.replace("#temp_tag","<!-- #card_tag_here -->")
# 	f = open('%s.html' %(dirnames[i].replace(" ","")),'w')
# 	f.write(replace_tag)
# 	f.close()