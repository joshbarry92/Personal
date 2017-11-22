"""Get space utilization for a specified mount point and write to file.

Script to run df and store the results for a specified mount point to a
text file for analysis later.
"""

import datetime
import subprocess


def main():

  now = [str(datetime.datetime.now())]
  file_object = open("space.txt", "a")

  space = subprocess.check_output("df -h | grep shfs", shell=True)
  space_details = space.split()
  sp_details_final = now + space_details

  file_object.write("*****")
  for item in sp_details_final:
    file_object.write("%s\n" % item)
  file_object.write("*****")

if __name__ == "__main__":
  main()
