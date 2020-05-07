import os

def get_dirlist(path):
    """
    Return a sorted list of all entries in path.
    This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """    
    if prefix == "": # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "
    
    dirlist = get_dirlist(path)
    for file in dirlist:
        print(prefix+file) # Print the line
        fullname = os.path.join(path, file) # Turn name into full pathname
        if os.path.isdir(fullname): # If a directory, recurse.
            print_files(fullname, prefix + "| ")

print_files( 'C:/Users/visca/Google Drive/Università/Post-doc/Bologna - 2019/Python/Py-tonici' )