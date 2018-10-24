import email.parser 
import os, sys, stat

def DiscardTag(srcdir):
	fp = open(srcdir)
	body = fp.read()
	result = []
	b = True
	for char in body:
		if b and char == '<':
			b = False
		if b:
			result.append(char)
		if not b and char == '>':
			b = True
	fp.close()
	return ''.join(result)

def DiscardAllTag(srcdir):
	files = os.listdir(srcdir)
	for file in files:
		srcpath = os.path.join(srcdir, file)
		src_info = os.stat(srcpath)
		if stat.S_ISDIR(src_info.st_mode): # for subfolders, recurse
			DiscardAllTag(srcpath)
		else:  # discard tag
			body = DiscardTag(srcpath)
			fp = open(srcpath, 'w')
			fp.write(body)
			fp.close()

print 'Input source directory: ' #ask for source and dest dirs
srcdir = raw_input()
if not os.path.exists(srcdir):
	print 'The source directory %s does not exist, exit...' % (srcdir)
	sys.exit()

DiscardAllTag(srcdir)