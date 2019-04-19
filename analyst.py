import pandas as pd
import numpy as np
import banpei
from tqdm import tqdm
import matplotlib.pyplot as plt

from util import parser

ALL_CPU_ID = -2
ALL_SYSTEM_NAME = 'all'

args = parser.parse_args()

def analyst(args):
    ALL_CPU_ID = -2
    ALL_SYSTEM_NAME = 'all'
    data = pd.read_csv(args.path)

    if args.cpu_id != ALL_CPU_ID:
        data = data[data['cpu_id']==args.cpu_id]
    if args.system_name != ALL_SYSTEM_NAME:
        data = data[data['system_name']==args.system_name]

    y = data[args.target]

    model = banpei.SST(w=50)
    results = model.detect(y, is_lanczos=True)
    start = args.start
    length = args.length
    total_length = len(y)

    while True:

        end = start + length
        end = end if end < total_length else total_length
        origin = y.iloc[start:end]
        result = results[start:end]
        x = range(start, end)

        plt.subplot(211)
        plt.plot(x, origin)
        plt.subplot(212)
        plt.plot(x, result)
        name = args.system_name + '_' + str(args.cpu_id) + '_' + str(start) + '_' + str(end) + '.png'
        plt.savefig('analyst/' + name)
        plt.close()

        start = end
        if end == total_length:
            break


if __name__ == "__main__":
    analyst(args)