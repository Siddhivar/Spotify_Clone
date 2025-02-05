import cmath
import math

inp = int(input("Select default(0, 1, 2) or custom(3) : "))
V = 220
alpha = 2
De = 1.828 * 0.01
Nc = float(2)
Ne = 1
Cal = 180
Cst = 80
Temp = 0.004
cost_of_energy = 5

if inp == 0:
    W1 = 2.2854
    W2 = 1.492
    E = 0.787
    A = 5.2970
    d = 0.02597
    Alpha = 17.7
    UTS = 13780
    y = 5.7904
    d_dash = 10.4589
    WtAl = float(896)
    WtSt = float(596)
    R_at20 = float(0.08989)
elif inp == 1:
    W1 = 1.98858
    W2 = 1.2290
    E = 0.787
    A = 4.3189
    d = 0.02345
    Alpha = 17.73
    UTS = 11310
    y = 5.7904
    d_dash = 10.4589
    WtAl = float(738)
    WtSt = float(491)
    R_at20 = float(0.11020)

elif inp == 2:
    W1 = 2.5389
    W2 = 1.726
    E = 0.787
    A = 6.1268
    d = 0.02793
    Alpha = 17.73
    UTS = 15910
    y = 5.7904
    d_dash = 10.4589
    WtAl = float(1036)
    WtSt = float(690)
    R_at20 = float(0.07771)

else:
    W1 = float(input("W1 : "))
    W2 = float(input("W2 or W3 or Wc : "))
    E = float(input("E(x * 10^11) : "))
    A = float(input("A(x * 10^(-4)) : "))
    # T = float(input("T(given) : "))
    UTS = int(input("UTS : "))
    Alpha = float(input("Alpha(  x * 10^(-6)  )  : "))
    y = float(input("y(m) : "))
    d = float(input("diameter of conductor,d(m) : "))
    d_dash = float(input("d'(m) : "))
    WtAl = float(input("Wt of Al strands : "))
    WtSt = float(input("Wt of St strands : "))
    R_at20 = float(input("Resistance of R at 20 C: "))

E = E * pow(10, 11)
p = 100
A = A * pow(10, -4)
fos1 = 2
fos2 = 2
l = float(250)
Alpha = Alpha * pow(10, -6)


def calculate(length, temp, T):
    line = length
    first = pow(W1, 2) * pow(line, 2) * E * A / (24 * pow(T, 2))

    second = temp * Alpha * E * A
    third = T
    a = 1
    b = first + second - third
    c = 0
    # e = pow(10, 2)
    d = -pow(W2, 2) * pow(line, 2) * E * A / 24

    # print("a : " + str(a))
    # print("b : " + str(b))
    # print("c : " + str(c))
    # print("d : " + str(d))

    # calculate intermediate values
    p = (3 * a * c - b**2) / (3 * a**2)

    q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)
    delta = q**2 / 4 + p**3 / 27
    x1 = 0
    x2 = 0
    x3 = 0
    # determine number and type of roots
    if delta > 0:  # one real and two complex roots
        u = (-q / 2 + cmath.sqrt(delta)) ** (1 / 3)
        v = (-q / 2 - cmath.sqrt(delta)) ** (1 / 3)
        x1 = u + v - b / (3 * a)
        x2 = -(u + v) / 2 - b / (3 * a) + (u - v) * cmath.sqrt(3) / 2j
        x3 = -(u + v) / 2 - b / (3 * a) - (u - v) * cmath.sqrt(3) / 2j
        # print("One real root and two complex roots:")
        # print("x1 = ", x1.real)
        # print("x2 = ", x2)
        # print("x3 = ", x3)
    elif delta == 0:  # three real roots, two are equal
        u = (-q / 2) ** (1 / 3)
        v = u
        x1 = 2 * u - b / (3 * a)
        x2 = -u - b / (3 * a)
        # print("Three real roots, two are equal:")
        # print("x1 = ", x1.real)
        # print("x2 = ", x2.real)
        # print("x3 = ", x3.real)
    else:  # three distinct real roots
        u = (-q / 2 + cmath.sqrt(delta)) ** (1 / 3)
        v = (-q / 2 - cmath.sqrt(delta)) ** (1 / 3)
        x1 = u + v - b / (3 * a)
        x2 = -(u + v) / 2 - b / (3 * a) + (u - v) * cmath.sqrt(3) / 2j
        x3 = -(u + v) / 2 - b / (3 * a) - (u - v) * cmath.sqrt(3) / 2j
        # print("Three distinct real roots:")
        # print("x1 = ", x1.real)
        # print("x2 = ", x2.real)
        # print("x3 = ", x3.real)
    return x1


