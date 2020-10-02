P = 100000
#ROI
R = 10
print("Enter number of years - ")
#months
Y = 1
N = Y*12
r=R/1200
n=(1+r)**N
EMI=(P*r*n)/(n-1)
Balance=P
print("EMI is - ", EMI)

def emi_inr(a,b,c):
	return((a*b*c)/100)

for n in range(N):
	interest=emi_inr(Balance,Y,R)/12
	prin_ded=EMI-interest
	Balance=Balance-prin_ded
	print("",prin_ded,"	",interest,"	",Balance)
P_RD=5000
#ROI
r_RD=8.25
#years
n_RD=1
#Interest Rate: Check below RD Interest rates for various banks.
#Compounding: It means when your money gains interest in a year, usually in most of the banks its "Quarterly"
#Duration: Generally, minimum time period is 6 months and its usually multiple of 3.
#Maturity Amount: It is the total amount that you will get after your time period.
#Installment: Installment amount that you have to pay each month.

#https://jira.ges.symantec.com/browse/CMPS-12900


Compounding=3
cf_RD=12/Compounding
r_RD=r_RD/100
mid=1+r_RD/cf_RD
A_RD = P_RD*((mid**(cf_RD*n_RD)-1)/(1-mid**(-cf_RD/12)))
print("Amount - ",A_RD)

A_RD=P_RD*(1+r_RD/cf_RD)**(cf_RD*n_RD)
print("Amount 2- ",A_RD)

A_RD=1000000
r_RD=8.2
n_RD=10
cf_RD=12
r_RD=r_RD/100
mid=1+r_RD/cf_RD
P_RD=A_RD/((mid**(cf_RD*n_RD)-1)/(1-mid**(-cf_RD/12)))
print("SIP- ",P_RD)