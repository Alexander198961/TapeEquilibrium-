	

list = [ 3 , 1 , 2 , 4 , 3 ]
def solution(A):
	sum2=0;
	sum1=0;
	minim=""
	for i in range(1,len(list)):
		for i in range(0, i):
			sum1=sum1+list[i]
			size=len(list)	
		for j in range(i+1,size):
			sum2=sum2+list[j]
			sum=sum1-sum2
		if sum < 0:
			sum=0-sum
		if minim == "":
			minim=sum
			
		if minim>sum:
			minim=sum
		sum1=0;
		sum2=0;
	return minim
a=solution(list);
print a
#def solution(A):
#print  minim	

#number=solution(list)
#print number