# Define the coefficients of the cubic equation ax^3+bx^2+cx+d
def calculateSage2(T):
    sg = W2 * pow(l, 2) / (8 * T)
    return sg


def calculateSage1(T):
    sg1 = W1 * pow(l, 2) / (8 * T)
    return sg1


def calculateT1():
    tension = UTS / fos1
    return tension


def calculateT2():
    tension = UTS / fos2
    return tension


def calculateG_min():
    return 17 + (V - 33) / 33


def calculateLpc(length):
    return 2 * d * p * length / 3


def calculateFc(tens):
    return 2 * tens * math.sin(math.radians(alpha / 2))


def calculateLpe(len):
    return 2 * De * p * len / 3


def calculateFe():
    Te = 18870 / 2
    return 2 * Te * math.sin(math.radians(alpha / 2))

    # def calculateFc()


print("####################################### ")
print("############   Table - 1  ############# ")
print("####################################### ")


while l <= 425:
    print("#########  For length : " + str(l) + "  ###########")
    print("#### Initial Condition(fos=2)")
    t1 = calculateT1()
    print(" T1:  " + str(t1))
    sg1 = calculateSage1(t1)
    print(" S1:  " + str(sg1))
    print("#### For 60 degree(fos=4)")
    t_2 = calculateT2()
    t2 = calculate(l, 60, t_2)
    print(" T2:  " + str(t2.real))
    sg2 = calculateSage2(t2.real)
    print(" S2:  " + str(sg2.real))
    print("#### For 30 degree (fos=4)")
    t3 = calculate(l, 30, t_2)
    print(" T3:  " + str(t3.real))
    sg3 = calculateSage2(t3.real)
    print(" S3:  " + str(sg3.real))

    ### Print H

    # print(" Wt : " + str(Wt))

    l = l + 25


print("####################################### ")
print("############   Table - 2  ############# ")
print("####################################### ")

G_min = calculateG_min()

print(" G_min(ft) :  " + str(G_min))
print(" G_min(m) :  " + str(G_min * 0.3048))

l = 250.0
while l <= 425:
    print("#########  For length : " + str(l) + "  ###########")
    t1 = calculateT1()
    sg1 = calculateSage1(t1)
    t_2 = calculateT2()
    t2 = calculate(l, 60, t_2)
    sg2 = calculateSage2(t2.real)
    t3 = calculate(l, 30, t_2)
    sg3 = calculateSage2(t3.real)
    G_min = calculateG_min()
    G_min = G_min * 0.3048
    H1 = G_min + sg2.real
    H2 = H1 + y
    H3 = H2 + y
    Ht = H3 + d_dash
    print(" Sag max:  " + str(sg2.real))
    print(" H1(m) :  " + str(H1))
    print(" H2(m) :  " + str(H2))
    print(" H3(m) :  " + str(H3))
    print(" Ht(m) :  " + str(Ht))
    print("#######################################")
    l = l + 25


