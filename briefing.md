# Projeto: MSFSStateModifier

## Descrição Geral

O **MSFSStateModifier** é um sistema desenvolvido em **Python** para o **Microsoft Flight Simulator 2020 (MSFS2020)** que modifica automaticamente o painel da aeronave **PMDG 737-800** ao carregamento do simulador. Ele simula situações em que a tripulação anterior ou equipe de manutenção pode ter deixado alguns botões fora das posições padrão do *Cold and Dark*, adicionando realismo e imprevisibilidade ao ambiente de voo.

---

## Funcionalidades

- 🎛️ **Randomização de botões no perfil Cold and Dark**
  - Altera botões aleatórios com base em configuração JSON.
  - Quantidade de alterações decidida por **probabilidades encadeadas**, simulando comportamento realista:
    - Exemplo: 50% de chance de aplicar 1 alteração, 40% para aplicar 2, e assim por diante.
  - Suporte a diferentes tipos de botões:
    - `binary`: alternância simples (ex: 0 ou 1)
    - `enum`: múltiplos valores fixos (ex: `Off`, `Auto`, `On`)
    - `int`: intervalo de inteiros definidos por `min` e `max`

- 🧩 **Perfis de nível de realismo prontos**
  - Perfis ajustáveis no `config.json`, com diferentes níveis de realismo:
    - `casual`: alterações leves e esporádicas
    - `natural`: comportamento realista de descuidos da tripulação
    - `avancado`: situações mais exigentes e frequentes
    - `caotico`: ambiente altamente imprevisível e desafiador
  - O perfil ativo é definido pela chave `selected_profile`.
  - A interface gráfica permite trocar o perfil em tempo real (via dropdown), atualizando automaticamente o `config.json`.

- 🛫 **Monitoramento de voo via SimConnect**
  - Observa a variável `GROUND_ALTITUDE`:
    - `0`: menu principal
    - `None`: loading
    - `> 0`: voo iniciado
  - Aplica modificações nos momentos ideais:
    - Ao iniciar o sistema
    - Ao retornar ao menu após um voo

- 🔄 **Encerramento automático**
  - O `.exe` principal é finalizado automaticamente quando o MSFS2020 é encerrado.

- 🚀 **Início automático com o Windows**
  - O script PowerShell (`watch-msfs.ps1`) inicia junto com o sistema via agendamento automático com um VBS oculto.

- 👻 **Execução oculta**
  - Tanto o PowerShell quanto o `.exe` principal executam de forma invisível ao usuário, sem ocupar a barra de tarefas.

- 🖼️ **Interface gráfica mínima**
  - Ícone na bandeja do sistema
  - Janela com botão "Randomizar agora"
  - Dropdown para trocar o nível de realismo em tempo real

- 📁 **Arquivos e configuração fora do Program Files**
  - Usa `%LOCALAPPDATA%\MSFSStateModifier` para evitar erros de permissão

- 📝 **Sistema de logs**
  - Logs separados para o monitorador (`msfs-state-modifier.log`) e para o modificador (`modification.log`)
  - Estratégias de limpeza implementadas:
    - 🧹 **Limpeza ao encerrar o simulador** (remove logs de sessões anteriores)

- 📦 **Instalador com Inno Setup**
  - Detecta automaticamente o diretório `PanelState`
  - Permite alteração manual do destino
  - Atualiza dinamicamente o `config.json` no pós-instalação

---

## Roadmap de Funcionalidades

### 🟡 Prioridade Média

1. **Tratar botões com valores do tipo float**
   - Exemplo: valores como `3.2`, `6.34`
   - Requer definição de `min`, `max` e precisão no JSON

2. **Checklist integrado**
   - Um checklist de cold and dark opcional incluído no sistema
   - Pode ser aberto via ícone da bandeja ou interface
   - Útil para usuários que não possuem checklist externo

---

## 🔵 Futuro

3. **Interface Gráfica Bonita e Funcional**
   - Com opções como:
     - Botão "Randomizar agora"
     - Histórico de modificações
     - Status do simulador
     - Visualização de logs e botão para limpá-los
     - Ícone de marca e estética clean

4. **Randomização automática e não-repetitiva**
   - Garantir variação e evitar repetir o mesmo state duas vezes seguidas

5. **Integração com clima ou aeroporto de origem**
   - Randomizar com base em METAR ou ICAO

