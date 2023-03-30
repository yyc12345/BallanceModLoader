import bml_config, bml_get_ver
import os
import shutil

# remove dist folder first
shutil.rmtree('Dist', True)

# Create dev package
if (bml_config.nightly is not None) and len(bml_config.nightly) != 0:
	dist_dir = 'Dist\\BML-nightly-{}.{}.{}.{}-dev'.format(*bml_get_ver.GetBMLVersion(), bml_config.nightly)
else:
	dist_dir = 'Dist\\BML-{}.{}.{}-dev'.format(*bml_get_ver.GetBMLVersion())
os.makedirs(dist_dir)

os.makedirs(dist_dir + '\\include\\BML')
shutil.copy('BMLAll.h', dist_dir + '\\include\\BML')
shutil.copy('BuildVer.h', dist_dir + '\\include\\BML')
shutil.copy('ExecuteBB.h', dist_dir + '\\include\\BML')
shutil.copy('Export.h', dist_dir + '\\include\\BML')
shutil.copy('Gui.h', dist_dir + '\\include\\BML')
shutil.copy('IBML.h', dist_dir + '\\include\\BML')
shutil.copy('ICommand.h', dist_dir + '\\include\\BML')
shutil.copy('IConfig.h', dist_dir + '\\include\\BML')
shutil.copy('ILogger.h', dist_dir + '\\include\\BML')
shutil.copy('IMod.h', dist_dir + '\\include\\BML')
shutil.copy('NightlyVer.h', dist_dir + '\\include\\BML')
shutil.copy('RegisterBB.h', dist_dir + '\\include\\BML')
shutil.copy('ScriptHelper.h', dist_dir + '\\include\\BML')
shutil.copy('Version.h', dist_dir + '\\include\\BML')
shutil.copytree('virtools', dist_dir + '\\include\\BML\\virtools', ignore = shutil.ignore_patterns('*.cpp'))

os.makedirs(dist_dir + '\\bin\\Release')
os.makedirs(dist_dir + '\\lib\\Release')
shutil.copy('Build\\Release\\BML.dll', dist_dir + '\\bin\\Release')
shutil.copy('Build\\Release\\BML.lib', dist_dir + '\\lib\\Release')

os.makedirs(dist_dir + '\\bin\\Debug')
os.makedirs(dist_dir + '\\lib\\Debug')
shutil.copy('Build\\Debug\\BML.dll', dist_dir + '\\bin\\Debug')
shutil.copy('Build\\Debug\\BML.lib', dist_dir + '\\lib\\Debug')

shutil.make_archive(dist_dir, 'zip', dist_dir)
