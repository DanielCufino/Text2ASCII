from torch.utils.data import Dataset
import json

class ASCIIDataset(Dataset):
    def __init__(self, path, tokenizer):
        self.data = json.loads(open(path), "r")

        self.X = []

        for entry in self.data:
            self.X.append(entry['prompt'])

        

        self.X_encoded = tokenizer(self.X, truncation=True, padding="max_length", return_tensors="pt")
        self.input_ids = self.X_encoded['input_ids']
        self.attention_mask = self.X_encoded['attention_mask']

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return (self.input_ids[idx], self.attention_mask[idx])

    
ds = ASCIIDataset('./raw_data.json', )