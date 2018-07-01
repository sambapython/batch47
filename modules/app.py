#fun()
'''
import file1
fun()
'''
'''
import file1
print file1.a
print file1.b
file1.fun()
'''
'''
import file1
'''
'''
import file2
'''
'''
import sys
print sys.path
import file2
file2.fun()
'''
'''
import sys
sys.path.append("/home/khyaathi-python")
print sys.path
import file2
file2.fun()
'''
'''
import sys
sys.path.insert(1,"/home/khyaathi-python")
print sys.path
import file2
file2.fun()
'''
'''
import file1
file1.fun()
'''
'''
import folder1
folder1.f1.fun()
'''
'''
from folder1 import f1,f2
f1.fun()
f2.fun()
'''
'''
from folder1.f1 import fun
fun()
'''
'''
from folder1.f1 import fun
from folder1.f2 import fun
fun()
fun()
'''
'''
from folder1.f1 import fun as f1_fun
from folder1.f2 import fun as f2_fun
f1_fun()
f2_fun()
'''
'''
import file1
file1.fun()
'''
import file2
file2.fun()
