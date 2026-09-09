<!-- HEADER E BANNER -->
<div align="center">
  <img width="2754" height="921" alt="m" src="https://github.com/user-attachments/assets/515f391f-7260-4149-aa2a-9dc7faaad866" />

  <br>

  <h1>Relatório Operacional de Pré-Decolagem<br><sub>(Aerospace Telemetry)</sub></h1>

  **Atividade Integradora FIAP - Ciência da Computação**

  *Sistema de simulação, análise e tomada de decisão baseado em dados de telemetria.*


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

>  **Objetivo:** Este projeto consiste em um ambiente analítico desenvolvido em Python para avaliar as condições rigorosas de pré-decolagem de um veículo espacial. O sistema engloba desde a geração de dados sintéticos até a tomada de decisão autônoma.

O pipeline de dados gera telemetria (temperatura, bateria, pressão), injeta anomalias simulando cenários de crise e processa um **Algoritmo de Verificação** para decidir automaticamente entre dois estados críticos:

- 🟢 `READY` (Pronto para Decolar)
- 🔴 `ABORT` (Decolagem Abortada)

<hr>

##  Tecnologias Utilizadas

| Tecnologia | Função no Projeto |
| :---: | :--- |
| 🐍 **Python** | Linguagem base para o processamento lógico de dados e regras de decisão. |
| 📊 **Pandas & NumPy** | Geração de dados sintéticos, cálculos físicos e manipulação de *DataFrames*. |
| 📈 **Matplotlib & Seaborn** | Criação de dashboards analíticos, *heatmaps* de correlação e fluxograma. |

<hr>

##  Principais Funcionalidades

Abaixo está o checklist de entregas integradas ao ambiente do projeto:

- [x] **1.1 Organização da Telemetria:** Definição de *ranges* seguros para sensores de temperatura, energia e pressão.
- [x] **1.2 Algoritmo de Verificação:** Fluxograma programado nativamente em Matplotlib demonstrando a árvore de decisão (`READY` vs `ABORT`).
- [x] **1.3 Script de Decisão:** Pipeline completo de leitura de CSV e classificação de dados.
- [x] **1.4 Análise Energética:** Capacidade total, percentual de carga, consumo elétrico (kW) e taxa de perda energética.
- [x] **1.5 Análise Assistida por IA:** Diagnóstico textual dos cenários de crise, identificação de anomalias críticas e sugestões de mitigação de riscos.

<hr>

##  Prints da Apresentação do Projeto
<img width="1056" height="453" alt="Captura de tela 2026-09-08 184623" src="https://github.com/user-attachments/assets/447d269f-c23a-480b-ad5f-145c76b26cab" />
<img width="1050" height="445" alt="Captura de tela 2026-09-08 184641" src="https://github.com/user-attachments/assets/854e6608-fd5e-4cd2-ad8a-fc0fdecd951b" />
<img width="1057" height="502" alt="Captura de tela 2026-09-08 184602" src="https://github.com/user-attachments/assets/b1b6d814-8f69-4e33-a542-61edfa23cabe" />
<img width="1028" height="361" alt="Captura de tela 2026-09-08 184613" src="https://github.com/user-attachments/assets/323078c5-cbf3-4903-bf20-08a1a1e2c009" />
<img width="1042" height="584" alt="Captura de tela 2026-09-08 185448" src="https://github.com/user-attachments/assets/f7be2a9c-c707-4e06-80cc-7305ce933750" />

<hr>

## RESUMO Reflexão Crítica & Impacto

Como parte da avaliação de impacto do projeto, refletimos sobre o papel da tecnologia no avanço da humanidade e as responsabilidades inerentes à engenharia de software de missão crítica. 

*Clique nas seções abaixo para expandir e ler as análises:*

<details>
  <summary><b> Ética e Responsabilidade</b></summary>
  <br>
  O desenvolvimento de sistemas, como algoritmos de pré-decolagem, exige rigor técnico e transparência. Um falso positivo (<code>READY</code>) pode resultar na perda de vidas, sem contar no impacto ambiental na queda dos destroços. Um falso negativo (<code>ABORT</code>) atrasa cronogramas científicos importantes e perde investimentos que podem mudar o nosso futuro. A responsabilidade da engenharia de software reside em não apenas criar lógicas de decisão, mas testá-las exaustivamente contra falhas, garantindo a integridade operacional absoluta.
</details>

<details>
  <summary><b> Impacto Social da Exploração Espacial</b></summary>
  <br>
  A exploração espacial deixou de ser um projeto puramente governamental para se tornar um catalisador de inovação global. Os retornos sociais são imensos, desde o desenvolvimento de novos materiais e tecnologias médicas até o monitoramento avançado do clima terrestre por satélites (essencial para a agricultura e prevenção de desastres). Popularizar e baratear o acesso ao espaço democratiza essa infraestrutura, trazendo benefícios diretos para o cotidiano de toda a sociedade.
</details>

<details>
  <summary><b> Sustentabilidade Tecnológica</b></summary>
  <br>
  O futuro da presença humana no espaço depende da nossa capacidade de ser sustentável. A telemetria analisada neste projeto destaca o uso rigoroso de gestão de energia, monitorando perdas e autonomia. Estender essa visão significa projetar foguetes reutilizáveis, gerenciar de forma inteligente e otimizar fontes de energia renovável nos veículos e estações orbitais, garantindo que o avanço espacial não repita os mesmos erros de exploração desmedida ocorridos na Terra.
</details>

<hr>

##  Como Executar

Siga o passo a passo abaixo para configurar e executar o ambiente de simulação. Clique nas seções para expandir as instruções detalhadas:

<details>
  <summary><b>💻 1. Clone o repositório</b></summary>
  <br>
  Abra o seu terminal (ou Prompt de Comando) e execute os comandos abaixo para baixar o projeto para a sua máquina local e acessar a pasta principal:

```bash
  git clone https://github.com/mt076/Graduacao_FIAP.git
```
<details>
  <summary><b>⚙️ 0. Pré-requisitos</b></summary>
  <br>
  Antes de iniciar, certifique-se de ter instalado em sua máquina:
  <ul>
    <li><a href="https://git-scm.com/">Git</a> (para clonar o repositório)</li>
    <li><a href="https://www.python.org/downloads/">Python 3.8+</a> (caso deseje rodar o projeto localmente)</li>
    <li>Uma conta Google ativa e abra o arquivo no Colab (caso prefira utilizar o ambiente na nuvem do Google)</li>
  </ul>
</details>
