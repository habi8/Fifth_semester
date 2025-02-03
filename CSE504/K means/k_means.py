import math
import copy

with open("input.txt", "r") as file:
    datapoints = [line.strip().split() for line in file]  

datapoints = [[int(num) for num in point] for point in datapoints]
print("Datapoints:", datapoints)

dataPoints_num = len(datapoints)
centroids_num = 3
prevCentroids = [[3,3],[3,7],[9,4]]
#centroids = datapoints[:centroids_num] 
centroids = [[3,3],[3,7],[9,4]]
distance = [[None] * centroids_num for _ in range(dataPoints_num)]
clusters = [None] * dataPoints_num
print("Centroids:", centroids)


stop = False
iter = 1

while(stop==False):
    for i in range(dataPoints_num):
        min_distance = 9999;
        for k in range(centroids_num):
            x2 = centroids[k][0]
            x1 = datapoints[i][0]
            y2 = centroids[k][1]  
            y1 = datapoints[i][1]  
            distance[i][k]=(math.sqrt((x2-x1)**2 + (y2-y1)**2))
             
            print(f"Distance between {datapoints[i]} and {centroids[k]}: ",distance[i][k])
        
            if(distance[i][k]<min_distance ):
                min_distance = distance[i][k]
                clusters[i]=k;
        print("\n")
    
    print("cluster: ",clusters)
    
        
    i = 0
    j = 0
    
    for i in range(centroids_num):
        sumx = 0
        sumy = 0
        count = 0
        for j in range(dataPoints_num):
            if(clusters[j]==i):
                sumx+=datapoints[j][0]
                sumy+=datapoints[j][1]
                #print("sumxy",sumx,sumy)
                count+=1
                
        meanx = sumx/count
        meany = sumy/count
        # print(meanx)
        # print(meany)
        
        
        print("Previous centroids " ,i ,prevCentroids)

        centroids[i][0] = meanx
        centroids[i][1] = meany
    
        print("New centroids ",centroids)

    resDis = [0]*centroids_num
    
    print("Differnece :")
    i=0
    max = 0
    print(prevCentroids[2][0])
    print(centroids[2][0])
    for i in range(centroids_num):
         resDis[i]= math.sqrt((prevCentroids[i][0]-centroids[i][0])**2+(prevCentroids[i][1]-centroids[i][1])**2)
         print(resDis[i])
         if(resDis[i]>max):
             max = resDis[i];
    
         print(max)
    if(max > 0.05):
        prevCentroids = copy.deepcopy(centroids)
    else:   
        stop = True
    
    iter+=1
    
##print(clusters)

        
