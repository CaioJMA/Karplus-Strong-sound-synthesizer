clc; clear; close all;

fs = 48000;
duration = 2;
L = 100;
n_samples = duration * fs;
n = 0:L - 1;

% a) Senoide

alpha_a = 0.995;
x_a = sin(2 * pi * n / L);

% b) Triangular

alpha_b = 1.0;
x_b = (2 * n / L) - 1;

% c) Quadrada

alpha_c = 0.95;
x_c = [ones(1, L/2), -ones(1, L/2)];

% d) Aleatória com distribuição normal

alpha_d = 0.995;
x_d = randn(1, L);  % Distribuição normal com desvio padrão 1

y_a = generate_signal(x_a, alpha_a, L, fs, n_samples);
pause(duration + 1);
plot_spectrum(y_a, fs);

y_b = generate_signal(x_b, alpha_b, L, fs, n_samples);
pause(duration + 1);
plot_spectrum(y_b, fs);

y_c = generate_signal(x_c, alpha_c, L, fs, n_samples);
pause(duration + 1);
plot_spectrum(y_c, fs);

y_d = generate_signal(x_d, alpha_d, L, fs, n_samples);
pause(duration + 1);
plot_spectrum(y_d, fs);

function y = generate_signal(x, alpha, L, fs, n_samples)

    y = zeros(1, n_samples);
    y(1:L) = x;

    for i = L+1:n_samples

        y(i) = alpha * y(i - L);

    end
    
    soundsc(y, fs);

end

function plot_spectrum(y, fs)

    Y = fft(y);
    N = length(Y);
    f = (0:N - 1) * (fs / N) / 1000;
    magnitude = abs(Y);
    phase = angle(Y);
    
    figure;
    subplot(2, 1, 1);
    plot(f, magnitude);
    title('Espectro de Magnitude |Y(e^{j\omega})|');
    xlabel('Frequência (kHz)');
    ylabel('|Y(e^{j\omega})|');
    grid on;
    
    subplot(2, 1, 2);
    plot(f, phase);
    title('Espectro de Fase \theta(e^{j\omega})');
    xlabel('Frequência (kHz)');
    ylabel('\theta(e^{j\omega}) (rad)');
    grid on;

end