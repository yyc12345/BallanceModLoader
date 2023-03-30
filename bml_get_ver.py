
def GetBMLVersion():
    version = [0, 0, 0]

    with open('BuildVer.h', 'r') as fin:
        for i in range(3):
            version[i] = int(fin.readline().split(' ')[-1])

    return version
	