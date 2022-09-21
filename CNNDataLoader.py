import torch
import pandas as pd
from torch.utils.data import Dataset, DataLoader

class CNNDataLoader(Dataset):
    
    def __init__(self, label_pickle, input_pickle):
        """
        Args:
            input_pickle (string): Directory with to pickle file processed tensor data
            master_file (string): Path to the master csv file with annotations. Column 'kd\ki' has labels.
        """
        
        self.labels = torch.load(label_pickle)
        self.torch_obj = torch.load(input_pickle)
                
    def __len__(self):
           return len(self.master_file)
    
    def __getitem__(self, i):
        
        sample = (self.torch_obj[i, :, :, :, :]).to_dense()
        label = self.labels[i]

        return sample, label



if __name__ == "__main__":
    
    #Create instance of our custom dataset
    dataset = CNNDataLoader(label_pickle = r"C:\Users\ogarland\Desktop\GenModels\Testing Files\dataloader_test.pt",
                            input_pickle = r'C:\Users\ogarland\Desktop\GenModels\Testing Files\tensor.pt')
    
    #Initiate the dataloader
    data = DataLoader(dataset, batch_size=4, shuffle=True)

    #Make calls to the dataloader
    for tensor_batch, label_batch in data:
        print("Batch of tensors has shape: ", tensor_batch.shape)
        print("Batch of labels has shape: ", label_batch.shape)