import sys
import os
import crypten
import torch
from crypten.config import cfg

rank = sys.argv[1]
os.environ["RANK"] = str(rank)
os.environ["WORLD_SIZE"] = str(2)
os.environ["MASTER_ADDR"] = '127.0.0.1'
os.environ["MASTER_PORT"] = "30007"
os.environ["RENDEZVOUS"] = "env://"
os.environ["GLOO_SOCHET_IFNAME"] = 'ens81np0'

crypten.init()
cfg.communicator.verbose = True
commInit = crypten.communicator.get().get_communication_stats()

x = torch.tensor([1.0, 2.0, 3.0])
x_enc = crypten.cryptensor(x, src = 1)
print("x_enc:", x_enc)
x_dec = x_enc.get_plain_text()
y = torch.tensor([2.0, 3.0, 4.0])
y_enc = crypten.cryptensor(y, src = 0)
print("y_enc:", y_enc)
sum_xy = x_enc + y_enc
sum_xy_dec = sum_xy.get_plain_text()
print("sum:", sum_xy_dec)
