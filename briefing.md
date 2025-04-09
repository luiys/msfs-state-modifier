# Projeto: MSFSStateModifier

## Descrição Geral

O **MSFSStateModifier** é um sistema desenvolvido em **Python** com o objetivo de monitorar o estado do simulador **Microsoft Flight Simulator 2020 (MSFS2020)** e aplicar automaticamente modificações no painel do **PMDG 737-800** com base em perfis aleatórios, simulando a possibilidade de que a tripulação anterior ou a equipe de manutenção tenha deixado algum botão fora da posição padrão do *Cold and Dark*.

---

## Funcionalidades

- 🎛️ **Randomização de botões no state Cold and Dark**
  - Seleciona até *N* botões aleatórios para alterar o valor.
  - Tipos de botões suportados:
    - `binary` (valores 0 ou 1)
    - `enum` (lista de valores fixos como `"OFF"`, `"AUTO"`, `"ON"`)
    - `int` (inteiros entre `min` e `max` definidos no JSON)

- 🛫 **Monitoramento do simulador com SimConnect**
  - Detecta:
    - Menu principal
    - Carregamento de voo
    - Voo iniciado
  - Aplica alterações no momento certo, sem interferência do usuário.

- ⚙️ **Execução automática com o Windows**
  - Script PowerShell inicia com o sistema e aguarda o MSFS2020.

- 📁 **Arquivos e configuração fora do Program Files**
  - Usa `%LOCALAPPDATA%\MSFSStateModifier` para evitar erros de permissão.

- 📝 **Sistema de logs**
  - Logs separados para o monitorador e para o modificador.
  - Planejamento para rotação automática futura.

- 📦 **Instalador com Inno Setup**
  - Detecta o diretório `PanelState` automaticamente.
  - Permite personalização manual dos caminhos.

---

## Roadmap de Funcionalidades

### 🟢 Prioridade Alta (estável/finalização)

1. **Ocultar execução do PowerShell**
   - Ao iniciar com o Windows, o PowerShell deve rodar completamente escondido (sem janela nem ícone visível na barra).

2. **Minimizar o .exe para a bandeja do sistema**
   - O programa deve aparecer apenas na bandeja (setinha da barra de tarefas) e não na barra principal.

3. **Fechar automaticamente o .exe quando o simulador for encerrado**
   - Detectar quando o MSFS2020 é finalizado e encerrar o modificador automaticamente.

---

### 🟡 Prioridade Média

4. **Limpeza automática dos logs**
   - Estratégia pendente:  
     - Ao desligar o Windows,  
     - Ou a cada X horas.
5. **Tratar botões com valores do tipo float**
   - Exemplo: valores como `3.2`, `6.34`
   - Requer definição de `min`, `max` e precisão

---

### 🔵 Futuro

6. **Interface Gráfica Bonita e Funcional**
   - Com opções como:
     - Botão "Randomizar agora"
     - Histórico de modificações
     - Status do simulador
     - Visualização de logs e botão para limpá-los
     - Ícone de marca e estética clean.

7. **Perfis de randomização**
   - Exemplo:
     - Casual
     - Realista
     - Emergência
   - Selecionáveis via JSON e futuramente via UI.

8. **Perfis personalizados**
   - Carregamento de configurações específicas do usuário via arquivos `.json`.

9. **Randomização automática e não-repetitiva**
   - Garantir variação e evitar repetir o mesmo state duas vezes seguidas.

10. **Integração com clima ou aeroporto de origem**
    - Randomizar com base em METAR ou ICAO.

11. **Rotação automática dos logs**
    - Deletar logs antigos e manter apenas os mais recentes.

---

## Diferenciais em relação ao concorrente
(Como o "PMDG 737-700 Panel Randomiser" do flightsim.to)

- Suporte a múltiplos modelos PMDG (ex: 737-800, 737-900)
- Randomização automática com base no carregamento do simulador
- Integração nativa com SimConnect
- Execução automática com o Windows
- Identidade visual pensada para flightsim.to
- Estrutura de configuração modular via JSON
- Suporte a diferentes tipos de botão: `binary`, `enum`, `int`
