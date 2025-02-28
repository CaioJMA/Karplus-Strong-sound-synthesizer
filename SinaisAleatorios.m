clc; clear; close all;

FO = 220; % Base de Lá
volume = 1;
mudanca_pitch = 2;
decaimento_onda = 0.0001;

loop(FO, volume, mudanca_pitch, decaimento_onda)

function loop(FO, volume, pitch_shift, decay_factor)

    Notas_n = {'LA','SI','DO','RE','MI','FA','SOL', 'SILENCIO'};
    Equivalente_n = [0 2 3 5 7 8 10 91];
    Mapeamento = containers.Map(Notas_n, Equivalente_n);

    notas = {'DO','RE','MI', 'FA', 'SOL', 'LA', 'SI'};

    fs = 48000;  % Frequência de amostragem

    D = 1.5; % Duração da nota

    figure; % Cria uma nova figura para os gráficos

    for i = 1:length(notas)

        nota_entero = cell2mat(values(Mapeamento, notas(i)));

        Y = nota(D, fs, FO, nota_entero, volume, pitch_shift, decay_factor);
        
        subplot(length(notas), 1, i);
        t = (0:length(Y)-1) / fs;
        plot(t, Y);
        xlabel('Time (s)');
        ylabel('Amplitude');
        title(['Forma de Onda da Nota ', notas{i}]);
    end
end

function Y = nota(D, fs, FO, nota_entero, volume, pitch_shift, decay_factor)

    Fo = FO * 2^((nota_entero + pitch_shift) / 12);

    T = floor(fs / Fo);

    x = (pi/2) * rand(T, 1) - 1; % Sinal inicial aleatório

    x = x * volume; % Ajuste de volume

    N = D * fs; % Número de amostras

    Y = zeros(N, 1);
    Y(1:T) = x;

    Y = tom(Y, N, T, fs, decay_factor);
end

function Y = tom(Y, N, T, fs, decay_factor)

    for i = 1:N-T - 1
        Y(i + T) = (Y(i) + Y(i + 1)) / (2 + decay_factor);
    end
    
    sound(Y, fs);
    pause(0.3);
end