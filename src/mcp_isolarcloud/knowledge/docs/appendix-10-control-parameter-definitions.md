# Appendix 10: Control Parameter Definitions

**Appendix 10: Control Parameter Definitions**

| param\_code | Device Type | Parameter | Set Value or Range Description |
| --- | --- | --- | --- |
| 10001 | Hybrid Inverter | SOC Upper Limit | The value range is 700 to 1000, which indicates 70% to 100% |
| 10002 | Hybrid Inverter | SOC Lower Limit | The value range is 0 to 500, which indicates 0% to 50% |
| 10003 | Hybrid Inverter | Energy Management Mode | 0: Self-consumption Mode, 2: Compulsory Mode, 3: External Energy Dispatch, 4: VPP Dispatch. Default to 0. |
| 10004 | Hybrid Inverter | Charging/Discharging Command | 170: Charging, 187: Discharging, 204: Stopped. Default to 204. |
| 10005 | Hybrid Inverter | Charging/Discharging Power | The value range is 0W to 5000W and defaults as 1000. |
| 10006 | Hybrid Inverter & PV Inverter | Existing Inverter | 170: Enable, 85: Disable |
| 10007 | Hybrid Inverter & PV Inverter | Limited power switch | 170: Enable, 85: Disable |
| 10008 | Hybrid Inverter & PV Inverter | Active Power Limit Ratio | The value range is 0 to 1000, which indicates 0% to 100% |
| 10009 | Hybrid Inverter & PV Inverter | Reactive Power Regulation Mode | 85: OFF, 161: PF enabled, 162: Reactive Power Ratio enable-Q (t), 164: Q (U) curve-Q (U), 163: Q(P) curve- Q(P) |
| 10010 | Hybrid Inverter & PV Inverter | Q(T) | The value range is -600 to 600, which indicates -60% to 60% |
| 10011 | Hybrid Inverter & PV Inverter | Boot/Shutdown | 207:Boot 206:Shutdown 174:Reboot |
| 10012 | Hybrid Inverter & PV Inverter | Feed-in Limitation | 170: Enable, 85: Disable |
| 10012 | Logger1000&EyeM4 | Feed-in Limitation | 1: Enable, 0: Disable |
| 10013 | Hybrid Inverter & PV Inverter | Feed-in Limitation Value | The value range is 0 to rated power of inverter (Feed-in Limitation must be enabled when setting this value) |
| 10014 | Hybrid Inverter & PV Inverter | Feed-in Limitation Ratio | The value range is 0 to 1000, which indicates 0% to 100% (Feed-in Limitation must be enabled when setting this value) |
| 10014 | Logger1000&EyeM4 | Feed-in Limitation Ratio | The value range is -1000 to 1000, which indicates -100% to 100% (Feed-in Limitation must be enabled when setting this value) Note:points used in the data collector mode of Logger1000 |
| 10015 | Hybrid Inverter | Forced Charging Target SOC1 | The value range is 0 to 100, which indicates 0% to 100% |
| 10016 | Hybrid Inverter | Forced Charging Target SOC2 | The value range is 0 to 100, which indicates 0% to 100% |
| 10017 | Hybrid Inverter | External EMS Heartbeat | The value range is 1 to 1000, which indicates 1s to 1000s |
| 10024 | Hybrid Inverter | Battery First | 170: Enable, 85: Disable |
| 10025 | Hybrid Inverter & PV Inverter | Active Power Soft Start after Fault | 170: Enable, 85: Disable |
| 10026 | Hybrid Inverter & PV Inverter | Active Power Soft Start Time after Fault | The value range is 1 to 1200, which indicates 1s to 1200s (Active Power Soft Start after Fault must be enabled when setting this value) |
| 10027 | Hybrid Inverter & PV Inverter | Active Power Soft Start | 170: Enable, 85: Disable |
| 10028 | Hybrid Inverter & PV Inverter | Active Power Soft Start Gradient | The value range is 5 to 10000, which indicates 0.05% ~ 100% (Active Power Soft Start must be enabled when setting this value)) |
| 10029 | Hybrid Inverter & PV Inverter | Active Power Gradient Control | 170: Enable, 85: Disable |
| 10030 | Hybrid Inverter & PV Inverter | Active Power Decline Gradient | The value range is 1 to 6000, which indicates 1%/min to 6000%/min (Active Power Gradient Control must be enabled when setting this value) |
| 10031 | Hybrid Inverter & PV Inverter | Active Power Rising Gradient | The value range is 1 to 6000, which indicates 1%/min to 6000%/min (Active Power Gradient Control must be enabled when setting this value) |
| 10032 | Hybrid Inverter & PV Inverter | Active Power Setting Persistence | 170: Enable, 85: Disable |
| 10033 | Hybrid Inverter & PV Inverter | Shutdown When Active Power Limit to 0% | 170: Enable, 85: Disable |
| 10034 | Hybrid Inverter & PV Inverter | Reactive Response | 170: Enable, 85: Disable (Only can be set only when Reactive Power Regulation Mode is set to PF, Qt, Q(P), or Q(U)) |
| 10035 | Hybrid Inverter & PV Inverter | Reactive power regulation time | The value range is 1 to 6000, which indicates 0.1s to 600s (Only can be set only when Reactive Power Regulation Mode is set to PF, Qt, Q(P), or Q(U)) |
| 10036 | Hybrid Inverter & PV Inverter | PF | The value range is -1000 to 1000, which indicates -1 to 1 (Only can be set only when Reactive Power Regulation Mode is set to PF) |
| 10065 | Hybrid Inverter & PV Inverter | Forced Charging | 170: Enable, 85: Close |
| 10066 | Hybrid Inverter & PV Inverter | Forced Charging Valid Time | 0: Weekdays 1: Everyday |
| 10067 | Hybrid Inverter & PV Inverter | Forced Charging Start Time 1: Hour | Value range: 0 to 24 (no minutes), 24 by default |
| 10068 | Hybrid Inverter & PV Inverter | Forced Charging Start Time 1: Minute | Value range: 0 to 59, 0 by default |
| 10069 | Hybrid Inverter & PV Inverter | Forced Charging End Time 1: Hour | Value range: 0 to 24 (no minutes), 24 by default |
| 10070 | Hybrid Inverter & PV Inverter | Forced Charging End Time 1: Minute | Value range: 0 to 59, 0 by default |
| 10071 | Hybrid Inverter & PV Inverter | Forced Charging Target SOC1 | Value range: 0 to 100, which indicates 0% to 100% |
| 10072 | Hybrid Inverter & PV Inverter | Forced Charging Start Time 2: Hour | Value range: 0 to 24 (no minutes), 24 by default |
| 10073 | Hybrid Inverter & PV Inverter | Forced Charging Start Time 2: Minute | Value range: 0 to 59, 0 by default |
| 10074 | Hybrid Inverter & PV Inverter | Forced Charging End Time 2: Hour | Value range: 0 to 24 (no minutes), 24 by default |
| 10075 | Hybrid Inverter & PV Inverter | Forced Charging End Time 2: Minute | Value range: 0 to 59, 0 by default |
| 10076 | Hybrid Inverter & PV Inverter | Forced Charging Target SOC2 | Value range: 0 to 100, which indicates 0% to 100% |
| 10082 | Logger1000 & EMS | Charge/Discharge Command in External Dispatch Mode | 170: Charge; 187: Discharge; 204: Forbidden |
| 10083 | Logger1000 & EMS | Charging/Discharging Power in External Dispatch Mode | Data Range: 0~Plant Charging/Discharging Upper Limit Range Description. Call interface: getDevPropertyPointValue to get the specific limit range with point id:29046. |
| 10085 | Logger1000 & EMS | EMS Heartbeat Settings in External Dispatch Mode | Data Range: 10~1000 |
| 10086 | Logger1000 & EMS | Energy Management Mode | 1: Self-Consumption; 2: Time Plan; 4: VPP; 5: Compulsory Mode |
| 10087 | Logger1000 & EMS | Feed-in Limitation Ratio in External Dispatch Mode | Data Range：-1000~1000, default 1000 Note:points used in the energy management mode of Logger1000 |
| 10088 | Logger1000 & EMS | Feed-in Limitation ON/OFF in External Dispatch Mode | 170：Enable，85：Close default Close |
| 10089 | Logger1000 & EMS | Feed-in Limitation Value in External Dispatch Mode | Data Range: -99999999~99999999,default 0 |
| 10090 | Logger1000 & EMS | PV power limitation | 1: Enable，0：Close |
| 10091 | Energy Storage System | Max. Charging Power | Data Range：10~(Max. Charging Power Upper Limit Range Description\*100), Max. Charging Power Upper Limit Range Description can be accessed by calling interface: getDevPropertyPointValue with point id:18290，Default Range is: 10~1060 |
| 10092 | Energy Storage System | Max. Discharging Power | Data Range：10~(Max. Discharging Power Upper Limit Range Description\*100), Max. Discharging Power Upper Limit Range Description can be accessed by calling interface: getDevPropertyPointValue with point id:18291，Default Range is: 10~1060 |
| 10095 | EMS | Function enable/disable | 1：Enable，0：Disable |
| 10096 | EMS | Grid-connection point frequency FN | Data Range: [0.000-100.000] Hz |
| 10097 | EMS | Contingency FCAS action deadband fd | Data Range: (0.000-0.200] Hz, Attention: Contingency FCAS action deadband fd(Hz) < Contingency FCAS frequency deviation threshold for full-scale response(Hz) |
| 10098 | EMS | Contingency FCAS maximum output active power PA | Data Range: (0.00-9999.99] MW |
| 10099 | EMS | Contingency FCAS maximum absorption active power PB | Data Range: (0.00-9999.99] MW |
| 10100 | EMS | Contingency FCAS frequency deviation threshold for full-scale response | Data Range: (0.000-0.500] Hz |
| 10038 | Hybrid Inverter & PV Inverter | Under-voltage first-level protection value | PV Inverter range: minimum rated voltage 0.05 times, maximum rated voltage 1.0 times -0.1V; Hybrid Inverter range: minimum 460, maximum 2300 |
| 10039 | Hybrid Inverter & PV Inverter | Overvoltage first-level protection value | PV Inverter range: minimum rated voltage (1.0 times + 0.2V), maximum rated voltage 1.4 times; Hybrid Inverter range: minimum 2300, maximum 2990 |
| 10040 | Hybrid Inverter & PV Inverter | Under-frequency first-level protection value | PV Inverter range: Minimum value [50Hz grid: 4500,60Hz grid: non-North American countries: 5500,60Hz grid: North American countries: 5000], maximum value [50Hz grid: 4996,60Hz grid: non-North American countries: 5996,60Hz grid: North American countries: 5996] Hybrid Inverter range: minimum 4500, maximum 5000 |
| 10041 | Hybrid Inverter & PV Inverter | Over-frequency first-level protection value | PV Inverter range: Minimum value [50Hz grid: 5004, 60Hz grid: 6004], maximum value [50Hz grid: 5500, 60Hz grid: 6600]; Hybrid Inverter range: minimum 5000, maximum 5550 |
| 10042 | Hybrid Inverter & PV Inverter | Overvoltage protection recovery value | PV Inverter range: Minimum 1.0 times the rated voltage +0.1V, maximum 1.4 times the rated voltage -0.1V; Hybrid Inverter range: minimum 2300, maximum 2990 |
| 10043 | Hybrid Inverter & PV Inverter | Under-voltage protection recovery value | PV Inverter range: minimum rated voltage (0.05 times +0.1V), maximum rated voltage 1.0 times; Hybrid Inverter range: minimum 1300, maximum 2300 |
| 10044 | Hybrid Inverter & PV Inverter | Overfrequency protection recovery value | PV Inverter range: Minimum value [50Hz grid: 5002, 60Hz grid: 6002], maximum value [50Hz grid: 5498, 60Hz grid: 6498]; Hybrid Inverter range: minimum 5000, maximum 5550 |
| 10045 | Hybrid Inverter & PV Inverter | Under-frequency protection recovery value | PV Inverter range: Minimum value [50Hz grid: 4502, 60Hz grid: 5502], maximum value [50Hz grid: 4998, 60Hz grid: 5998] ; Hybrid Inverter range: minimum 4450, maximum 5000 |
| 10101 | Hybrid Inverter & PV Inverter | Under-voltage first-level protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the first-level protection time for under-voltage = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10102 | Hybrid Inverter & PV Inverter | Under-voltage secondary protection value | Range dependence: Rated grid voltage, maximum undervoltage secondary protection value = rated grid voltage -1, minimum undervoltage secondary protection value = rated grid voltage \*0.05; The grid company provides standard default Settings for setting the abnormal protection threshold and protection time of the power grid, which generally do not need to be changed. |
| 10103 | Hybrid Inverter & PV Inverter | Under-voltage secondary protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the secondary protection time for under-voltage = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10104 | Hybrid Inverter & PV Inverter | Overvoltage level 1 protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the first-level protection time for overvoltage = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10105 | Hybrid Inverter & PV Inverter | Overvoltage secondary protection value | Range dependence: Rated grid voltage, maximum overvoltage secondary protection value = rated grid voltage \*1.4, minimum overvoltage secondary protection value = rated grid voltage +2. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10106 | Hybrid Inverter & PV Inverter | Overvoltage secondary protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the secondary protection time for overvoltage = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10107 | Hybrid Inverter & PV Inverter | Under-frequency first-level protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the first-level protection time for under-frequency = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10108 | Hybrid Inverter & PV Inverter | Underfrequency secondary protection value | 50Hz grid range: [4500-4996]Hz, 60Hz Non-North American national grid range: [5500-5996]Hz, 60Hz North American national grid range: [5000-5996]Hz |
| 10109 | Hybrid Inverter & PV Inverter | Under-frequency secondary protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the secondary protection time for underfrequency = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10110 | Hybrid Inverter & PV Inverter | Over-frequency first-level protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the first-level protection time for overfrequency = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10111 | Hybrid Inverter & PV Inverter | Over-frequency secondary protection value | 50Hz power grid range: [5004-5500]Hz; 60Hz power grid range: [6004-6600]Hz; |
| 10112 | Hybrid Inverter & PV Inverter | Over-frequency secondary protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the secondary protection time for overfrequency = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10113 | Hybrid Inverter & PV Inverter | Under-voltage level three protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the three-level under-voltage protection time = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10114 | Hybrid Inverter & PV Inverter | Overvoltage level three protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the three-level overvoltage protection time = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10115 | Hybrid Inverter & PV Inverter | Under-frequency third-level protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the third-level protection time for under-frequency = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10116 | Hybrid Inverter & PV Inverter | Over-frequency three-level protection time | Range: [1-1440,000]s; Range dependence: The lower limit of the time range for abnormal protection of the power grid, the minimum value of the three-level protection time for overfrequency = the lower limit of the time range for abnormal protection of the power grid. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10117 | Hybrid Inverter & PV Inverter | Under-voltage level three protection value | Range dependence: Rated grid voltage, maximum value of undervoltage three-level protection = rated grid voltage -1, minimum value of undervoltage three-level protection = rated grid voltage \*0.05; The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10118 | Hybrid Inverter & PV Inverter | Overvoltage level three protection value | Range dependence: Rated grid voltage, maximum overvoltage three-level protection value = rated grid voltage \*1.4, minimum overvoltage three-level protection value = rated grid voltage +2. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10119 | Hybrid Inverter & PV Inverter | Under-frequency three-level protection value | 50Hz grid range: [4500-4996]Hz, 60Hz. Non-north American country range: [5500-5996]Hz, 60Hz. North American country grid range: [5000-5996]Hz. The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10120 | Hybrid Inverter & PV Inverter | Overfrequency level three protection value | 50Hz power grid range: [4500-4996]Hz, 60Hz national range: [5500-5996]Hz; The power grid company provides standard default Settings, which generally do not need to be changed. |
| 10307 | Communication Model | Modbus TCP 502 port switch | Issue the enumeration values: 1 = Open, 0 = Close |

**Note:**

Please refer to the external communication protocols for inverters to determine the coefficients.

When switching EMS modes through the API, make sure to send the heartbeat signal simultaneously.
