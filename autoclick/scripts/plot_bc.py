import imp
from math import ceil
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./autoclick/files/bcoin_log_file.csv', sep=";")

df = df[df.bcoin != -1]
df['timestamp'] = df['timestamp'].transform(lambda ts: datetime.fromtimestamp(ts))

df = df[df.timestamp >= datetime.strptime("2022-01-29 22:00:00", "%Y-%m-%d %H:%M:%S")]

duration = (df.iloc[-1].timestamp - df.iloc[0].timestamp).seconds/3600
bcoin_farm = df.iloc[-1].bcoin - df.iloc[0].bcoin
farm_hora = bcoin_farm/duration
print("duração", round(duration, 2))
print("farm total", round(bcoin_farm, 2))
print("farm/hora", round(farm_hora, 2))
print("farm/dia", round(farm_hora*24, 2))
print("farm/semana", round(farm_hora*24*7, 2))

time_to_target = ceil((155-df.iloc[-1].bcoin)/farm_hora/24)
print("ttt: (155 bcoin)", time_to_target, "dias")