print("####################################### ")
print("############   Table - 3  ############# ")
print("####################################### ")
l = 250.0
while l <= 425:
    print("#########  For length : " + str(l) + "  ###########")
    # print("#### Initial Condition")
    t1 = calculateT1()
    # print(" T1:  " + str(t1))
    sg1 = calculateSage1(t1)
    # print(" S1:  " + str(sg1))
    # print("#### For 60 degree")
    t_2 = calculateT2()
    t2 = calculate(l, 60, t_2)
    # print(" T2:  " + str(t2.real))
    sg2 = calculateSage2(t2.real)
    # print(" S2:  " + str(sg2.real))
    # print("#### For 30 degree ")
    t3 = calculate(l, 30, t_2)
    # print(" T3:  " + str(t3.real))
    sg3 = calculateSage2(t3.real)
    # print(" S3:  " + str(sg3.real))
    G_min = calculateG_min()
    # print(" G_min(ft) :  " + str(G_min))
    # print(" G_min(m) :  " + str(G_min * 0.3048))

    G_min = G_min * 0.3048
    H1 = G_min + sg2.real

    H2 = H1 + y
    H3 = H2 + y
    Ht = H3 + d_dash
    ### Print H

    # print("####################################### ")
    # print("############   Table - 1  ############# ")
    # print("####################################### ")
    # print(" Sag max:  " + str(sg2.real))
    # print(" H1(m) :  " + str(H1))
    # print(" H2(m) :  " + str(H2))
    # print(" H3(m) :  " + str(H3))
    # print(" Ht(m) :  " + str(Ht))
    #
    L_pc = calculateLpc(l)
    Fc = calculateFc(t1)
    Lpe = calculateLpe(l)
    Fe = calculateFe()
    M = (2.5 / 1000) * (Nc * (L_pc + Fc) * (H1 + H2 + H3) + Ne * Ht * (Lpe + Fe))
    # print(" M : " + str(M))
    K = 0.008
    Wt = K * Ht * math.sqrt(M)

    print(" Lpc : " + str(L_pc))
    print(" Lpe : " + str(Lpe))
    print(" M : " + str(M))
    print(" Wt : " + str(Wt))

    print("#######################################")
    l = l + 25
# calculate(l)
print("####################################### ")
print("############   Table - 4 Economic Consideration  ############# ")
print("####################################### ")
l = 250


minl = 0
minC = float("inf")
tlc = 0
while l <= 425:

    print("#########  For length : " + str(l) + "  ###########")
    t1 = calculateT1()
    sg1 = calculateSage1(t1)
    t_2 = calculateT2()
    t2 = calculate(l, 60, t_2)
    sg2 = calculateSage2(t2.real)
    t3 = calculate(l, 30, t_2)
    sg3 = calculateSage2(t3.real)
    G_min = calculateG_min()

    G_min = G_min * 0.3048
    H1 = G_min + sg2.real

    H2 = H1 + y
    H3 = H2 + y
    Ht = H3 + d_dash

    L_pc = calculateLpc(l)
    Fc = calculateFc(t1)
    Lpe = calculateLpe(l)
    Fe = calculateFe()
    M = (2.5 / 1000) * (Nc * (L_pc + Fc) * (H1 + H2 + H3) + Ne * Ht * (Lpe + Fe))
    K = 0.008
    Wt = K * Ht * math.sqrt(M)

    Ct = 98 * pow(10, 6) * Wt / l  # Rs/km
    print("Cost of Tower", Ct)

    Ci = 0.2 * Ct
    Ce = 0.1 * Ct

    print("Cost of Insulation", Ci)
    print("Cost of Erection", Ce)
    Cc = 3 * Nc * (8000 + (Cal * WtAl + Cst * WtSt))
    print("Cost of Conductor ", Cc)
    Cgs = 60
    Wtgs = 582.5
    Cce = 8000 + Cgs * Wtgs
    print("Cost of Earth Wire ", Cce)
    C = Ct + Ci + Ce + Cc + Cce
    print("Total Capital Cost", C)
    AFC = 0.15 * C
    print("Annual Fixed Cost ", AFC)
    R_at60 = R_at20 * (1 + 40 * Temp)
    Rph = R_at60 / Nc
    Iph_fullload = 210 * pow(10, 6) / (pow(3, 1 / 2) * 220 * 1000 * 0.96)
    Avg_power_loss = 0.4 * 3 * Iph_fullload * Iph_fullload * Rph / 1000

    ARC = Avg_power_loss * 24 * 365 * cost_of_energy
    print("Annual Running Cost ", ARC)
    total_annual_cost = AFC + ARC
    print("Total Annual Cost ", total_annual_cost)

    if C < minC:
        minC = C
        minl = l
        tlc = total_annual_cost
    print("#######################################")
    l = l + 25

print("#######################################")
print("#######################################")
print("Minimum cost at  ", minl)
print("Minimum Capital cost is ", minC)
print("TLC is ", tlc)
print("#######################################")
print("#######################################")
