

def countDayOfTheWeek():
    # This first line is provided for you
    dayCount = dict()
    file_name = input("Enter a file name: ")    # end assignment

    fileInfo = open(file_name)

    for line in fileInfo:
        if line.startswith('From '):
            positions = line.split()
            #print(positions)
            dayData = (positions[2])
            dayCount[dayData]=dayCount.get(dayData, 0)+1
        
        else:
            continue
    print(dayCount)

#      mbox-short.txt    

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#countDayOfTheWeek()