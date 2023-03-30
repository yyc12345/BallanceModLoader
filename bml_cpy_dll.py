import bml_config
import os
import sys
import shutil

if len(sys.argv) != 2 or sys.argv[1] not in ('Debug', 'Release', ):
	print("Error parameter!")
	print("Format: python bml_cpy_dll.py [Debug|Release]")
	sys.exit(1)

sln_configuration = sys.argv[1]
vcxproj_output = os.path.join('Build', sln_configuration)
shutil.copy(os.path.join(vcxproj_output, 'BML.dll'), os.path.join(bml_config.deploy_path, 'BML.dll'))
