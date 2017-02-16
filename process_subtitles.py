import os
# """
# The Pirates of Silicon Valley file contains an encoding
# error. Run the program to find the error and manually look
# in the file to find out what the problem is.
#
filename = "pirates_of_silicon_valley.srt"
# """
# filename = "small_subtitles.srt"
my_file = open(filename, encoding='utf-8', errors='ignore')
counter = 0
output_file = open("output.js", "a+")
output_file.write("var SUBTITLES = [")
for line in my_file:
  line = line.strip()
  if line == "":
    counter = -1
    output_file.write('{'+"\n")
    output_file.write('Duration: '+ duration+",\n")
    output_file.write('Line1: '+ line1+",\n")
    output_file.write('Line2: '+line2+",\n")
    output_file.write('},'+"\n")
    duration = ""
    line1 = "\"\""
    line2 = "\"\""
  counter +=1
  if counter == 2:
    duration='"'
    duration += line
    duration +='"'
  elif counter == 3:
    line1='"'
    if "\"" in line:
      line = line.replace("\"","\\\"")
    line1 += line
    line1 +='"'
  elif counter == 4:
    line2='"'
    if "\"" in line:
      line = line.replace("\"","\\\"")
    line2 += line
    line2 +='"'
output_file.write('];')
output_file.close()
