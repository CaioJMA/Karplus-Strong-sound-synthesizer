clc; clear; close all;

FO = 262; % C3

loop(FO)

function loop(~)

    Notas_n = {'DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI'};
    
    Frequencias_n = [262, 294, 330, 350, 392, 440, 494];

    Pentagrama = containers.Map(Notas_n, Frequencias_n);

    fs = 48000; % Frequência de amostragem
    D = 1; % Duração da nota

    for i = 1:length(Notas_n)

        freq_nota = cell2mat((values(Pentagrama, Notas_n(i))));
        
        Y = nota(D, fs, freq_nota);
        
        figure;

        subplot(2, 1, 1);
        t = (0:length(Y) - 1) / fs;
        plot(t, Y);
        xlabel('Time (s)');
        ylabel('Amplitude');
        title(['Forma de onda da nota ', Notas_n{i}]);

        subplot(2, 1, 2);
        plot_spectro(Y, fs, Notas_n{i});

    end
end

function Y = nota(D, fs, Fo)

    T = floor(fs / Fo);

    x = (pi / 2) * rand(T, 1) - 1; % Sinal inicial aleatório

    N = D * fs; % Número de amostras

    Y = zeros(N, 1);
    Y(1:T) = x;

    Y = tom(Y, N, T);

    sound(Y, fs);
    
    pause(0.3);
end

function Y = tom(Y, N, T)
  
    for i = 1:N - T

        Y(i + T) = (Y(i) + Y(i + 1)) / 2.01;

    end
end

function plot_spectro(Y, fs, nota_name)
    
    Y_fft = fft(Y);
    N = length(Y);
    f = (0:N - 1) * (fs / N) / 1000;
    Y_magnitude = abs(Y_fft)/N;

    plot(f, Y_magnitude);
    xlabel('Frequency (kHz)');
    ylabel('Magnitude');
    title(['Espectro de Magnitude da Nota ', nota_name]);
end
