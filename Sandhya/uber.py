import csv
import numpy as np
#from sklearn import svm
from scipy import stats

#Tells us what filename we want
filename = "SF_data.csv"
filename = "TT_DayOfWeek.csv"
filename = "fire.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 
data = []
nov = []
dec = []

print('\n')

# reading csv file 
with open(filename, 'r') as csvfile:  #file object is named csvfile
       #creating a csv reader object 
       #converted to csvreader object
       csvreader = csv.reader(csvfile) 
          
       # extracting field names through first row 
       fields = csvreader.next() 
      
       print("extracting each data row one by one")
       # extracting each data row one by one 
       for row in csvreader: 
          rows.append(row) 
          data += [row]
          
       # get total number of rows 
       print("Total no. of rows: %d"%(csvreader.line_num))

              
# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 
                
#  printing first 5 rows 
def firstfive():
    print('\nFirst 5 rows are:\n') 
    for row in rows[:5]: 
          # parsing each column of a row 
          for col in row: 
             print("%10s"%col), 
          print('\n') 

#filters data. returns a tuple where 1st element is data in month of nov and 2nd is data in month of dec
def sortData():
    dec = []
    nov = []

    for row in data:
        month = (int) (row[2])
        #print("month: ", month, type(month) )
        if(month == 11):
            nov += [row]
        if(month == 12):
            dec += [row]
    return nov,dec
nov,dec = sortData()

#this computes a t-test and prints the resulting t-value and p-value
def ttest():
    novA = np.asarray(nov).astype(np.float)
    decA = np.asarray(dec).astype(np.float)
    novB = novA[:,3]
    decB = decA[:,3]

    (t, prob) = stats.ttest_ind(novB, decB)
    print("t: ", t)
    print("p-val: ", prob)
    if(prob < 0.05):
        print("can conclude that there is a difference in means")
ttest()

newdata = np.array(data) #so newdata is now of type nd.array


#Creates a SVM using the first 1000 data as the training data
#tries to predict the last 10 entries (using that as test data)
def prediction():
        print("entered prediction function")
        features = newdata[:, [0,3]]
        target1 = newdata[:, [1] ]
        features = features.tolist()
        target1 = target1.tolist()
        target3 = []
        for x in target1:
            target3 += x
        target = np.array(target3)

        #clf = svm.SVC(gamma='auto')
        clf = svm.SVC(gamma=0.001, C=100.)
        print("fitting")
        clf.fit(features[:1000], target[:1000]) 
        print("predicting")
        res = clf.predict(features[-10:])
        print ("testing set is last 10 samples of features")
        print ("it predicted", res)
        print ("actual results: ", target[-10:])
        #print "accuracy: ", clf.score(features[-10:], target[-10:])

#prediction()

#Computes average time for the day of the week
def AvgTimes(data):
	print("Average travel time for Monday is")
	count = 0
	time = 0
	for row in data:
		if(row[2] == '1'):
			count = count + 1
			time += float(row[3])
	avg = time/count
	avg = round(avg,2)
	print (avg, "seconds", " or ", round(avg/60,2) , "minutes")


	print("Average travel time for Tuesday is")
	count = 0
	time = 0
	for row in data:
		if(row[2] == '2'):
			count = count + 1
			time += float(row[3])
	avg = time/count
	avg = round(avg,2)
	print (avg, "seconds", " or ", round(avg/60,2) , "minutes")


	print("Average travel time for Wednesday is")
	count = 0
	time = 0
	for row in data:
		if(row[2] == '3'):
			count = count + 1
			time += float(row[3])
	avg = time/count
	avg = round(avg,2)
	print (avg, "seconds", " or ", round(avg/60,2) , "minutes")


	print("Average travel time for Thursday is")
	count = 0
	time = 0
	for row in data:
		if(row[2] == '4'):
			count = count + 1
			time += float(row[3])
	avg = time/count
	avg = round(avg,2)
	print (avg, "seconds", " or ", round(avg/60,2) , "minutes")


	print("Average travel time for Friday is")
	count = 0
	time = 0
	for row in data:
		if(row[2] == '5'):
			count = count + 1
			time += float(row[3])
	avg = time/count
	avg = round(avg,2)
	print (avg, "seconds", " or ", round(avg/60,2) , "minutes")

