# MSFS State Modifier

**🇺🇸 EN**  
Tool for MSFS2020 that introduces random variations to the Cold & Dark state of PMDG 737 aircraft, making each flight startup more realistic.

**🇧🇷 PT-BR**  
Ferramenta para MSFS2020 que introduz variações aleatórias no estado Cold & Dark dos PMDG 737, tornando cada início de voo mais realista.

---

## ✈️ Purpose / Objetivo

**🇺🇸**  
MSFS2020 loads the PMDG 737 in Cold & Dark, but all buttons and systems always start in the same position, reducing immersion. Currently, the checklist to verify if everything is in the correct position is essentially useless, as all buttons always start in the same default position.  
MSFS State Modifier keeps the general Cold & Dark state but adds realistic variations, as if the previous crew or the maintenance team left something out of place. This simulates a more authentic operational environment, where some things might not be in their proper position, requiring extra attention from the pilot during the cockpit setup.

**🇧🇷**  
Embora o MSFS2020 carregue o PMDG 737 em Cold & Dark, todos os botões e sistemas iniciam nas mesmas posições, o que reduz a imersão. Atualmente, o checklist para verificar se tudo está na posição correta é praticamente inútil, já que todos os botões sempre começam na mesma posição padrão.  
O MSFS State Modifier mantém o estado geral Cold & Dark, mas com variações realistas, como se a tripulação anterior ou a equipe de manutenção tivesse deixado algo fora do lugar. Isso simula de forma mais autêntica o ambiente operacional de um avião real, onde algumas coisas podem não estar em suas posições corretas, exigindo atenção extra do piloto durante a preparação do cockpit.

---

## ⚙️ Features / Funcionalidades

**🇺🇸**  
- ✅ Support for PMDG 737-800 *(others coming soon)*  
- 🎲 Automatic aircraft state randomization  
- 🧠 **Chain-based probability** logic  
- 🧾 Realism profiles via JSON:
  - *Casual* – light, ideal for beginners  
  - *Realistic* – plausible crew oversights  
  - *Advanced* – requires extra attention  
  - *Chaotic* – intense variation, like total disorder  
- 🛫 Automatic activation with MSFS  
- 🚪 Automatically shuts down with the sim  
- 📦 Automated installer  
- 👻 Runs silently in background  
- 🖼️ Tray interface with "Randomize Now" button  

**🇧🇷**  
- ✅ Suporte ao PMDG 737-800 *(em breve outros modelos)*  
- 🎲 Randomização automática do estado da aeronave  
- 🧠 Lógica de **probabilidades encadeadas**  
- 🧾 Perfis de realismo via JSON:
  - *Casual* – leve, ideal para iniciantes  
  - *Natural* – esquecimentos plausíveis da tripulação  
  - *Avançado* – exige atenção redobrada  
  - *Caótico* – como se tudo estivesse errado  
- 🛫 Ativação automática com o MSFS  
- 🚪 Encerra junto com o simulador  
- 📦 Instalador automatizado  
- 👻 Execução invisível  
- 🖼️ Interface em bandeja com botão "Randomize Now"

---

## 🛠️ Installation / Instalação

**🇺🇸**  
To install MSFS State Modifier, just follow these steps:  
1. Download the `Setup_MSFS_State_Modifier` installer.  
2. Run the installer.  
3. After the installation, the tool will automatically detect if MSFS is open, and if it is, MSFS State Modifier will automatically start in the tray.  
4. If MSFS is closed, the tool will start automatically in the tray once you launch MSFS.  

**🇧🇷**  
Para instalar o MSFS State Modifier, basta seguir os passos abaixo:  
1. Baixe o instalador `Setup_MSFS_State_Modifier`.  
2. Execute o instalador.  
3. Após a instalação, a ferramenta detectará automaticamente se o MSFS está aberto e, se estiver, iniciará automaticamente na bandeja o MSFS State Modifier.  
4. Se o MSFS estiver fechado, quando você iniciá-lo, o MSFS State Modifier será iniciado automaticamente na bandeja.

---

## 🧪 How to Use / Como Usar

**🇺🇸**  
1. Load the PMDG 737-800 on the ground at any airport.  
2. In the FMC, go to *PMDG Setup*, then *Startup State*, and select the profile called "RANDOM_COLD_AND_DARK_STATE".  
3. Done! Now, every time you start a flight with the 737-800, there will be a possibility that some things will be out of place.  
4. To configure the randomness probability of the buttons, there are some pre-configured realism profiles. To switch between them, go to the tray applications, right-click on MSFS State Modifier, and click "Open".  
5. Choose between the profiles: Casual, Realistic, Advanced, and Chaotic.  
6. After switching profiles, click "Randomize Now" and start a new flight with the 737-800.

**🇧🇷**  
1. Carregue o PMDG 737-800 no solo em qualquer aeroporto.  
2. No FMC, vá em *PMDG Setup*, depois em *Startup State* e selecione o perfil chamado "RANDOM_COLD_AND_DARK_STATE".  
3. Pronto! Agora, toda vez que você iniciar um voo com o 737-800, haverá a possibilidade de algumas coisas estarem fora do lugar.  
4. Para configurar as probabilidades de aleatoriedade dos botões, existem alguns perfis de realismo já configurados. Para alterar entre eles, vá nos aplicativos que ficam na bandeja, clique com o botão direito no MSFS State Modifier e clique em "Open".  
5. Escolha entre os perfis: Casual, Realistic, Advanced e Chaotic.  
6. Após trocar de perfil, clique em "Randomize Now" e comece um novo voo com o 737-800.

---

## ⚙️ Customization / Personalização

**🇺🇸**  
You can customize the behavior of each realism profile by editing the `config.json` file in `%LOCALAPPDATA%\MSFSStateModifier`.  
It’s also possible to create **your own profiles** with custom probability values for each system group.

**🇧🇷**  
Você pode personalizar o comportamento de cada perfil de realismo editando o arquivo `config.json` localizado em `%LOCALAPPDATA%\MSFSStateModifier`.  
Também é possível criar **seus próprios perfis**, com valores personalizados de probabilidade para cada grupo de sistemas.

---

## ❓ Troubleshooting / Dúvidas

**🇺🇸**  
If something goes wrong or if you have any questions, feel free to leave a comment, and I'll be happy to help you with any issues you may encounter!

**🇧🇷**  
Se algo der errado ou se você tiver alguma dúvida, fique à vontade para deixar um comentário, e eu ficarei feliz em ajudar com qualquer problema que você possa encontrar!

---

## 📜 License / Licença

**🇺🇸**  
This project is for personal use only.  
All simulator content belongs to its original developers.

**🇧🇷**  
Projeto de uso pessoal, sem fins comerciais.  
Conteúdo do simulador pertence aos desenvolvedores originais.

