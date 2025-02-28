clc; clear; close all;

L = 3;
alpha = 0.7;

n_samples = 10 * L;

h = zeros(1, n_samples);

h(1) = 1;

for n = 2:n_samples
    if n > L
        h(n) = alpha * h(n - L);
    end
end

% Plotar a resposta ao impulso
stem(0:n_samples-1, h, 'filled');
title('Resposta ao Impulso h[n]');
xlabel('n');
ylabel('h[n]');
grid on;