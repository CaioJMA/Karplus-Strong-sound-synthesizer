clc; clear; close all;

fs = 48000;
duration = 2;
L = 100;
n_samples = duration * fs;
n = 0:L-1;

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

% Tocar os sinais para os diferentes casos

play_sound(x_a, alpha_a, L, fs, n_samples);
pause(duration + 1);

play_sound(x_b, alpha_b, L, fs, n_samples);
pause(duration + 1);

play_sound(x_c, alpha_c, L, fs, n_samples);
pause(duration + 1);

play_sound(x_d, alpha_d, L, fs, n_samples);
pause(duration + 1);

function play_sound(x, alpha, L, fs, n_samples)

    y = zeros(1, n_samples);
    y(1:L) = x;

    for i = L+1:n_samples

        y(i) = alpha * y(i - L);

    end
    
    soundsc(y, fs);

end