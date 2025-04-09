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
- 📁 Perfis personalizáveis via arquivos `.json`
- 🛫 Ativação automática ao iniciar o MSFS
- 🧠 Lógica para detectar quando o simulador está no menu, carregando ou em voo
- 🗂️ Instalação automatizada via Inno Setup
- 🔧 Compatível com execução automática junto ao Windows
- 🧾 Geração de logs e histórico de randomizações

---

## 🛠️ Instalação

O instalador `Setup_MSFS_State_Modifier.exe` configura automaticamente:

1. O caminho da pasta de estados do PMDG 737-800
2. A pasta onde os arquivos modificados serão salvos
3. Um atalho para iniciar junto com o MSFS2020 (opcional)
4. Um serviço para manter o estado atualizado após cada voo

---

## 🧪 Como usar

1. Instale o programa.
2. Inicie o MSFS2020 normalmente.
3. O programa irá detectar o momento certo e aplicar o estado desejado automaticamente.
4. Você pode alterar os arquivos dentro da pasta `assets/` para definir seus próprios perfis.

---

## 🧼 Limpeza de logs (em breve)

Será implementada uma rotina automática para limpar arquivos de log antigos periodicamente, evitando acúmulo desnecessário no disco.

---

## 🚧 Em desenvolvimento

- Interface gráfica em bandeja do sistema
- Suporte a múltiplos modelos PMDG (737-900, 737-700 etc.)
- Integração com clima real ou aeroporto de origem
- Randomização com base em eventos (por exemplo: hora do dia, falhas simuladas)
- Detecção e tratamento de botões com múltiplos valores (não binários)

---

## 🤝 Contribuições

Atualmente, este projeto é mantido de forma pessoal. Sugestões, feedbacks e testes são bem-vindos!

---

## 📜 Licença

Este projeto é de uso pessoal e não possui fins comerciais. Todo o conteúdo do simulador e das aeronaves utilizadas pertence a seus respectivos desenvolvedores (Microsoft, Asobo, PMDG).

---

## 🙏 Agradecimentos

A todos os desenvolvedores de conteúdo para MSFS, especialmente os criadores da SDK SimConnect e da comunidade de entusiastas da aviação virtual.

---

> “Tudo o que fizerdes, fazei-o de todo o coração, como para o Senhor e não para os homens.” (Colossenses 3,23)

---


