import random
import statistics
random.seed(0)
salaries = [round(random.random()*1000000, -3) for _ in range(100)]
print(salaries)


#The Mean is:
sum = 0
#values = [8,20,12,15,4]
n = len(salaries)

for i in salaries:
    sum = sum + i

mean = sum/n
print ('The Mean is: ' + str(mean)) 


# The Median is:
median=statistics.median(salaries)
print ('The Median is: ' + str(median)) 

#The Mode is:
Mode=statistics.mode(salaries)
print ('The Mode is: ' + str(Mode))

### sample variance.Remember to use Bessel's correction.
Variance=statistics.variance(salaries)
print ('The Variance is: ' + str(Variance))

# sample standard deviation.Remember to use Bessel's correction.
SDeviation=statistics.stdev(salaries)
print ('The standard deviation is: ' + str(SDeviation))

##range
max=max(salaries)
min=min(salaries)
our_range=max-min
print(our_range) 


#coefficient of variation
#import numpy as np
#import pandas as pd

#define function to calculate cv
import numpy as np
import pandas as pd
cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100 
df = pd.array(salaries)
df.apply(cv)


#interquartile range

from scipy import stats

x = stats.iqr(salaries)

print(x)

#quartile coefficent of dispersion
import numpy

x = numpy.std(salaries)

print(x)

#min-max scaling
#
from sklearn.preprocessing import minmax_scale

minmax_scale(salaries)

#standardizing

from sklearn import preprocessing
data = array.salaries()
 
# separate the independent and dependent variables
X_data = data.data
target = data.target
 
# standardization of dependent variables
standard = preprocessing.scale(salaries)
print(standard)

#covariance
#import pandas as pd
COV=salaries.cov()
print(COV)





     
     













