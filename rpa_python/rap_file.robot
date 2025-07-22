*** Settings ***
Library		OperatingSystem
Library		os_py.py

*** Test Cases***
check for directory
	${result}	               mk_dir
	Directory Should Exist	       ${result}
	Log To Console		       ${result}

check for Directories

	${result}                      mk_dirs
        Directory Should Exist	       ${result}
        Log To Console		       ${result}

check for removed directories
	${result}			rm_dir
	Directory Should Not Exist     ${result}
        Log To Console		       ${result}
check for removed files
	${result}			remove
	File Should Not Exist		${result}
	Log To Console                  ${result}
check for rename
	${result}			rename
        File Should Exist		${result}
        Log To Console			${result}


check for change directory
        create directory              vicky1
        Change Directory              vicky1
        ${result}=                    getcwd
        Log To Console                ${result}
