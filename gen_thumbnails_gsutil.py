import openslide
import os,sys
from subprocess import call

with open("done.txt") as thmbd:
    thmbs = thmbd.read().splitlines()
thmbd = open("done.txt",'a')
with open("svss") as f:
    slides = f.read().splitlines()
def thumbit():
#    f = open("svss")
    for slide in slides:
        print 'Reading {}\n'.format(slide)
        parts = slide.split('/')
        if slide not in thmbs:      
            directory = "path-imaging-west-thmbs/"+parts[3]+"/"
            if not os.path.exists(directory):
                print '  mkdir {}\n'.format(directory)
                os.makedirs(directory)
            else:
                print '  Skip mkdir {}\n'.format(directory)
            saveas = directory+"thmb_128x64.jpeg"
            print '    Save as {}\n'.format(saveas)
            try:
#                call(['gsutil','cp',slide,'temp_slide.svs'])
#                s = openslide.OpenSlide('temp_slide.svs')
                call(['gsutil','cp',slide,'/var/ramdisk/temp_slide.svs'])
                s = openslide.OpenSlide('/var/ramdisk/temp_slide.svs')
                thmb = s.get_thumbnail((128,64))
                thmb.save(saveas,"JPEG")
                thmbd.write("%s\n"%slide)
                thmbd.flush()
                os.remove('/var/ramdisk/temp_slide.svs')
            except:
                print '*******Unable to open {}\n'.format(saveas)
        else:
            print '    Skipped {}\n'.format(slide)
        sys.stdout.flush
    thmbd.close()
    f.close()

thumbit()
