import os, time
import datetime
import shutil

today_date = datetime.date.today()
print("For this test scenario, for the first prompt, enter 'two' and second 'Jovian'")
keyword = input("What specific text would you like me to look for in your files name? ") # this stores the string value of your keyword.. in my test I just used 'two'
keyname = input("Is there a specific name you would like me to look for in a text file? A directory will be created with this name for organization. ")

# This is just DUMMY DATA
def run_once():
    # file one
    file_one = open('file_one.txt', 'w') # this will create this file at the root of main.py
    user_one = 'Hello, my name is Jovian and I have some stuff to say.'
    file_one.write(user_one)
    file_one.close()
    # file two
    file_two = open('file_two.txt', 'w')
    user_two = 'Hello, my name is Tems and I have some stuff to say.'
    file_two.write(user_two)
    file_two.close()

# uncomment the next line to run it
run_once()

# Possible criteria you may want to consider


prop = os.stat("file_one.txt")
last_accessed = str(time.ctime(prop.st_atime)) # this gets last accessed time and converts the value to a string in a variable
la_datetime_obj = datetime.datetime.strptime(last_accessed, "%a %b %d %H:%M:%S %Y").date() # this converts that string to a date object to compare against todays date
print("Size: %s bytes" % prop.st_size)
print("Last Accessed: %s" % time.ctime(prop.st_atime))
print("Last Modified: %s" % time.ctime(prop.st_mtime))


if la_datetime_obj == today_date:  # if the file was created today do what follows
    all_files = os.listdir()
    for file in all_files:  # this lists all the files in the directory main.py is run from
        if '.txt' in file:  # if the extension is of type 'txt'
            #print(all_files[all_files.index(file)])
            with open(file) as f:
                if keyname in f.read():  # as an example if the keyname entered earlier is in the contents of the text of that file...
                    if os.path.exists(keyname):
                        try:
                            f.close()
                            shutil.move(file, keyname)
                        except:
                            # DON'T FORGET TO STATEMENT EVERYTHING BELOW PRINT - These delete straggler files
                            print('Most likely the file already exists in the destination')
                            shutil.rmtree(keyname)
                            os.remove(file)
                    else:
                        f.close()
                        os.mkdir(keyname)
                        shutil.move(file, keyname)
                elif keyword in file: # as an example if the keyword entered earlier is in the file name of that file...
                    if os.path.exists(keyword):
                        try:
                            f.close()
                            shutil.move(file, keyword)
                        except:
                            # DON'T FORGET TO STATEMENT EVERYTHING BELOW PRINT - These delete straggler files
                            print('Most likely the file already exists in the destination')
                            shutil.rmtree(keyword)
                            os.remove(file)
                    else:
                        f.close()
                        os.mkdir(keyword)
                        shutil.move(file, keyword)
