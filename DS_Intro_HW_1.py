# Gal Giller 209264555
# 1
def  my_func(x1,x2,x3):
    if ((type(x1)==float) and (type(x2)==float) and (type(x3)==float)):
        a = x1+x2+x3
        b = (x2+x3)*x3
        if a == 0:
            return "Not a number - denominator equals zero"
        else:
            return float((a*b)/a)
    else:
        print("Error: parameters should be double")
# 2
def convert(hours, minutes):
    if (hours>= 0 and minutes>=0):
        c = int(hours*60*60)
        d = int(minutes*60)
        return (c+d)
    else:
        print("Input error!")