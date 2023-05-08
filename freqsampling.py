import math as m

def FSMCoeff(N, H):
    coeff_vec=[]
    alpha = m.ceil((N-1)/2)
    kul = 0
    if ((N%2) == 0):
        kul = m.ceil(N/2-1)
    else:
        kul = m.ceil((N-1)/2)
    Ht=0
    for n in range(N):
        for k in range(1,kul):
            Ht +=2*H[k]*m.cos(abs(2*m.pi*k*(n-alpha)/N))
        coeff_vec.append((Ht+H[0])/N)        
        Ht=0
    print(coeff_vec)

#H(k) is defined below... for the filter
#eg below cut off is at 5Khz, but resolution is 2Khz... so last value 1 is at 4HKz and 0 is at 6Khz...
#    H(0)->0KHz,H(1)->2KHz,H(2)->4KHz,H(3)->6KHz,H(4)->8KHz
#H = [1,1,1,0,0] for N=9, N/2 -> 4.5 roundup ->5.. therefore 5 placements for H(k) array.
#FSMCoeff(N,H)
Fs = 18 #Hz
N = 9 #Number of samples in one wavelenth 2pi
FperS=Fs/N
print("Frequency per sample point: ",FperS,"Hz")
H = H = [1,1,1,0]
FSMCoeff(N,H)
