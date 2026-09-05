<!-- HEADER E BANNER -->
<div align="center">
  <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop" width="100%" height="250" style="object-fit: cover; border-radius: 10px;" alt="Aerospace Banner">

  <br>

  <h1>Relatório Operacional de Pré-Decolagem<br><sub>(Aerospace Telemetry)</sub></h1>

  **Atividade Integradora FIAP - Ciência da Computação**

  *Sistema de simulação, análise e tomada de decisão preditiva baseado em dados de telemetria de voos aeroespaciais.*

  <br>

  <!-- BADGES DE TECNOLOGIA -->
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="Matplotlib">
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
</div>

<hr>

##  Resumo do Projeto

>  **Objetivo:** Este projeto consiste em um ambiente analítico robusto desenvolvido em Python para avaliar as condições rigorosas de pré-decolagem de um veículo espacial. O sistema engloba desde a geração de dados sintéticos até a tomada de decisão autônoma.

O pipeline de dados gera telemetria (temperatura, bateria, pressão e integridade de módulos), injeta anomalias simulando cenários de crise e processa um **Algoritmo de Verificação** para decidir automaticamente entre dois estados críticos:

- 🟢 `READY` (Pronto para Decolar)
- 🔴 `ABORT` (Decolagem Abortada)

<hr>

##  Tecnologias Utilizadas

Para garantir a precisão matemática e a clareza analítica do sistema de telemetria, as seguintes bibliotecas foram empregadas:

| Tecnologia | Função no Projeto |
| :---: | :--- |
| 🐍 **Python** | Linguagem base para o processamento lógico de dados e regras de decisão. |
| 📊 **Pandas & NumPy** | Geração de dados sintéticos, cálculos físicos (ex: autonomia energética) e manipulação de *DataFrames*. |
| 📈 **Matplotlib & Seaborn** | Criação de dashboards analíticos, *KDE plots*, *heatmaps* de correlação e fluxogramas renderizados diretamente via código. |

<hr>

##  Principais Funcionalidades

Abaixo está o checklist de entregas integradas ao ambiente do projeto:

- [x] **1.1 Organização da Telemetria:** Definição de *ranges* seguros para sensores de temperatura, energia e pressão.
- [x] **1.2 Algoritmo de Verificação:** Fluxograma executivo programado nativamente em Matplotlib demonstrando a árvore de decisão (`READY` vs `ABORT`).
- [x] **1.3 Script de Decisão:** Pipeline completo de leitura de CSV e classificação de dados em tempo real.
- [x] **1.4 Análise Energética:** Cálculo físico preciso da autonomia da nave em minutos, considerando capacidade total, percentual de carga, consumo elétrico (kW) e taxa de perda energética.
- [x] **1.5 Análise Assistida por IA:** Diagnóstico textual dos cenários de crise, identificação de anomalias críticas (ex: *sobrepressão de 215 bar*) e sugestões de mitigação de riscos.

<hr>

##  Reflexão Crítica & Impacto

Como parte da avaliação de impacto do projeto, refletimos sobre o papel da tecnologia no avanço da humanidade e as responsabilidades inerentes à engenharia de software de missão crítica. 

*Clique nas seções abaixo para expandir e ler as análises:*

<details>
  <summary><b> Ética e Responsabilidade</b></summary>
  <br>
  O desenvolvimento de sistemas de missão crítica, como algoritmos de pré-decolagem, exige rigor técnico e transparência inegociáveis. Um falso positivo (<code>READY</code> indevido) pode resultar na perda de vidas e de bilhões de dólares, enquanto um falso negativo (<code>ABORT</code> indevido) atrasa cronogramas científicos importantes. A responsabilidade da engenharia de software reside em não apenas criar lógicas de decisão, mas testá-las exaustivamente contra falhas de hardware, garantindo a integridade operacional absoluta antes de qualquer ignição.
</details>

<details>
  <summary><b> Impacto Social da Exploração Espacial</b></summary>
  <br>
  A exploração espacial deixou de ser um projeto puramente governamental para se tornar um catalisador de inovação global. Os retornos sociais são imensos, desde o desenvolvimento de novos materiais e tecnologias médicas até o monitoramento avançado do clima terrestre por satélites (essencial para a agricultura e prevenção de desastres). Popularizar e baratear o acesso ao espaço democratiza essa infraestrutura, trazendo benefícios diretos para o cotidiano de toda a sociedade.
</details>

<details>
  <summary><b> Sustentabilidade Tecnológica</b></summary>
  <br>
  O futuro da presença humana no espaço depende da nossa capacidade de ser sustentável. A telemetria analisada neste projeto destaca o uso rigoroso de gestão de energia, monitorando perdas e autonomia. Estender essa visão significa projetar foguetes reutilizáveis, gerenciar de forma inteligente o lixo espacial (<i>space debris</i>) e otimizar fontes de energia renovável nos veículos e estações orbitais, garantindo que o avanço da fronteira espacial não repita os mesmos erros de exploração desmedida ocorridos na Terra.
</details>

<hr>

##  Como Executar

Siga os passos abaixo para rodar o ambiente de simulação na sua máquina:

**1. Clone o repositório:**
```bash
EM ANDAMENTO
