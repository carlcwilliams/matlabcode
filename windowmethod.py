import math as m

def fcN(Fpbe,Tw,Fstp,Fs,Wtype):
    if(Fstp!=0):
        Tw = Fstp-Fpbe
        fc = (Fpbe + Tw/2)/Fs
    else:
        fc = (Fpbe + Tw/2)/Fs
    print(fc)
    if (Wtype == "rect"):
        N=0.9/(Tw/Fs)
    if (Wtype == "han"):
        N=3.1/(Tw/Fs)
    if (Wtype == "ham"):
        N=3.3/(Tw/Fs)
    if (Wtype == "black"):
        N=5.5/(Tw/Fs)
    print(N)
    return fc, m.ceil(N)

def rectWF():
    return 1

def hanWF(n,N):
    return 0.5 + 0.5*m.cos(2*m.pi*n/N)

def hamWF(n,N):
    return 0.54 + 0.46*m.cos(2*m.pi*n/N)

def blackWF(n,N):
    return 0.42 + 0.5*m.cos((2*m.pi*n)/(N-1))+0.08*m.cos((4*m.pi*n)/(N-1))

def kaiserWF(n,N,B):
    self
    
#Fpbe - Passband edge frequency
#Tw - Transition width
#Fstp -Frequency Stop Band
#Fs - Sampling Frequency
#Wtype - rect, han, ham, black
def LPF(Fpbe,Tw,Fstp,Fs,Wtype):
    array_coeff=[]
    fc, Ns=fcN(Fpbe,Tw,Fstp,Fs,Wtype)
    wc = 2*m.pi*fc 
    N=m.ceil(Ns/2)
    hno=2*fc 
    for n in range(N):
        if (n==0):
            if (Wtype == "rect"):
                array_coeff.append(hno*rectWF())
            if (Wtype == "han"):
                array_coeff.append(hno*hanWF(n,Ns))
            if (Wtype == "ham"):
                array_coeff.append(hno*hamWF(n,Ns))    
            if (Wtype == "black"):
                array_coeff.append(hno*blackWF(n,Ns))
        else:
            hn=(2*fc*m.sin((n*wc))/(n*wc))
            if (Wtype == "rect"):
                array_coeff.append(hn * rectWF())
            if (Wtype == "han"):
                array_coeff.append(hn * hanWF(n,Ns))
            if (Wtype == "ham"):
                array_coeff.append(hn * hamWF(n,Ns))
            if (Wtype == "black"):
                array_coeff.append(hn * blackWF(n,Ns))
    complete_array_coeff=array_coeff[::-1]
    complete_array_coeff.extend(array_coeff[1::])
    return complete_array_coeff

#Fpbe - Passband edge frequency
#Tw - Transition width
#Fstp -Frequency Stop Band
#Fs - Sampling Frequency
#Wtype - rect, han, ham, black
def HPF(Fpbe,Tw,Fstp,Fs,Wtype):
    array_coeff=[]
    fc, Ns=fcN(Fpbe,Tw,Fstp,Fs,Wtype)
    wc = 2*m.pi*fc 
    N=m.ceil(Ns/2)
    hno = (1-2*fc)
    
    for n in range(N):
        if (n==0):
            if (Wtype == "rect"):
                array_coeff.append(hno*rectWF())
            if (Wtype == "han"):
                array_coeff.append(hno*hanWF(n,Ns))
            if (Wtype == "ham"):
                array_coeff.append(hno*hamWF(n,Ns))    
            if (Wtype == "black"):
                array_coeff.append(hno*blackWF(n,Ns))
        else:
            hn = (-2*fc*m.sin((n*wc))/(n*wc))
            if (Wtype == "rect"):
                array_coeff.append(hn * rectWF())
            if (Wtype == "han"):
                array_coeff.append(hn * hanWF(n,Ns))
            if (Wtype == "ham"):
                array_coeff.append(hn * hamWF(n,Ns))
            if (Wtype == "black"):
                array_coeff.append(hn * blackWF(n,Ns))
    complete_array_coeff=array_coeff[::-1]
    complete_array_coeff.extend(array_coeff[1::])
    return complete_array_coeff

#f1 - f1 edge frequency
#f2 - f2 edge frequency
#Tw - Transition width
#PBrip -Passband Ripple
#StBAtt - Stopband attenuation
#Fs - Sampling Frequency
#Wtype - rect, han, ham, black

