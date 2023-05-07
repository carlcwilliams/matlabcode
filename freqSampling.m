%Test Program for Frequency Sampled Filter
freqHz1 = 1000;
freqHz2 = 2000;
freqHz3 = 4000;
freqHz4 = 7000;
freqHz5 = 10000;
fsHz = 18000;
dt = 1/fsHz;
t = 0:dt:1-dt;
s1 = 1 * sin(2*pi*freqHz1*t);
s2 = 1 * sin(2*pi*freqHz2*t);
s3 = 1 * sin(2*pi*freqHz3*t);
s4 = 1 * sin(2*pi*freqHz4*t);
s5 = 1 * sin(2*pi*freqHz5*t);
stot=s1+s2+s3+s4+s5;

N = 18000;
transform = fft(stot,N)/N;
magTransform = abs(transform);

faxis = linspace(-fsHz/2,fsHz/2,N);
subplot(2,1,1)
plot(faxis/1000,fftshift(magTransform));
axis([-10 10 0 1])
ylabel('Magnitude'); title('(a) before filtering');
xlabel('Frequency (KHz)')

%h[n] coefficients with different values and lengths... last three relate
%to 1,2,3 transisition values.
%hn=[0.07252262718512655, -0.11111111111111116, -0.059120987359772864, 0.3199316935079797, 0.5555555555555556, 0.3199316935079797, -0.059120987359772864, -0.11111111111111116, 0.07252262718512655]
hn=[-0.05555555555555555, 0.0192942419629923, 0.04528930383866127, -0.05555555555555566, -0.012593422050315514, 0.08511604923544196, -0.05555555555555563, -0.10441029119843422, 0.30063745154498744, 0.6111111111111112, 0.30063745154498744, -0.10441029119843422, -0.05555555555555563, 0.08511604923544196, -0.012593422050315514, -0.05555555555555566, 0.04528930383866127, 0.0192942419629923];
%hn=[0.0074444444444444445, 0.008354406769975663, -0.013911331270850955, -0.02405555555555556, 0.03566737786618012, 0.03685524931894633, -0.0870555555555556, -0.045209656088921996, 0.311577286738004, 0.5481111111111111, 0.311577286738004, -0.045209656088921996, -0.0870555555555556, 0.03685524931894633, 0.03566737786618012, -0.02405555555555556, -0.013911331270850955, 0.008354406769975663];
%hn=[0.005777777777777777, 0.006794493406199815, -0.009853585385087639, -0.022055555555555557, 0.027216385283307602, 0.03963957523515218, -0.07772222222222228, -0.054934068641352, 0.30747053343511316, 0.5611111111111111, 0.30747053343511316, -0.054934068641352, -0.07772222222222228, 0.03963957523515218, 0.027216385283307602, -0.022055555555555557, -0.009853585385087639, 0.006794493406199815];
%hn=[-0.0020000000000000018, 0.004243840937612635, 0.0022209513750456444, -0.018555555555555596, 0.005202307165698232, 0.04687587557498375, -0.051666666666666736, -0.08178638317926307, 0.2952434081259226, 0.5984444444444444, 0.2952434081259226, -0.08178638317926307, -0.051666666666666736, 0.04687587557498375, 0.005202307165698232, -0.018555555555555596, 0.0022209513750456444, 0.004243840937612635]
yn=conv(hn,s)
transform = fft(yn,N)/N;
magTransform = abs(transform);

faxis = linspace(-fsHz/2,fsHz/2,N);
subplot(2,1,2)
plot(faxis/1000,fftshift(magTransform));
axis([-10 10 0 1])
ylabel('Magnitude'); title('(b) after filtering');
xlabel('Frequency (KHz)')

%freq sweep
frqaxis=-pi:(pi/N):pi;
FreqResp=freqz(hn,1,frqaxis);
figure;plot(frqaxis,abs(FreqResp));
axis([-pi pi 0 2])
ylabel('Magnitude'); title('frequency response');
xlabel('Frequency (-pi to pi)')
