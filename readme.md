# MSFS State Modifier

**MSFS State Modifier** é uma ferramenta para MSFS2020 que introduz variações aleatórias no estado Cold & Dark das aeronaves PMDG 737, tornando cada início de voo mais realista e imprevisível.

---

## ✈️ Objetivo

Embora o MSFS2020 já carregue o PMDG 737 no estado Cold & Dark, todos os botões, chaves e sistemas sempre iniciam nas mesmas posições. Isso tira parte da imersão e da sensação de continuidade entre voos.

O objetivo do MSFS State Modifier é manter o estado geral Cold & Dark, mas com variações aleatórias e realistas em alguns botões e sistemas, como se a tripulação anterior ou uma equipe de manutenção tivesse deixado algo fora do lugar. Isso simula de forma mais autêntica o ambiente operacional de um avião real, exigindo atenção extra do piloto durante a preparação do cockpit.

---

## ⚙️ Funcionalidades

- ✅ Suporte ao PMDG 737-800 (e futuramente outros modelos)
- 🎲 Randomização automática dos estados da aeronave
- 🧠 Lógica baseada em **probabilidades encadeadas** para decidir quantos botões serão alterados
- 🧾 Níveis de realismo configuráveis via JSON:
  - *Casual* – leve, ideal para iniciantes
  - *Natural* – simula esquecimentos plausíveis da tripulação
  - *Avançado* – exige atenção redobrada
  - *Caótico* – variação intensa, como se tudo tivesse sido deixado errado
- 📁 Arquivo único de configuração (`config.json`)
- 🛫 Ativação automática ao iniciar o MSFS
- 🔄 Aplicação automática de modificações ao retornar ao menu principal
- 🚪 Encerramento automático junto com o simulador
- 🧼 Limpeza de logs ao final de cada voo
- 📦 Instalação automatizada com configuração de diretórios
- 👻 Execução em segundo plano, sem janelas ou interferência visual
- 🖼️ Interface em bandeja com botão de "Randomizar Agora" (versão mínima)

---

## 🛠️ Instalação

O instalador `Setup_MSFS_State_Modifier.exe` configura automaticamente:

1. O caminho da pasta de estados do PMDG 737-800
2. A pasta onde os arquivos modificados serão salvos
3. Um atalho para iniciar junto com o MSFS2020
4. Um serviço oculto que monitora o simulador e aplica os estados automaticamente

---

## 🧪 Como usar

1. Instale o programa normalmente.
2. Inicie o Microsoft Flight Simulator.
3. O sistema detectará automaticamente o momento ideal para aplicar as alterações.
4. O estado Cold & Dark será carregado com variações aleatórias realistas.

---

## ⚙️ Personalização

Se quiser ajustar os **níveis de realismo**, abra o arquivo `config.json` (localizado em `%LOCALAPPDATA%\MSFSStateModifier`) e altere o valor da chave `"selected_profile"` para um dos seguintes:

- `"casual"`
- `"natural"`
- `"avancado"`
- `"caotico"`

Cada perfil contém um conjunto de probabilidades que determinam a quantidade de alterações realizadas em cada voo.

---

## 🚧 Em desenvolvimento

- Suporte a outros modelos da família PMDG 737
- Interface gráfica completa com histórico e controles
- Integração com clima real ou aeroporto de origem
- Randomização com base em condições externas
- Checklists integrados para Cold & Dark

---

## 📜 Licença

Este projeto é de uso pessoal e não possui fins comerciais. Todo o conteúdo do simulador e das aeronaves utilizadas pertence a seus respectivos desenvolvedores (Microsoft, Asobo, PMDG).

---

## 🙏 Agradecimentos

A todos os desenvolvedores de conteúdo para MSFS, especialmente os criadores da SDK SimConnect e da comunidade de entusiastas da aviação virtual.

---

> “Tudo o que fizerdes, fazei-o de todo o coração, como para o Senhor e não para os homens.” (Colossenses 3,23)
