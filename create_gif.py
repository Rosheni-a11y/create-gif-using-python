import imageio.v3 as iio
import os
import sys



def create_gif(image_files,output_name='output.gif',duration=500,loop=0):
  images = []

  for filename in image_files:
    if not os.path.exists(filename):
      print(f" Warning:{filename} not found, skipping..")
      continue
    images.append(iio.imread(filename))

  if len(images) < 2:
    print("Error: Need at least 2 images to create a GIF")
    return

  iio.imwrite(output_name,images,duration=500,loop=0)
  print(f"GIF created: {output_name}")


if __name__ =="__main__":
 filenames = ['hippocorn1.png','hippocorn2.png','hippocorn3.png','hippocorn4.png']
 create_gif(filenames,'hippocorn.gif',duration=500,loop=0)