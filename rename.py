import glob, os
import argparse
#ap = argparse.ArgumentParser()
#ap.add_argument("-d", "--dataset", required=True,
#	help="path to input dataset")
#args = vars(ap.parse_args())

allfiles = glob.glob('*.mp3')
for afile in allfiles:
  os.rename(afile, 't_'+ afile)
 
allfiles = glob.glob('*.mp3')
count=0
for afile in allfiles:
  new_filename =str(count).zfill(3) + '.mp3'
  print (new_filename)
  os.rename(afile, new_filename)
  count += 1
print("Done")