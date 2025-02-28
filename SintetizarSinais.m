clc; clear; close all;

L = 100;
n_samples = 10 * L;
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

plot_response(x_a, alpha_a, L, n_samples, 'Senoide');
plot_response(x_b, alpha_b, L, n_samples, 'Triangular');
plot_response(x_c, alpha_c, L, n_samples, 'Quadrada');
plot_response(x_d, alpha_d, L, n_samples, 'Aleatória');

function plot_response(x, alpha, L, n_samples, plot_title)

    y = zeros(1, n_samples);
    y(1:L) = x;

    for i = L+1:n_samples

        y(i) = alpha * y(i - L);

    end
    
    figure;
    stem(0:n_samples-1, y, 'filled');
    title(['Resposta ao Impulso: ', plot_title]);
    xlabel('n');
    ylabel('y[n]');
    grid on;

end