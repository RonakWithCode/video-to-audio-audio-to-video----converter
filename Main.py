import os # This is os for Changes in file 
path_Video = "Paste full video path" # This variable for path of Video  
path_Audio = "Paste full audio path" # This variable for path of Audio 
        # this Video path, this audio path  
os.rename(path_Video , path_Audio)
        # this Audio path, this Video path  
os.rename(path_Audio , path_Video)