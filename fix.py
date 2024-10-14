import os


for (root,_,files) in os.walk("."):
	mds = list(filter(lambda x: x.endswith(".md"), files))
	for fn in mds:
		f = open(os.path.join(root, fn), "r")
		mcode = f.read()
		f.close()

		f = open(os.path.join(root, fn), "w")
		f.write(mcode.replace("$$", "\n$$\n").replace(":", ":\n"))
		f.close()

