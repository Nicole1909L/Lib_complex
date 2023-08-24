import math
def sumacplx(c1,c2):
    part_real = c1[0] + c2[0]
    part_img = c1[1] + c2[1]
    return (part_real,part_img)

def multicplx(c1,c2):
    part_real = c1[0] * c2[0] - c1[1] * c2[1]
    part_img = c1[0] * c2[1] + c2[0] * c1[1]
    return (part_real, part_img)

def restcplx(c1,c2):
    part_real = c1[0] - c2[0]
    part_img = c1[1] - c2[1]
    return (part_real,part_img)

def divicplx(c1,c2):
    numer = multicplx(c1,(c2[0],-c2[1]))
    denom = multicplx(c2,(c2[0],-c2[1]))
    part_real = numer[0]/denom[0]
    part_img = numer[1]/denom[0]
    return (part_real,part_img)

def moducplx(c):
    a = c[0]**2
    b = c[1]**2
    modulo = math.sqrt(a+b)
    return (modulo)

def conjucplx(c):
    part_real = c[0]
    part_img = -c[1]
    return (part_real,part_img)

def fasecplx(c):
    x = c[1] / c[0]
    fase = math.atan(x)
    return (fase)

def geomcplx(c):
    p = moducplx(c)
    ang = fasecplx(c)
    part_real = p * math.cos(ang)
    part_img = p * math.sin(ang)
    return (part_real,part_img)

if __name__ == '__main__':
    print(sumacplx((3,2),(-5,5.2)))
    print(multicplx((3,2),(4,-5)))
    print(restcplx((3, 2), (-5, 5.2)))
    print(divicplx((3,2),(4,-5)))
    print(moducplx((2,8)))
    print(conjucplx((4,5)))
    print(fasecplx((2,8)))
    print(geomcplx((2,8)))