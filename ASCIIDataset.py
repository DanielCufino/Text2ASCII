from torch.utils.data import Dataset
import json

from transformers import GPT2LMHeadModel, GPT2Tokenizer
from torch.optim import Adam
from torch.utils.data import DataLoader
import tqdm
import torch

class ASCIIDataset(Dataset):
    def __init__(self, path, tokenizer):
        self.data = None

        self.X = []

        with open(path, 'r') as file:
            self.data = json.load(file)
            for entry in self.data:
                prompt = entry['prompt']
                text = entry['text']
                self.X.append(f'<BOS> {prompt}\n<RES>:\n{text}\n<EOS>')
            # print(test[0])

        # for entry in self.data:
        #     prompt = entry['prompt']
        #     text = entry['text']
        #     self.X.append(f'<BOS> {prompt} <bot>: {text} <EOS>')
        
        print("Tokenizing Text...")
        self.X_encoded = tokenizer(self.X, truncation=True, padding="max_length", return_tensors="pt")
        self.X_encoded = self.X_encoded.to(device)
        print("Done Tokenizing.")
        self.input_ids = self.X_encoded['input_ids']
        self.attention_mask = self.X_encoded['attention_mask']
        self.lens = []
        for item in self.attention_mask:
            self.lens.append(len(item))
        print(max(self.lens))

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return (self.input_ids[idx], self.attention_mask[idx])
        # return (self.X[idx])

    def decode(self, tokens):
        return tokenizer.decode(tokens)

def train(model, optimizer, dataloader):
 
    e = 10

    for _ in tdqm(range(e)):
        for b, a in dataloader:
            
            optimizer.zero_grad()

            loss = model(b, attention_mask=a, labels=a).loss()

            loss.backward()

            optim.step()

        torch.save(model.state_dict(), "model_state.pt")


        break

device = "cpu"

def prompt(prompt, text):
    inp = f'<BOS> {prompt}\n<RES>:\n{text}\n<EOS>'
    inp = tokenizer(inp, return_tensors="pt")
    x = inp["input_ids"].to(device)
    a = inp["attention_mask"].to(device)
    output = model.generate(x, attention_mask=a)
    output = tokenizer.decode(output[0])
    return output


tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.add_special_tokens({"pad_token": "<pad>", 
                                "bos_token": "<BOS>",
                                "eos_token": "<EOS>"})
tokenizer.add_tokens(["<RES>:"])

model = GPT2LMHeadModel.from_pretrained("gpt2")
model.resize_token_embeddings(len(tokenizer))
print(len(tokenizer))

optim = Adam(model.parameters())

# model = model.to(device)

# print(tokenizer.decode(model.generate(**tokenizer("hey i was good at basketball but ",
#                          return_tensors="pt"))[0]))

ASCII_DATA = ASCIIDataset("./raw_data.json", tokenizer)

print(ASCII_DATA[0])
print(ASCII_DATA[1])
# print(len(ASCII_DATA))
# print(max(ASCII_DATA.attention_mask, lambda x: x.size(0)))
# chatData =  DataLoader(chatData, batch_size=64)
    
dataloader = ASCIIDataset('./raw_data.json', batch_size=64)


