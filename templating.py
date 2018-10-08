# import the things
import glob
import os
import random

# load the file path names in the directory
f = []
for (dirpath, dirnames, filenames) in os.walk("../website_data"):
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
	f = open('../wesbite_data/%s.html' %(dirnames[i].replace(" ","")),'w')
	f.write(replace_title)
	f.close()

# # make a card tag in the respective html file for each of the sub folders in that file
# for i in range(len(dirnames)):
# 	print(dirnames[i])
# 	# get all the subfolders in each main folder
# 	temp=[]
# 	for (dirpath_temp, album_dir, filenames_temp) in os.walk("%s" %dirnames[i]):
# 		temp.extend(filenames_temp)
# 		break
# 	print(filenames_temp)

# 	# init the card_tag variable
# 	card_tag=str("")
# 	for j in range(len(album_dir)):
# 		print("--%s" %album_dir[j])
# 		# make the image list from the current directory
# 		img_list=glob.glob("%s\%s\*.jpg" %(dirnames[i],album_dir[j]))
# 		# print("%s\%s\\a.txt" %(dirnames[i],album_dir[j]))
# 		# print(img_list)

# 		# open the album description text file and read into a variable
# 		f = open('%s\%s\description.txt' %(dirnames[i],album_dir[j]),'r')
# 		album_text = f.read()
# 		f.close()
# 		# append a tag for each subfolders
# 		card_tag+=str('<div class="card">\n<img class="card-img-top card" src="%s\%s\zcover.jpg" alt="Card image cap">\n<div class="card-body">\n<h4 class="card-title">%s</h4>\n<p class="card-text">%s</p>\n <a href="%s\%s.html" class="btn btn-primary">View Album</a>\n</div>\n</div>'%(dirnames[i],album_dir[j],album_dir[j],album_text,dirnames[i],album_dir[j].replace(" ","")))

# 		# init the image_tag var and make the tags
# 		image_tag=str("")
# 		for k in range(len(img_list)):
# 			image_tag+=str('<img class="center" src="%s" srcset="" alt="Placeholder">\n' %img_list[k].replace("%s\\"%dirnames[i],""))

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