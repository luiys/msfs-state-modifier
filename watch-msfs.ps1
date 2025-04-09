param (
    [string]$ExecutablePath
)

# Caminho do diretório de log seguro
$LogDir = "$env:LOCALAPPDATA\MSFSStateModifier"
$LogFile = Join-Path -Path $LogDir -ChildPath "msfs-state-monitor.log"
$MainLogFile = Join-Path -Path $LogDir -ChildPath "msfs-state-modifier.log"
$ModifierLogFile = Join-Path -Path $LogDir -ChildPath "modification.log"

# Cria a pasta de log, se necessário
if (-not (Test-Path -Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
}

function Write-Log {
    param (
        [string]$Message
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $LogFile -Value "[$timestamp] $Message"
}

function Is-FlightSimulatorRunning {
    $process = Get-Process -Name "FlightSimulator" -ErrorAction SilentlyContinue
    return $process -ne $null
}

function Is-StateModifierRunning {
    $process = Get-Process -Name "msfs-state-modifier" -ErrorAction SilentlyContinue
    return $process -ne $null
}

function Clear-Logs {
    try {
        if (Test-Path $LogFile) {
            Clear-Content $LogFile
            Write-Log "🧹 Log do monitor limpo com sucesso."
        }
        if (Test-Path $MainLogFile) {
            Clear-Content $MainLogFile
            Write-Log "🧹 Log da main limpo com sucesso."
        }
        if (Test-Path $ModifierLogFile) {
            Clear-Content $ModifierLogFile
            Write-Log "🧹 Log do modificador limpo com sucesso."
        }
    } catch {
        Write-Log "⚠️ Erro ao tentar limpar os logs: $_"
    }
}

Write-Log "Monitor de MSFS iniciado."
Write-Log "Caminho do modificador: $ExecutablePath"

if (-not (Test-Path $ExecutablePath)) {
    Write-Log "Executável não encontrado no caminho especificado. Encerrando script."
    exit 1
}

# Loop contínuo para monitorar o MSFS
while ($true) {
    try {
        if (Is-FlightSimulatorRunning) {
            Write-Log "MSFS2020 detectado."

            if (-not (Is-StateModifierRunning)) {
                Write-Log "Iniciando o modificador de state..."
                Start-Process -FilePath $ExecutablePath
            } else {
                Write-Log "Modificador já está em execução."
            }

            # Espera até o MSFS ser fechado
            while (Is-FlightSimulatorRunning) {
                Start-Sleep -Seconds 5
            }

            Write-Log "MSFS2020 foi encerrado."

            # Encerra o modificador se estiver rodando
            $modifierProc = Get-Process -Name "msfs-state-modifier" -ErrorAction SilentlyContinue
            if ($modifierProc) {
                Write-Log "Encerrando o modificador de state..."
                Stop-Process -Id $modifierProc.Id -Force
                Write-Log "Modificador encerrado com sucesso."
            }

            # Limpa os logs
            Clear-Logs
        } else {
            Write-Log "MSFS2020 não está em execução."
        }
    } catch {
        Write-Log "Erro durante monitoramento: $_"
    }

    Start-Sleep -Seconds 5
}
