import bml_config
import os
import shutil

# remove dist folder first
shutil.rmtree('Dist', True)

# Create dev package
if bml_config.nightly is not None and len(bml_config.nightly) != 0:
	dist_dir = 'Dist\\Dev\\BML-{}.{}.{}-dev'.format(*bml_config.version)
else:
	dist_dir = 'Dist\\Dev\\BML-nightly-{}.{}.{}.{}-dev'.format(*bml_config.version, bml_config.nightly)
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

# Create user package
if bml_config.bmlmods_path is not None and len(bml_config.bmlmods_path) != 0:
	if bml_config.nightly is not None and len(bml_config.nightly) != 0:
		dist_dir = 'Dist\\User\\BML-{}.{}.{}'.format(*bml_config.version)
	else:
		dist_dir = 'Dist\\User\\BML-nightly-{}.{}.{}.{}'.format(*bml_config.version, bml_config.nightly)
	os.makedirs(dist_dir)

	os.makedirs(dist_dir + '\\BuildingBlocks')
	shutil.copy('Build\\Release\\BML.dll', dist_dir + '\\BuildingBlocks')

	os.makedirs(dist_dir + '\\ModLoader')
	os.makedirs(dist_dir + '\\ModLoader\\Config')
	os.makedirs(dist_dir + '\\ModLoader\\Maps')
	os.makedirs(dist_dir + '\\ModLoader\\Mods')
	os.makedirs(dist_dir + '\\ModLoader\\Trails')

	# Due to Gamepiaynmo/BML-Mods build configuration
	# We should copy mods from deploy path
	# todo: update Gamepiaynmo/BML-Mods build strategy to 
	# make this copy more proper
	mods_folder = os.path.join(bml_config.deploy_path, 'ModLoader\\Mods')
	shutil.copy(os.path.join(mods_folder, 'BallSticky.zip'), dist_dir + '\\ModLoader\\Mods\\BallSticky.zip')
	shutil.copy(os.path.join(mods_folder, 'BMLModuls.zip'), dist_dir + '\\ModLoader\\Mods\\BMLModuls.zip')
	shutil.copy(os.path.join(mods_folder, 'DeformedWB.bmod'), dist_dir + '\\ModLoader\\Mods\\DeformedWB.bmod')
	shutil.copy(os.path.join(mods_folder, 'DualBallControl.bmod'), dist_dir + '\\ModLoader\\Mods\\DualBallControl.bmod')
	shutil.copy(os.path.join(mods_folder, 'DynamicFov.bmod'), dist_dir + '\\ModLoader\\Mods\\DynamicFov.bmod')
	shutil.copy(os.path.join(mods_folder, 'MapScripts.bmod'), dist_dir + '\\ModLoader\\Mods\\MapScripts.bmod')
	shutil.copy(os.path.join(mods_folder, 'SpiritTrail.bmod'), dist_dir + '\\ModLoader\\Mods\\SpiritTrail.bmod')
	shutil.copy(os.path.join(mods_folder, 'TASSupport.bmod'), dist_dir + '\\ModLoader\\Mods\\TASSupport.bmod')

	shutil.make_archive(dist_dir, 'zip', dist_dir)
