# Projeto: MSFSStateModifier

## Descrição Geral

O **MSFSStateModifier** é um sistema desenvolvido em **Python** para o **Microsoft Flight Simulator 2020 (MSFS2020)** que modifica automaticamente o painel da aeronave **PMDG 737-800** ao carregamento do simulador. Ele simula situações em que a tripulação anterior ou equipe de manutenção pode ter deixado alguns botões fora das posições padrão do *Cold and Dark*, adicionando realismo e imprevisibilidade ao ambiente de voo.

---

## Funcionalidades

- 🎛️ **Randomização de botões no perfil Cold and Dark**
  - Altera até *N* botões aleatórios com base em configuração JSON.
  - Suporte a diferentes tipos de botões:
    - `binary`: alternância simples (ex: 0 ou 1)
    - `enum`: múltiplos valores fixos (ex: `Off`, `Auto`, `On`)
    - `int`: intervalo de inteiros definidos por `min` e `max`

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
  - Ícone na bandeja do sistema (system tray)
  - Janela pode ser exibida ao clicar no ícone

- 📁 **Arquivos e configuração fora do Program Files**
  - Usa `%LOCALAPPDATA%\MSFSStateModifier` para evitar erros de permissão

- 📝 **Sistema de logs**
  - Logs separados para o monitorador e para o modificador
  - Salvos em local seguro com permissão de escrita

- 📦 **Instalador com Inno Setup**
  - Detecta automaticamente o diretório `PanelState`
  - Permite alteração manual do destino
  - Atualiza dinamicamente o `config.json` no pós-instalação

---

## Roadmap de Funcionalidades

### 🟡 Prioridade Média

1. **Limpeza automática dos logs**
   - Estratégia pendente:  
     - Ao desligar o Windows  
     - Ou a cada X horas

2. **Tratar botões com valores do tipo float**
   - Exemplo: valores como `3.2`, `6.34`
   - Requer definição de `min`, `max` e precisão no JSON

3. **Probabilidades encadeadas para decidir quantidade de alterações**
   - Exemplo:
     - 50% de chance para aplicar 1 alteração
     - Se for bem-sucedido, tenta aplicar 2 com 40% de chance, e assim por diante.
   - Aborta o processo quando uma chance falha, e usa o último número bem-sucedido.

4. **Checklist integrado**
   - Um checklist de cold and dark opcional incluído no sistema
   - Pode ser aberto via ícone da bandeja ou interface
   - Útil para usuários que não possuem checklist externo

---

## 🔵 Futuro

5. **Interface Gráfica Bonita e Funcional**
   - Com opções como:
     - Botão "Randomizar agora"
     - Histórico de modificações
     - Status do simulador
     - Visualização de logs e botão para limpá-los
     - Ícone de marca e estética clean

6. **Perfis de randomização**
   - Exemplo:
     - Casual
     - Realista
     - Emergência
   - Selecionáveis via JSON e futuramente via UI

7. **Perfis personalizados**
   - Carregamento de configurações específicas do usuário via arquivos `.json`

8. **Randomização automática e não-repetitiva**
   - Garantir variação e evitar repetir o mesmo state duas vezes seguidas

9. **Integração com clima ou aeroporto de origem**
   - Randomizar com base em METAR ou ICAO

10. **Rotação automática dos logs**
    - Deletar logs antigos e manter apenas os mais recentes

---

## Diferenciais em relação ao concorrente
(Como o "PMDG 737-700 Panel Randomiser" do flightsim.to)

- Suporte a múltiplos modelos PMDG (ex: 737-800, 737-900)
- Randomização automática com base no carregamento do simulador
- Integração nativa com SimConnect
- Execução automática com o Windows
- Ocultação completa (PowerShell e EXE)
- Interface em bandeja do sistema
- Estrutura de configuração modular via JSON
- Suporte a diferentes tipos de botão: `binary`, `enum`, `int`
- Planejamento para logs limpos e interface rica
- Lógica realista de randomização com base em probabilidade
- Planejamento de checklist integrado ao sistema
