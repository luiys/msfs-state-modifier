[Setup]
AppName=MSFS State Modifier
AppVersion=1.0
DefaultDirName={pf}\MSFSStateModifier
DefaultGroupName=MSFS State Modifier
OutputDir=dist
OutputBaseFilename=Setup_MSFS_State_Modifier
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\msfs-state-modifier.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\config.json"; DestDir: "{localappdata}\MSFSStateModifier"; Flags: ignoreversion
Source: "dist\assets\*"; DestDir: "{localappdata}\MSFSStateModifier\assets"; Flags: ignoreversion recursesubdirs
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "empty_log.txt"; DestDir: "{app}"; DestName: "msfs-state-modifier.log"; Flags: onlyifdoesntexist
Source: "watch-msfs.ps1"; DestDir: "{app}"; Flags: ignoreversion
Source: "empty_log.txt"; DestDir: "{localappdata}\MSFSStateModifier"; DestName: "modification.log"; Flags: onlyifdoesntexist

[Icons]
Name: "{group}\MSFS State Modifier"; Filename: "{app}\msfs-state-modifier.exe"
Name: "{commonstartup}\MSFS State Modifier - Hidden Launcher"; Filename: "{app}\launch-hidden.vbs"

[Code]
var
  FinalStatePage: TInputDirWizardPage;
  DefaultFinalPath: string;

function ReplaceStr(const S, OldPattern, NewPattern: String): String;
var
  I: Integer;
begin
  Result := S;
  I := Pos(OldPattern, Result);
  while I > 0 do
  begin
    Delete(Result, I, Length(OldPattern));
    Insert(NewPattern, Result, I);
    I := Pos(OldPattern, Result);
  end;
end;

procedure InitializeWizard;
begin
  DefaultFinalPath := ExpandConstant('{userappdata}') + '/../Local/Packages/Microsoft.FlightSimulator_8wekyb3d8bbwe/LocalState/packages/pmdg-aircraft-738/work/PanelState';

  FinalStatePage := CreateInputDirPage(
    wpSelectDir,
    'Pasta de destino do State Final',
    'Escolha a pasta onde o arquivo "random_cold_and_dark_state.sav" será salvo:',
    'Se você não quiser mudar, apenas clique em "Avançar" para manter o valor padrão abaixo:',
    False, ''
  );

  FinalStatePage.Add('');
  FinalStatePage.Values[0] := ExpandConstant(DefaultFinalPath);
end;

procedure CurStepChanged(CurStep: TSetupStep);
var
  ConfigFile, FinalPath, NewLine, VBScriptFile: string;
  ConfigContentAnsi: AnsiString;
  ConfigContent: string;
  ResultCode: Integer;
begin
  if CurStep = ssPostInstall then
  begin
    // Atualizar o config.json com o caminho final
    ConfigFile := ExpandConstant('{localappdata}\MSFSStateModifier\config.json');
    FinalPath := FinalStatePage.Values[0] + '/random_cold_and_dark_state.sav';
    FinalPath := ReplaceStr(FinalPath, '\', '/');
    NewLine := '"final_state_path": "' + FinalPath + '"';

    if LoadStringFromFile(ConfigFile, ConfigContentAnsi) then
    begin
      ConfigContent := string(ConfigContentAnsi);
      StringChangeEx(ConfigContent, '"final_state_path": "TO_BE_DEFINED"', NewLine, True);
      SaveStringToFile(ConfigFile, ConfigContent, False);
    end;

    // Criar dinamicamente o launch-hidden.vbs
    VBScriptFile := ExpandConstant('{app}\launch-hidden.vbs');
    SaveStringToFile(VBScriptFile,
      'Set WshShell = CreateObject("WScript.Shell")' + #13#10 +
      'WshShell.Run "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File ""' +
      ExpandConstant('{app}\watch-msfs.ps1') + '"" -ExecutablePath ""' +
      ExpandConstant('{app}\msfs-state-modifier.exe') + '""", 0', False);

    // Executar PowerShell ocultamente já durante a instalação
    Exec('powershell.exe',
      '-ExecutionPolicy Bypass -WindowStyle Hidden -File "' + ExpandConstant('{app}\watch-msfs.ps1') +
      '" -ExecutablePath "' + ExpandConstant('{app}\msfs-state-modifier.exe') + '"',
      '', SW_HIDE, ewNoWait, ResultCode);
  end;
end;

[UninstallDelete]
Type: files; Name: "{app}\msfs-state-modifier.log"
Type: files; Name: "{app}\watch-msfs.ps1"
Type: files; Name: "{app}\icon.ico"
Type: files; Name: "{app}\launch-hidden.vbs"
Type: files; Name: "{app}\msfs-state-modifier.exe"
Type: filesandordirs; Name: "{localappdata}\MSFSStateModifier"
Type: dirifempty; Name: "{app}"
Type: files; Name: "{localappdata}\MSFSStateModifier\modification.log"

[Run]
Filename: "powershell.exe"; Parameters: "-Command New-Item -ItemType Directory -Path '$env:LOCALAPPDATA\MSFSStateModifier' -Force"; Flags: runhidden
