# models/model_samsung.py

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import FinanceDataReader as fdr
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tqdm.auto import tqdm
import torchinfo
import pickle


# LSTM 모델 클래스 정의
class LSTMModelsk(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMModelsk, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.dropout1 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(hidden_size, 64)
        self.relu = nn.ReLU()
        self.dropout2 = nn.Dropout(0.5)
        self.fc2 = nn.Linear(64, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.dropout1(out[:, -1, :])
        out = self.fc1(out)
        out = self.relu(out)
        out = self.dropout2(out)
        out = self.fc2(out)
        return out

def load_data_sk():
    sam = fdr.DataReader('034730')
    del sam['Change']
    sam.columns = ['시가', '고가', '저가', '종가', '거래량']
    sam['종가2'] = sam['종가']
    begins_2022 = sam.index.get_loc('2022-01-03')
    scaler = StandardScaler()
    sam.iloc[:, 0:5] = scaler.fit_transform(sam.iloc[:, 0:5])

    window_size = 8
    x = []
    y = []
    for i in range(len(sam) - window_size):
        x.append(sam.iloc[i:i+window_size, 0:5])
        y.append(sam.iloc[i+window_size, 5])

    x = np.array(x)
    y = np.array(y)
    split_point = begins_2022 - window_size

    x_train = x[:split_point]
    x_test = x[split_point:]
    y_train = y[:split_point]
    y_test = y[split_point:]

    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, shuffle=True)

    x_train = torch.FloatTensor(x_train)
    y_train = torch.FloatTensor(y_train)
    x_val = torch.FloatTensor(x_val)
    y_val = torch.FloatTensor(y_val)
    x_test = torch.FloatTensor(x_test)
    y_test = torch.FloatTensor(y_test)

    return x_train, x_val, x_test, y_train, y_val, y_test, sam.index[sam.index >= '2022-01-03']

def predict_stock_sk():
    x_train, x_val, x_test, y_train, y_val, y_test, days_2022 = load_data_sk()

    model = LSTMModelsk(input_size=5, hidden_size=64, output_size=1)
    criterion = nn.L1Loss()
    optimizer = optim.Adam(model.parameters(), lr=0.1)
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.5)

    num_epochs = 150
    best_val_loss = float('inf')
    patience = 20
    counter = 0

    # for epoch in tqdm(range(num_epochs), desc="epoch", position=0):
    #     model.train()
    #     for batch_x, batch_y in DataLoader(TensorDataset(x_train, y_train), batch_size=32, shuffle=True):
    #         optimizer.zero_grad()
    #         outputs = model(batch_x)
    #         loss = criterion(outputs.squeeze(), batch_y)
    #         loss.backward()
    #         optimizer.step()

    #     model.eval()
    #     with torch.no_grad():
    #         val_loss = 0
    #         for batch_x, batch_y in DataLoader(TensorDataset(x_val, y_val), batch_size=32):
    #             outputs = model(batch_x)
    #             val_loss += criterion(outputs.squeeze(), batch_y).item()
    #         val_loss /= len(DataLoader(TensorDataset(x_val, y_val), batch_size=32))

    #     if val_loss < best_val_loss:
    #         best_val_loss = val_loss
    #         torch.save(model.state_dict(), 'best_model_sk.pth')
    #         counter = 0
    #     else:
    #         counter += 1
    #         if counter >= patience:
    #             break

    model.load_state_dict(torch.load('best_model_sk.pth'))
    # pickle.dump(model, open('model.pickle', 'wb'))
    model.eval()
    with torch.no_grad():
        y_pred = model(x_test).squeeze().detach().numpy()

    return y_pred, y_test, days_2022

