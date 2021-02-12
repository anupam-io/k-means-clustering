import os
import imageio
cur_dir = os.getcwd()
images = []

filenames = []
for i in range(6):
    filenames.append(cur_dir+'/shots/'+str(i)+'.png')

for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave(cur_dir+'/'+'foo.gif', images, duration=0.5)