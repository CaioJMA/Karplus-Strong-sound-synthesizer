# 🎸 Karplus Strong Sound Synthesizer

<p align="justify">
A síntese de áudio tem desempenhado um papel fundamental no desenvolvimento de instrumentos musicais eletrônicos e em diversas aplicações de processamento de sinal. Um dos métodos clássicos de síntese é o algoritmo de Karplus-Strong, introduzido nos anos 1980, que é notoriamente eficaz para a geração de sons semelhantes a instrumentos de cordas, como vioilões, guitarras, baixos e harpas. Este algoritmo combina conceitos de processamento digital de sinais com técnicas de retroalimentação e filtragem para produzir sons que são tanto agradáveis quanto realistas.
</p>
<p align="justify">
Este projeto implementa e analisa o Algoritmo de Karplus-Strong, envolvendo desde a formulação matemática até a geração de notas musicais específicas.
</p>

# Equações de Diferenças

<p align="justify">
A equação de diferenças para o algoritmo de Karplus-Strong é derivada levando em conta que o sistema é composto por um gerador de ondas de curta duração e um laço de realimentação com $$"L"$$ unidades de atraso e um fator de ganho $$α$$.
</p>
<p align="justify">
O algoritmo Karplus-Strong pode ser descrito em termos de uma equação de diferenças que leva em conta um filtro de atraso (com atraso de $$"L"$$ amostras) e uma multiplicação por um ganho $$α$$. A saída $$y[n]$$ em um dado instante $$"n"$$ depende da entrada $$x[n]$$ e da saída em instantes anteriores.
</p>
<p align="justify">
A equação de diferenças para $$y[n]$$ pode ser dada por:
</p>

$$
y[n] = x[n] + \alpha \cdot y[n - L]
$$

<p align="justify">
O sinal de saída $$y[n]$$ é dado por:
</p>

$$
y[n] =
\begin{cases}
\bar{x}[n], & \text{para } 0 \leq n < L \\
\alpha \ \cdot y[n - L], & \text{para } n \geq L
\end{cases}
$$

<p align="justify">
Neste contexto, $$\bar{x}[n]$$ representa o sinal de entrada de suporte finito (duração $$"L"$$) e $$α$$ controla o decaimento do sinal no laço de realimentação. Quando $$α = 1$$, o sinal se repete indefinidamente, enquanto valores de $$α < 1$$ resultam em um decaimento exponencial do sinal ao longo do tempo.
</p>

# Síntese de Sinais

<p align="justify">
Através do código MATLAB *"SintetizarSinais"*, obteve-se os sinais de uma Senoide, Triangular, Quadrada e Aleatória (com Distribuição Normal e Desvio Padrão igual a 1) com $$L = 100$$ amostras e 10 períodos. Enquanto que através do código MATLAB $$“TocarSinais”$$, é possível tocar os sinais sintetizados.
</p>

# Gerador de Tons e Escala Diatônica de Dó

<p align="justify">
Através do código MATLAB $$"SinaisAleatorios"$$, obteve-se diferentes gráficos de Forma de Onda das notas Dó, Ré, Mi, Fá, Sol, Lá, Si dentro da base de Lá (220 Hz) simulando o efeito de cordas através da estimulação por um sinal aleatório. O sinal aleatório inicial desempenha um papel crucial no método de Karplus-Strong, que é amplamente utilizado para a síntese de sons de cordas em processamento digital de sinais. Este método simula a vibração de uma corda vibrante ao utilizar um filtro digital baseado em um buffer de amostras. O sinal aleatório inicial, frequentemente gerado a partir de uma sequência de valores aleatórios, é essencial porque representa a excitação inicial da corda, que imita as vibrações complexas e desordenadas que ocorrem quando uma corda é percutida ou dedilhada. Dessa forma, através do código MATLAB $$"EscalaDiatonicaDo"$$, é possível tocar os sinais das notas da Escala Diatônica de Dó Maior na 3ª Oitava.
</p>

# Análises Extras

