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













