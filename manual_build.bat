MSBuild BML.sln -p:Configuration=Debug -p:Platform=x86
MSBuild BML.sln -p:Configuration=Release -p:Platform=x86
python bml_package_release.py
