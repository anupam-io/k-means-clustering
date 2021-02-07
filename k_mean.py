# Making the imports
from random import randint, uniform
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
plt.rcParams['figure.figsize'] = (8, 6)


os.system("rm -rf shots; mkdir -p shots;")


def distance(p1, p2):
    assert len(p1) == len(p2)
    
    ret = 0
    for i in range(len(p1)): 
        ret += (p2[1][i] - p1[1][i])**2
    
    return ret**0.5

def centroid(pts):
    return pts.mean()

def draw_this(df, centers, fno):
    X = []
    Y = []
    for i in mat:
        X.append(i[0])
        Y.append(i[1])

    X1 = []
    Y1 = []
    
    for i in range(len(centers)):
        X1.append(centers.iloc[i][0])
        Y1.append(centers.iloc[i][1])
        X1.append(centers.iloc[i][0])
        Y1.append(centers.iloc[i][1])
    
    plt.clf()
    plt.scatter(X, Y)
    plt.scatter(X1, Y1)

    plt.savefig('shots/'+str(fno)+'.png')


def k_mean(X, K):
    """
    INPUTS:
        X: data samples with
            n rows: no. of sample point in the space
            d dimensions: dimension of the samples
        K: number of clusters you want to make

    RETURNS:
        C:  cluster centres
            k rows: no. of clustering points in the space
            d dimensions: dimension of the samples
    """
    no_of_steps = 20

    centers = X.sample(n=K) # Select randomly k centres among the given points
    centers.reset_index(drop=True, inplace=True)

    my_cluster = {}
    for xyz in range(no_of_steps):
        # Assign each point to a cluster center
        for i in X.iterrows():
            # Assign this point to the closes point among all the points in `centres`        
            cl = None
            min_dis = 10*10
            for j in centers.iterrows():
                d = distance(i, j)
                if d<min_dis:
                    min_dis = d
                    cl = j
            my_cluster[i[0]] = cl[0]
        
        # print(my_cluster)
        

        clusters = {}
        for i in X.index:
            clr = my_cluster[i]
            if clr in clusters:
                clusters[clr] = clusters[clr].append(pd.Series(X.iloc[i]))
            else:
                clusters[clr] = pd.DataFrame()
                clusters[clr] = clusters[clr].append(pd.Series(X.iloc[i]))

        new_centers = pd.DataFrame()
        for i in clusters:
            clusters[i] = clusters[i].astype(int)
            new_centers = new_centers.append(centroid(clusters[i]), ignore_index=True)
        
#         print(new_centers.iloc[0])

            
            
        draw_this(df, centers, xyz)
            
        # Termination condition
        if pd.DataFrame.equals(centers, new_centers):
            print('Terminating after ', xyz, ' steps.')
            break
        
        centers =  new_centers
        
        # Find the cost
        total_cost = 0

print('.'*50)
mat = []
for i in range(100):
    mat.append([uniform(0, 100), uniform(0, 100)])
        
        
df = pd.DataFrame(mat, columns=['X', 'Y'])
k_mean(df, 10)