# 🧑‍💻 Manual Técnico — MSFS State Modifier

Este manual é voltado para desenvolvedores que desejam contribuir ou retomar o desenvolvimento do sistema **MSFS State Modifier**. Ele fornece uma visão geral da estrutura, instruções para testes, empacotamento e boas práticas para modificações.

---

## 📁 Estrutura de Pastas

- **assets/**: arquivos .sav de estado Cold & Dark (original e cópia modificada)
- **build/**: arquivos gerados pelo PyInstaller
- **dist/**: contém o .exe empacotado e o setup final gerado pelo Inno Setup
- **SimConnect/**: SDK SimConnect e seus módulos Python
- **utils/**: scripts auxiliares reutilizáveis (modifier_probability.py, etc.)
- **__pycache__/**: cache de arquivos .pyc (ignorar)
- **Arquivo main.py**: ponto de entrada principal do sistema
- **Arquivo state_modifier.py**: lógica de modificação de botões
- **Arquivo watch-msfs.ps1**: script de monitoramento e controle de execução
- **Arquivo installer.iss**: script do instalador criado com Inno Setup
- **Arquivo main.spec**: script de empacotamento do PyInstaller
- **Arquivo config.json**: arquivo de configuração principal (veja observações abaixo)

---

## 🧠 O que cada arquivo faz

- **main.py**: monitora o estado do simulador (menu, carregando, em voo) via SimConnect e aciona o modificador (state_modifier.py) nos momentos certos.
- **state_modifier.py**: aplica as modificações nos botões com base nas regras configuradas no config.json.
- **utils/modifier_probability.py**: contém a lógica de sorteios encadeados, baseada no perfil selecionado no config.json.
- **watch-msfs.ps1**: script que monitora o MSFS, inicia o .exe quando ele abrir, finaliza quando fechar e limpa os logs.
- **config.json**: todas as configurações do sistema, inclusive os perfis de realismo.
- **main.spec**: define os arquivos incluídos no .exe ao empacotar com PyInstaller.
- **installer.iss**: configura o instalador (setup) gerado com Inno Setup.

---

## 🧪 Como testar

**Cenário simples (apenas main.py ou state_modifier.py):**

1. Alterar o código.
2. Rodar com:
   - py main.py

**Cenário completo (envolve outros arquivos ou testes reais):**

1. Rodar:
   - pyinstaller main.spec
2. Compilar installer.iss com o Inno Setup.
3. Desinstalar o MSFSStateModifier anterior.
4. Instalar o novo setup gerado na pasta /dist/.

---

## 📋 Observações importantes

- O config.json **deve ser atualizado em dois lugares**:
  - na raiz do projeto
  - na pasta /dist
- Logs para debug estão na pasta:
  %LOCALAPPDATA%\MSFSStateModifier
  - msfs-state-monitor.log: logs do PowerShell
  - msfs-state-modifier.log: logs da main.py
  - modification.log: logs da state_modifier.py
- **Novos arquivos Python** devem ser adicionados no main.spec e no installer.iss

---

## 🔧 Comandos úteis

**Listar processos ativos do watch-msfs.ps1:**

Get-WmiObject Win32_Process | Where-Object { $_.CommandLine -like '*watch-msfs.ps1*' } | Select-Object ProcessId, CommandLine

**Encerrar todos os processos do watch-msfs.ps1:**

Get-WmiObject Win32_Process | Where-Object { $_.CommandLine -like '*watch-msfs.ps1*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }

---

## ✅ Checklist ao adicionar uma nova funcionalidade

- [ ] Atualizar o config.json (raiz e dist)
- [ ] Adicionar mensagens de log onde necessário
- [ ] Incluir o arquivo no main.spec (caso necessário)
- [ ] Incluir no installer.iss (se for ser distribuído com o setup)
- [ ] Atualizar o briefing.md (documentação técnica)
- [ ] Testar rodando o .exe com o MSFS em execução

---

## 🧱 Rotina de empacotamento (PyInstaller + Inno Setup)

1. Executar:
   - pyinstaller main.spec
2. Abrir o Inno Setup
3. Compilar o installer.iss
4. Desinstalar o atual MSFSStateModifier
5. Instalar o novo setup da pasta dist/

---

Se algo ainda parecer confuso, rode o sistema com py main.py, leia os logs e vá rastreando o comportamento a partir das funções do main.py.

"Conhecer o próprio sistema é metade da batalha."