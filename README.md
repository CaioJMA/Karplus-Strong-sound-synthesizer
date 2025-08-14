# 🎸 Karplus Strong Sound Synthesizer

A síntese de áudio tem desempenhado um papel fundamental no desenvolvimento de instrumentos musicais eletrônicos e em diversas aplicações de processamento de sinal. Um dos métodos clássicos de síntese é o algoritmo de Karplus-Strong, introduzido nos anos 1980, que é notoriamente eficaz para a geração de sons semelhantes a instrumentos de cordas, como vioilões, guitarras, baixos e harpas. Este algoritmo combina conceitos de processamento digital de sinais com técnicas de retroalimentação e filtragem para produzir sons que são tanto agradáveis quanto realistas.

Este projeto implementa e analisa o **Algoritmo de Karplus-Strong**, envolvendo desde a formulação matemática até a geração de notas musicais específicas.

A equação de diferenças para o algoritmo de Karplus-Strong é derivada levando em conta que o sistema é composto por um gerador de ondas de curta duração \( \bar{x}[n] \) e um laço de realimentação com \( L \) unidades de atraso e um fator de ganho \( \alpha \).
