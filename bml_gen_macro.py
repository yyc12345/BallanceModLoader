import bml_config

with open('BuildVer.h', 'w') as fout:
	fout.write('#define BML_MAJOR_VER ' + str(bml_config.version[0]) + '\n')
	fout.write('#define BML_MINOR_VER ' + str(bml_config.version[1]) + '\n')
	fout.write('#define BML_BUILD_VER ' + str(bml_config.version[2]) + '\n')
	if bml_config.nightly is not None and len(bml_config.nightly) != 0:
		fout.write('#define BML_NIGHTLY_VER "' + bml_config.nightly + '"\n')
