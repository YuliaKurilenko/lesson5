from pprint import pprint
file_name = "byron.txt"
my_file = open(file_name, mode="rb")
file_content = my_file.read()
my_file.close()
pprint(file_content.decode("utf-8"))






