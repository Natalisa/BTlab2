import math
import matplotlib.pyplot as plt
# IEE 802.11n

#Исходные данные:
PowerTxAs   =   20#мощность пеередатчика точки доступа WiFi дБ
PowerTxUs   =   20#мощность пеередатчика пользовательского терминала дБ
Gain        =   6#коэф усиления антены точки доступа дБи
ClutterLosses = 12#запас мощности сигнала на проникновения сквозь стены дБ
InterMargin =   5#запас мощности на интерференцию дБ
#модель распростронения сигнала UMiNLOS
BW24        =   2.4#диапазон частот ГГц
BW5         =   5
BWul        =   15#полоса частот в UL МГц
BWdl        =   20#полоса частот в DL МГц
NoiseFigureAp = 5#коэф шума приемника точки доступа дБ
NoiseFigureUs = 8#коэф шума приемника пользователя дБ
RequiredSINRdl= 17#требуемой отношение SINR для DL дБ 36.7
RequiredSINRul= 15#требуемой отношение SINR для UL дБ

def ThermNoise(BW):
    return -174 + 10*math.log10(BW*pow(10,6))

#чуствительность приемного устройства пользователя в DownLink
RxSensDl = ThermNoise(BWdl) + NoiseFigureUs + RequiredSINRdl
print("RxSensDl",RxSensDl)

#чуствительность приемного устройства пользователя в UpLink
RxSensUl = ThermNoise(BWul) + NoiseFigureUs + RequiredSINRul
print("RxSensUl",RxSensUl)

#расчет уровня допустимых потерь радио сигнла
# при котором возможно декодирование
Loss=0#дБ
MAPLdl = PowerTxAs - Loss + Gain - RxSensDl - InterMargin - ClutterLosses
MAPLul = PowerTxUs - Loss - RxSensUl - InterMargin - ClutterLosses
print("MAPLdl",MAPLdl,"MAPLul",MAPLul)
def PL(d):
    return 26*math.log10(BW5) + 22.7 + 36.7*math.log10(d)
d=pow(10,((MAPLul-26*math.log10(BW5) - 22.7 )/ 36.7))
print(d)
d=pow(10,((MAPLdl-26*math.log10(BW5) - 22.7 )/ 36.7))
print(d)
d=range(1,30)
PLmas = list(map(PL,d))
print(PLmas)
#for i in range(40,50):
#     print(PL(i))
#print(PLmas)

plt.plot(d,PLmas)
plt.hold
plt.plot([MAPLdl for x in d], label="DL")
plt.plot([MAPLul for x in d], label="UL")
plt.legend()
print(PL(MAPLdl),PL(MAPLul))
plt.show()
