from ASCIIDataset import ASCIIDataset

from torch.utils.data import Dataset
import json

from transformers import GPT2LMHeadModel, GPT2Tokenizer
from torch.optim import Adam
from torch.utils.data import DataLoader
import tqdm
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.add_special_tokens({"pad_token": "<pad>", 
                                "bos_token": "<BOS>",
                                "eos_token": "<EOS>"})
tokenizer.add_tokens(["<RES>:"])

model = GPT2LMHeadModel.from_pretrained("gpt2")
model.resize_token_embeddings(len(tokenizer))

# model = model.to(device)

# print(tokenizer.decode(model.generate(**tokenizer("hey i was good at basketball but ",
#                          return_tensors="pt"))[0]))

ASCII_DATA = ASCIIDataset("./raw_data.json", tokenizer)

inp = ASCII_DATA[0]

print(inp)

test = tokenizer(inp)

print(test)

print(len(test['input_ids']))

# print(inp)