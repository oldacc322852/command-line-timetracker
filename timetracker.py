import sys, select, os, time, datetime, csv
from termcolor import colored

def write_to_file():
	with open('timelog.csv', 'a', newline='') as csvfile:
		csvfile.write(message)

activity = input('What are you going to study? ').lower()

running = input('Do you wish to start the clock (Y/N)? ').lower()

if(running == 'y' or running == 'yes'):

	start_time = datetime.datetime.now().replace(microsecond = 0)

	while True:
	    os.system('cls' if os.name == 'nt' else 'clear')

	    time_passed = datetime.datetime.now().replace(microsecond = 0) - start_time
	    time_passed = str(time_passed)

	    message = activity + ', ' + str(start_time) + ', ' + time_passed + '\n'


	    print('Currently studying: ', colored(activity, 'green'))
	    print('Press ENTER to stop.\n')
	    print(colored(time_passed, 'green'))
	    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
	        line = input()
	        break
	    time.sleep(1)

	write_to_file()


