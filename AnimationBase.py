# -*- coding: utf_8 -*-
"""
Created on 13.07.2014

@author: gitoni
"""

import subprocess as sp
import os
import webbrowser as wb



class Animation(object):
    """
    A class for creating animations with ImageMagick. 
    Paths need to be adapted to your system.
    This here works on Windows, asuming that ImageMagick and Msys is installed and in the Sys Path. 
    """
    def __init__(self, workdir, im_path = r"C:\Program Files (x86)\ImageMagick-6.8.7-Q16\convert.exe", browser = True):
        """
        Define workdir and path to ImageMagick. 
        Set option for opening in browser when finished.
        """
        self.workdir = workdir
        self.im_path = im_path
        self.browser = browser
        print("ready for animation...")
    

    def create_animation(self, aniname, gif = False): 
        output_dir = self.workdir
        try:  
            print("creating animation...")
            aniformat = ".mp4"
            if gif == True:
                aniformat = ".gif"
                
            args = [self.im_path,
                       "-delay", "20", 
                       "*.png", 
                       "-quality", "100%", 
                       "-compress", "None", 
                       "-loop", "0",
                       aniname + aniformat,
                       ]
            p = sp.Popen(args, 
                               cwd = output_dir, 
                               stdin=sp.PIPE, stdout=sp.PIPE)
            t = p.communicate()
            print("remove pngs...")
            args = ["rm.exe", "*.png"]
            p = sp.Popen(args,
                               cwd = output_dir, 
                               stdin=sp.PIPE, stdout=sp.PIPE)
            t = p.communicate()
            print(t)
        except Exception as e:
            print(e)
        if gif == True and self.browser == True:
            pa = os.path.join(output_dir, aniname + aniformat)
            wb.open("file:///" + pa)
        
#...............................................................................
if __name__ == "__main__":
    
    
    def create_pngframes():
        import pylab as pl
        
        liner = [3,5,6,7,8,9,4,7,3,4,6,8,5,3,2,3,2,3,5,7,9,3,5,6,7,8,9,4,7,3,4,6,8,5,3,2,3,2,3,5,7,9]
        for n, ele in enumerate(liner):
            pl.xlim(0,36)
            pl.ylim(0,10)
            pl.plot(range(n),liner[:n],"go", )
            pl.savefig(r"E:\tmp\ani\tmp_" + str(n).zfill(3) + ".png")
    
    
    create_pngframes()
    workdir=r"E:\tmp\ani"
    obj = Animation(workdir)
    obj.create_animation("testani1",gif = True)
