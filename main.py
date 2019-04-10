f = open('diabetic_data.txt','r')
#  vector of features
features = f.readline()
features = features.rstrip()
features = features.split(',')
#  list of data points
data_points = f.readlines()
f.close()
N = len(data_points)  # number of data points
# saving only first visit of each patient
for i in range(N):
    data_point = data_points[i].rstrip()
    data_points[i] = data_point.split(',')

list = sorted(data_points, key=lambda x: x[1])
new_list = []
for i in range(N):
    if list[i][7]!='11' and list[i][7]!='13' and list[i][7]!='14':  # "cleaning" data by removing encounters that resulted in hospice or death
        if i == 0:
            new_list.append(list[i])  # add the admission to the new list
        elif list[i][1] != list[i-1][1]:  # this is the first admission of the patient
            new_list.append(list[i])

print(len(new_list))
