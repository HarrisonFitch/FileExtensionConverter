'''
	This is a simple file conversion script.

    Given a path, input extension, and output extension, this script
    will convert all files in the path with the input extension
    to the output extension. This will also perform the same action
    in all child directories within the given path. Use with CAUTION.

	Notes: 	June 1, 2020	Initial Version

'''

import os

def convertFileExt( directPath, inputExt, outputExt ):
    for root, dir, filename in os.walk( directPath):
        # For the files in the directory convert the extension
        # from the inputExt to the outputExt.
        for name in filename:
            if name.endswith( inputExt ):
                file_path = os.path.join( root, name )
                new_name = file_path.replace( inputExt, outputExt )
                os.rename( file_path, new_name )

        for folder in dir:
            # if there is a folder in the directory, search the folder as well
            convertFileExt( os.path.abspath( folder ), inputExt, outputExt )

################################## MAIN BLOCK #####################################

# Get user inputs for path and extraction style
_directPath_    = input ( "Enter the path containing the file(s) (PLAIN TEXT): " )
while not os.path.exists( _directPath_ ) and not os.path.isdir( _directPath_ ):
    print(  "ERROR: The provided path is not valid.\n"
            "Please check that the path is a valid directory.\n")
    _directPath_    = input ( "Enter the path containing the file(s) (PLAIN TEXT): " )

_inputExt_      = input ( "Enter the input file extension (.txt) : ")
_outputExt_     = input ( "Enter the output file extension (.md) : ")

convertFileExt( _directPath_, _inputExt_, _outputExt_ )


####################################################################################