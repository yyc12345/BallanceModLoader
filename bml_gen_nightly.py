import bml_config

with open('NightlyVer.h', 'w') as fout:
	if (bml_config.nightly is not None) and len(bml_config.nightly) != 0:
		fout.write('#define BML_NIGHTLY_VER "' + bml_config.nightly + '"\n')
	else:
		fout.write('// Yes, this is just a placeholder.\n')
