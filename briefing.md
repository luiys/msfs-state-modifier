# Projeto: MSFSStateModifier

## Descrição Geral

O MSFSStateModifier é um sistema desenvolvido em **Python** com o objetivo de monitorar o estado do simulador **Microsoft Flight Simulator 2020 (MSFS2020)** e aplicar automaticamente modificações no painel do **PMDG 737-800** com base em perfis definidos, melhorando a imersão e variedade entre voos.

## Componentes Principais

- **Monitoramento via SimConnect** da variável `GROUND_ALTITUDE`:
  - `0`: menu principal.
  - `None`: carregamento.
  - `> 0`: voo iniciado.

- **Modificador de State**:
  - Aplica modificações nos arquivos `PanelState` do PMDG 737-800.
  - Ativado em dois momentos:
    1. Ao iniciar o Windows (para garantir que o próximo voo já carregue com o state novo).
    2. Ao terminar um voo e retornar ao menu (detectado durante o loading).

- **Instalador com Inno Setup**:
  - Detecta automaticamente o diretório padrão dos arquivos `PanelState`.
  - Permite alterar manualmente os caminhos.
  - Cria tarefa agendada no Windows para iniciar automaticamente o programa junto com o sistema.
  - Adiciona opcionalmente um serviço NSSM para garantir execução contínua.

- **Configuração & Assets**:
  - Arquivos de configuração e estados movidos para:  
    `%LOCALAPPDATA%\MSFSStateModifier`
  - Evita erros de permissão e facilita backups ou alterações.

- **Logs**:
  - Sistema de log ativo que registra ações e erros.
  - Logs serão limpos automaticamente no futuro para evitar acúmulo.

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

5. **Tratar botões com valores diferentes de 0 e 1**
   - Permitir configuração individual para:
     - Inteiros com valor máximo (ex: 0 a 4).
     - Floats com valor mínimo e máximo (ex: 3.2 a 6.34).
   - Isso garantirá realismo e compatibilidade com controles que não são binários.

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

- Suporte a múltiplos modelos PMDG (737-800, 737-900, etc).
- Randomização automática com perfis configuráveis.
- Detecção automática de carregamento e término do simulador.
- Execução automática com o sistema e integração com SimConnect.
- Suporte à interface em bandeja com botão "Randomizar manualmente".
- Planejamento para integração com clima/aeroporto.
- Estrutura modular, organizada por JSONs.
- Identidade visual forte para publicação no flightsim.to.
- Planejamento para limpeza automática de logs.
