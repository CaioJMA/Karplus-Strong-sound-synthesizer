clc; clear; close all;

L = 3;
alpha = 0.7;

fs = 1000;

numerator = 1;
denominator = [1, zeros(1, L-1), -alpha];
H = tf(numerator, denominator, 1/fs);


omega = linspace(0, pi, 1024);
f = omega * fs / (2*pi);

[H_freq, w] = freqz(numerator, denominator, 1024, fs);


figure;
subplot(2,1,1);
plot(f, abs(H_freq));
title('Resposta de Magnitude |H(e^{j\omega})|');
xlabel('Frequência (kHz)');
ylabel('|H(e^{j\omega})|');
grid on;


subplot(2,1,2);
plot(f, angle(H_freq));
title('Resposta de Fase θ(e^{j\omega})');
xlabel('Frequência (kHz)');
ylabel('Fase (radianos)');
grid on;

figure;
zplane(numerator, denominator);
title('Diagrama de Polos e Zeros');
grid on;
