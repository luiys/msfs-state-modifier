# Relatório de Análise de Botões do MSFS State Modifier

Este documento lista os botões definidos no `config.json`, com suas possíveis variações de valor e, quando possível, o mapeamento de valores numéricos do `.sav` da PMDG com seus significados operacionais. Ao final, também são listados os botões cuja definição foi adiada por complexidade ou impossibilidade de análise.

---

## ✅ Botões com valores identificados

| Nome do Botão                  | Tipo     | Valores Numéricos  | Significado dos Valores                    |
|-------------------------------|----------|---------------------|---------------------------------------------|
| Passenger Oxygen Switch       | Binário  | 0 / 1              | 0 = Norm, 1 = On                            |
| Wing AntiIce Switch           | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| R Wiper Control               | Int      | 0 / 1 / 2 / 3      | 0 = Park, 1 = INT, 2 = LO, 3 = HI           |
| L Wiper Control               | Int      | 0 / 1 / 2 / 3      | Mesmo que R Wiper Control                   |
| Yaw Damper Switch             | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Window Heat Switches (1–4)    | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Probe Heat Switch 1           | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Probe Heat Switch 2           | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Engine AntiIce Switch         | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Engine AntiIce Switch 2       | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Eng Pump Switch A / B         | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Elec Pump Switch A / B        | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Pack Switch L / R             | Binário  | 0 / 1              | 0 = Off, 1 = Auto                           |
| Bleed Air Switch L / R        | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| APU Bleed Air Switch          | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Isolation Valve Switch        | Int      | 0 / 1 / 2          | 0 = Close, 1 = Auto, 2 = Open               |
| Cabin Press Mode Selector     | Int      | 0 / 1 / 2          | 0 = Auto, 1 = ALTN, 2 = Man                 |
| Wing Light                    | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Taxi Light                    | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Logo Light                    | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Position Light                | Int      | 0 / 1 / 2          | 0 = Strobe & Steady, 1 = Off, 2 = Steady    |
| Anti Collision Light          | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Wheel Well Light              | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| Show Meters                   | Botão    | 0 / 1              | 0 = Off, 1 = On                             |
| Captain Right Armrest         | Binário  | 0 / 1              | 0 = Recolhido, 1 = Estendido                |
| Parking Brake Lever           | Binário  | 0 / 1              | 0 = Released, 1 = Set                       |
| Xpndr                         | Int      | 0–4                | 0 = Stby, 1 = Alt Rptg Off, 2 = Xpndr, 3 = TA Only, 4 = TA/RA |
| Autobrakes Selector           | Int      | 0–5                | 0 = RTO, 1 = Off, 2 = 1, 3 = 2, 4 = 3, 5 = MAX |
| Fuel Pumps (todos)            | Binário  | 0 / 1              | 0 = Off, 1 = On                             |
| EmergencyLightsSwitch         | Int      | 0 / 1 / 2          | 0 = Off, 1 = Armed, 2 = On                  |
| Seat Belts Switch             | Int      | 0 / 1 / 2          | 0 = Off, 1 = Auto, 2 = On                   |
| Smoking Switch                | Int      | 0 / 1 / 2          | 0 = Off, 1 = Auto, 2 = On                   |

---

## ⚠️ Botões ainda não definidos

| Nome do Botão                 | Motivo da indefinição                         |
|-------------------------------|-----------------------------------------------|
| Flap Lever                    | Complexo: exige múltiplas variáveis relacionadas |
| flapLeverPosition             | Complexo: depende de outras variáveis          |
| Passenger Oxygen Switch Guard | Desnecessário: apenas guarda de proteção       |
| Spoiler Lever                 | Complexo: múltiplas posições possíveis         |

---
