🚀 Relatório Operacional de Pré-Decolagem (Aerospace Telemetry)

Atividade Integradora FIAP - Ciência da Computação

Sistema de simulação, análise e tomada de decisão preditiva baseado em dados de telemetria de voos aeroespaciais.

📋 Resumo do Projeto

Este projeto consiste em um ambiente analítico em Python para avaliar as condições de pré-decolagem de um veículo espacial. O sistema gera dados sintéticos de telemetria (temperatura, bateria, pressão e integridade de módulos), injeta anomalias simulando cenários de crise e processa um Algoritmo de Verificação para decidir automaticamente entre dois estados: READY (Pronto para Decolar) ou ABORT (Decolagem Abortada).

🛠️ Tecnologias Utilizadas

Python: Linguagem base para processamento de dados e lógica de decisão.

Pandas & NumPy: Geração de dados sintéticos, cálculos físicos (autonomia energética) e manipulação de DataFrames.

Matplotlib & Seaborn: Criação de dashboards analíticos, KDE plots, heatmaps de correlação e fluxogramas renderizados via código, seguindo a paleta de cores institucional.

📊 Principais Funcionalidades (Checklist de Entregas)

[x] 1.1 Organização da Telemetria: Definição de ranges seguros para sensores de temperatura, energia e pressão.

[x] 1.2 Algoritmo de Verificação: Fluxograma executivo programado nativamente em Matplotlib demonstrando a árvore de decisão (READY vs ABORT).

[x] 1.3 Script de Decisão: Pipeline completo de leitura de CSV e classificação de dados em tempo real.

[x] 1.4 Análise Energética: Cálculo físico preciso da autonomia da nave em minutos, considerando capacidade total, percentual de carga, consumo elétrico (kW) e taxa de perda energética.

[x] 1.5 Análise Assistida por IA: Diagnóstico textual dos cenários de crise, identificação de anomalias críticas (ex: sobrepressão de 215 bar) e sugestões de mitigação de riscos baseados nos dados.

🌍 1.6 Reflexão Crítica

Como parte da avaliação de impacto do projeto, refletimos sobre o papel da tecnologia no avanço da humanidade e as responsabilidades inerentes à engenharia de software de missão crítica.

⚖️ Ética e Responsabilidade

O desenvolvimento de sistemas de missão crítica, como algoritmos de pré-decolagem, exige rigor técnico e transparência inegociáveis. Um falso positivo (READY indevido) pode resultar na perda de vidas e de bilhões de dólares, enquanto um falso negativo (ABORT indevido) atrasa cronogramas científicos importantes. A responsabilidade da engenharia de software reside em não apenas criar lógicas de decisão, mas testá-las exaustivamente contra falhas de hardware, garantindo a integridade operacional absoluta antes de qualquer ignição.

🧑‍🚀 Impacto Social da Exploração Espacial

A exploração espacial deixou de ser um projeto puramente governamental para se tornar um catalisador de inovação global. Os retornos sociais são imensos, desde o desenvolvimento de novos materiais e tecnologias médicas até o monitoramento avançado do clima terrestre por satélites (essencial para a agricultura e prevenção de desastres). Popularizar e baratear o acesso ao espaço democratiza essa infraestrutura, trazendo benefícios diretos para o cotidiano de toda a sociedade.

♻️ Sustentabilidade Tecnológica

O futuro da presença humana no espaço depende da nossa capacidade de ser sustentável. A telemetria analisada neste projeto destaca o uso rigoroso de gestão de energia, monitorando perdas e autonomia. Estender essa visão significa projetar foguetes reutilizáveis, gerenciar de forma inteligente o lixo espacial (space debris) e otimizar fontes de energia renovável nos veículos e estações orbitais, garantindo que o avanço da fronteira espacial não repita os mesmos erros de exploração desmedida ocorridos na Terra.

🚀 Como Executar

Clone este repositório.

Abra o arquivo ATIVIDADE_INTEGRADORA_FIAP.ipynb no Jupyter Notebook ou Google Colab.

Execute as células sequencialmente.

Os datasets telemetry_baseline.csv e anomalous_telemetry_data.csv serão gerados automaticamente na primeira execução.

Desenvolvido pelo Grupo: Matheus dos Anjos, [Nome 2], [Nome 3].