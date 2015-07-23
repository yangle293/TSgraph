import pickle


class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

A = MyClass()

file_Name = "testfile"
# open the file for writing
fileObject = open(file_Name,'wb')

# this writes the object a to the
# file named 'testfile'
pickle.dump(A,fileObject)

# here we close the fileObject
fileObject.close()
# we open the file for reading
fileObject = open(file_Name,'r')
# load the object from the file into var b
b = pickle.load(fileObject)

print b.f()