def BPF(f1,f2,Tw,PBrip,StBAtt,Fs,Wtype):
    Dp = (10**(PBrip/20))-1
    Ds = 10**(StBAtt/-20)
    D = min(Dp,Ds)
    
    DF=Tw/Fs
    DF2=DF/2
    f1adj = f1/Fs + DF2
    f2adj = f2/Fs + DF2
    w1 = 2*m.pi*f1adj
    w2 = 2*m.pi*f2adj
    
    Ns = 0
    N = 0
    
    if (Wtype == "rect"):
        Ns = m.ceil(0.9/DF)
        N=m.ceil(Ns/2)  
    if (Wtype == "han"):
        Ns = m.ceil(3.1/DF)
        N=m.ceil(Ns/2)  
    if (Wtype == "ham"):
        Ns = m.ceil(3.3/DF)
        N=m.ceil(Ns/2)
    if (Wtype == "black"):
        Ns = m.ceil(5.5/DF)
        N=m.ceil(Ns/2)  
    
    array_coeff=[]
    hno = 2*(f2adj-f1adj)
      
    for n in range(N):
        if (n==0):
            if (Wtype == "rect"):
                array_coeff.append(hno * rectWF())
            if (Wtype == "han"):
                array_coeff.append(hno * hanWF(n,Ns))
            if (Wtype == "ham"):
                array_coeff.append(hno * hamWF(n,Ns))    
            if (Wtype == "black"):
                array_coeff.append(hno * blackWF(n,Ns))
        else:
            hn=(2*f2adj*m.sin((n*w2))/(n*w2)-(2*f1adj*m.sin((n*w1))/(n*w1)))
            if (Wtype == "rect"):
                array_coeff.append(hn * rectWF())
            if (Wtype == "han"):
                array_coeff.append(hn * hanWF(n,Ns))
            if (Wtype == "ham"):
                array_coeff.append(hn * hamWF(n,Ns))
            if (Wtype == "black"):
                array_coeff.append(hn * blackWF(n,Ns))
    complete_array_coeff=array_coeff[::-1]
    complete_array_coeff.extend(array_coeff[1::])
    return complete_array_coeff

#f1 - f1 edge frequency
#f2 - f2 edge frequency
#Tw - Transition width
#PBrip -Passband Ripple
#StBAtt - Stopband attenuation
#Fs - Sampling Frequency
#Wtype - rect, han, ham, black

def SBF(f1,f2,Tw,PBrip,StBAtt,Fs,Wtype):
    Dp = (10**(PBrip/20))-1
    Ds = 10**(StBAtt/-20)
    D = min(Dp,Ds)
    
    DF=Tw/Fs
    DF2=DF/2
    f1adj = f1/Fs + DF2
    f2adj = f2/Fs + DF2
    w1 = 2*m.pi*f1adj
    w2 = 2*m.pi*f2adj
    
    Ns = 0
    N = 0
    
    if (Wtype == "rect"):
        Ns = m.ceil(0.9/DF)
        N=m.ceil(Ns/2)  
    if (Wtype == "han"):
        Ns = m.ceil(3.1/DF)
        N=m.ceil(Ns/2)  
    if (Wtype == "ham"):
        Ns = m.ceil(3.3/DF)
        N=m.ceil(Ns/2)
    if (Wtype == "black"):
        Ns = m.ceil(5.5/DF)
        N=m.ceil(Ns/2)  
    
    array_coeff=[]
    hno = 1-2*(f2adj-f1adj)
        
    for n in range(N):
        if (n==0):
            if (Wtype == "rect"):
                array_coeff.append(hno*rectWF())
            if (Wtype == "han"):
                array_coeff.append(hno*hanWF(n,Ns))
            if (Wtype == "ham"):
                array_coeff.append(hno*hamWF(n,Ns))    
            if (Wtype == "black"):
                array_coeff.append(hno*blackWF(n,Ns))
        else:
            hn = (2*f1adj*m.sin((n*w1))/(n*w1)) - (2*f2adj*m.sin((n*w2))/(n*w2))
            if (Wtype == "rect"):
                array_coeff.append(hn * rectWF())
            if (Wtype == "han"):
                array_coeff.append(hn * hanWF(n,Ns))
            if (Wtype == "ham"):
                array_coeff.append(hn * hamWF(n,Ns))
            if (Wtype == "black"):
                array_coeff.append(hn * blackWF(n,Ns))
                                    
    complete_array_coeff=array_coeff[::-1]
    complete_array_coeff.extend(array_coeff[1::])
    return complete_array_coeff

#When using these functions please ensure that you are using the same frequency scale.

#Fpbe - Passband edge frequency
#Tw - Transition width
#Fstp -Frequency Stop Band
#Fs - Sampling Frequency
#Wtype - rect, han, ham, black
#LPF(Fpbe,Tw,Fstp,Fs,Wtype)
LPF(1.5,0.5,0,8,"ham")

#--------------------------------------------------
#f1 - f1 edge frequency
#f2 - f2 edge frequency
#Tw - Transition width
#PBrip -Passband Ripple
#StBAtt - Stopband attenuation
#Fs - Sampling Frequency
#Wtype - rect, han, ham, black
#BPF(f1,f2,Tw,PBrip,StBAtt,Fs,Wtype)
#BPF(10,20,1,0.1,60,100,"ham")

#------------------------------------------------
#f1 - f1 edge frequency
#f2 - f2 edge frequency
#Tw - Transition width
#PBrip -Passband Ripple
#StBAtt - Stopband attenuation
#Fs - Sampling Frequency
#Wtype - rect, han, ham, black
#SBF(f1,f2,Tw,PBrip,StBAtt,Fs,Wtype)
#SBF(10,20,1,0.1,60,100,"ham")
