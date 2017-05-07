import tarfile
import os

os.chdir(r"C:\Users\Paulina\Downloads//")
tfile = tarfile.open("enron_mail_20150507.tgz")
tfile.extractall(".")

print "you're ready to go!"