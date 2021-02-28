import os
import time
from pathlib import Path

# Intro
def home():
	print("\n------Welcome to Course Plan Organizer------")
	print("by Daffa Ananda Pratama Resyaly -- 13519107\n")
	print("Pick your choice: (Enter/Exit)")

# Read input from text file
# And change it to DAG (containing list of course and its prerequisite)
def readfile(filename):
	# Open the text file and read it line-by-line
	fOpen = open(filename)
	fRead = fOpen.read().split('\n')

	listCourse = []
	for line in fRead:
		# Clean each line from unwanted characters
		# e.g. From "C1, C2, C3." to "C1,C2,C3"
		line = line.strip()
		line = line.strip('.')
		line = line.replace(' ', '')
		# Insert each course ID that was separated by comma to listCourse
		# e.g. From "C1,C2,C3" to "['C1', 'C2', 'C3']"
		line = line.split(',')
		listCourse.append(line)

	return listCourse

def topologicalsort(listCourse, result):
	# Do process recursively until the list of course has no more element
	if len(listCourse) != 0:
		available = []
		# Find course which has no prerequisite in list of course to be processed first
		# Insert that course to list of available courses
		for courses in listCourse:
			if (len(courses) == 1):
				available.append(courses[0])
		i = 0
		while (i < len(listCourse)):
			# Delete node of the course which is in list 'available' on each course in listCourse,
			# if it's one of the prerequisites of relevant course
			for course in available:
				if course in listCourse[i]:
					listCourse[i].remove(course)
			# Delete node that has been removed before
			# (the one(s) on list 'available')
			# Size of listCourse is reduced by 1
			if (len(listCourse[i]) == 0):
				listCourse.remove(listCourse[i])
				i-=1
			i+=1

		# Format of output if it's possible to take more than one course in a semester
		# e.g. "Semester IV : IF2211, IF2212"
		# Append to result list first
		courseID = ""
		for i in range(len(available)):
			if (i+1 == len(available)):
				courseID += available[i]
			else:
				courseID += available[i]
				courseID += ', '
		result.append(courseID)
		# Recursive call of topological sort
		topologicalsort(listCourse, result)
	return result

# Show the recommended course plan out to CLI
def courseplan(result):
	for i in range (len(result)):
		# Show the output in format :
		# "Semester <which semester> : <courseID, courseName>"
		print("Semester", end=' ')
		# Determine semester based on i (same as switch case in C)
		# Assumption : Maximum semester is 8
		semester = {
		0:"I",
		1:"II",
		2:"III",
		3:"IV",
		4:"V",
		5:"VI",
		6:"VII",
		7:"VIII"
		}[i]
		print(semester, end='')
		print("\t: " + result[i], end='')
		
		# End every semester except last semester with newline
		# End last semester with '.'
		if (i+1 != len(result)):
			print()
		else:
			print('.')

# Main Program
# Welcome
if __name__ == "__main__":
	home()
	option = str(input())
	option = option.lower()
	# Determine action based on option
	if (option == 'enter'):
		# Initialization to count the execution time
		start_time = time.time()
		# option == Enter => Start Program
		# Initialize test file with its path
		path = os.path.dirname(Path(__file__).absolute().parent)
		filename = "test3.txt"
		ffilename = os.path.join(path, 'test', filename)

		print('\nReading from file "%s"\n' % filename)
		print('Recommended Course Plan:')
		print('------------------------')

		# Start reading file and determine the output
		f = readfile(ffilename)
		res = []
		test2 = topologicalsort(f, res)
		courseplan(test2)

		# Show the program execution time
		print("\nProgram execution time : %f detik" % (time.time() - start_time))
		print("Goodbye~")
	else:
		# option == Exit => Exit Program
		exit()
