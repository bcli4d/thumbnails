import openslide
import os,sys

f = open("svss")
for slide in f:
    parts = slide.split('/')
#    print(parts)
    directory = "path-imaging-west-thmbs/"+parts[3]+"/"
    if not os.path.exists(directory):
        print '  mkdir {}\n'.format(directory)
        os.makedirs(directory)
    else:
        print '  Skip mkdir {}\n'.format(directory)
    
    saveas = directory+"thmb_128x64.jpeg"
    if not os.path.exists(saveas):
        print '    Save as {}\n'.format(saveas)
        try:
            print 'Reading {}\n'.format(slide)
            slide = slide.rsplit('//',1)[1].strip()
            s = openslide.OpenSlide(slide)
            thmb = s.get_thumbnail((128,64))
            thmb.save(saveas,"JPEG")
        except:
            print '*******Unable to open {}\n'.format(saveas)
    else:
        print '    Skipped {}\n'.format(saveas)
