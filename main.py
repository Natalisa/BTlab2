import math
import numpy as np
import matplotlib.pyplot as plt
# IEE 802.11n

#Исходные данные:
PowerTxAs   =   20#мощность пеередатчика точки доступа WiFi дБ
PowerTxUs   =   20#мощность пеередатчика пользовательского терминала дБ
Gain        =   5#коэф усиления антены точки доступа дБи
ClutterLosses = 12#запас мощности сигнала на проникновения сквозь стены дБ
InterMargin =   5#запас мощности на интерференцию дБ
#модель распростронения сигнала UMiNLOS
BW24        =   2.4#диапазон частот ГГц
BW5         =   5
BWul        =   15#полоса частот в UL МГц
BWdl        =   20#полоса частот в DL МГц
NoiseFigureAp = 5#коэф шума приемника точки доступа дБ
NoiseFigureUs = 8#коэф шума приемника пользователя дБ
RequiredSINRdl= 17#требуемой отношение SINR для DL дБ
RequiredSINRul= 15#требуемой отношение SINR для UL дБ

def ThermNoise(BW):
    return -174 + 10*math.log10(BW)

#чуствительность приемного устройства пользователя в DownLink
RxSensDl = ThermNoise(BWdl) + NoiseFigureUs +RequiredSINRdl
print(RxSensDl)

#чуствительность приемного устройства пользователя в UpLink
RxSensUl = ThermNoise(BWul) +NoiseFigureUs +RequiredSINRul
print(RxSensUl)

#нехватате Lossfor/g откда взять?
MAPLdl = PowerTxAs + Gain - RxSensDl - InterMargin - ClutterLosses
MAPLul = PowerTxUs  - RxSensUl - InterMargin - ClutterLosses

def PL(d):
    return 26*math.log10(BW5) + 22.7 + 36.7*math.log10(d)

d=range(1,1500)
PLmas = list(map(PL,d))
print(PLmas)

plt.plot(d,PLmas)
plt.hold
plt.plot([MAPLdl for x in d])
plt.plot([MAPLul for x in d])
print(PL(MAPLdl),PL(MAPLul))
plt.show()