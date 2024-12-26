from lzma import open as lopen
from tarfile import open as topen

LEVEL = 'submit'
FNAME = 'better_farm_systems_%s_image.xz'

# 'close', 'closed', 'detach', 'fileno', 'flush', 'isatty', 'peek', 'read', 'read1'
# 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'seek', 'seekable'
# 'tell', 'truncate', 'writable', 'write', 'writelines'

with topen(FNAME % LEVEL, 'r:xz') as fp:
	print(fp.inodes)