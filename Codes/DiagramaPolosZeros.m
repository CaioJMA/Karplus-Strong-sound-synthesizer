clc; clear; close all;

L = 3;
alpha_vec = [1, 3];

figure;

for i = 1:length(alpha_vec)

    alpha = alpha_vec(i);
   
    numerator = 1;
    denominator = [1, zeros(1, L-1), -alpha];
    
    subplot(1, length(alpha_vec), i);
    zplane(numerator, denominator);
    title(['Diagrama de Polos e Zeros para \alpha = ', num2str(alpha)]);
    grid on;
    
end