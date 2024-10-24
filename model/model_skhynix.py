import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import FinanceDataReader as fdr
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import os


# LSTM 모델 클래스 정의
class LSTMModelskhynix(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMModelskhynix, self).__init__()
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

def preprocess_and_save_data_skhynix(save_path='skhynix_preprocessed_data.pkl'):
    sam = fdr.DataReader('000660')  # 데이터 불러오기
    del sam['Change']  # Change 열 삭제
    sam.columns = ['시가', '고가', '저가', '종가', '거래량']  # 열 이름 변경
    sam['종가2'] = sam['종가']  # 종가2 열 추가
    
    # 데이터 전처리 (스케일링)
    scaler = StandardScaler()
    sam.iloc[:, 0:5] = scaler.fit_transform(sam.iloc[:, 0:5])

    # 윈도우 사이즈 정의
    window_size = 8
    x = []
    y = []
    for i in range(len(sam) - window_size):
        x.append(sam.iloc[i:i+window_size, 0:5])
        y.append(sam.iloc[i+window_size, 5])

    # 배열로 변환
    x = np.array(x)
    y = np.array(y)

    # 전처리된 데이터를 저장
    with open(save_path, 'wb') as f:
        pickle.dump((x, y, sam.index), f)
    
    return x, y, sam.index

def load_data_skhynix(save_path='skhynix_preprocessed_data.pkl'):
    if not os.path.exists(save_path):
        print("Preprocessed data not found, preprocessing...")
        x, y, index = preprocess_and_save_data_skhynix(save_path)
    else:
        print("Loading preprocessed data...")
        with open(save_path, 'rb') as f:
            x, y, index = pickle.load(f)
    
    # 데이터 분할
    begins_2022 = np.where(index == '2022-01-03')[0][0]
    window_size = 8
    split_point = begins_2022 - window_size

    x_train = x[:split_point]
    x_test = x[split_point:]
    y_train = y[:split_point]
    y_test = y[split_point:]

    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, shuffle=True)

    # Tensor로 변환
    x_train = torch.FloatTensor(x_train)
    y_train = torch.FloatTensor(y_train)
    x_val = torch.FloatTensor(x_val)
    y_val = torch.FloatTensor(y_val)
    x_test = torch.FloatTensor(x_test)
    y_test = torch.FloatTensor(y_test)

    return x_train, x_val, x_test, y_train, y_val, y_test, index[index >= '2022-01-03']

def predict_stock_skhynix():
    x_train, x_val, x_test, y_train, y_val, y_test, days_2022 = load_data_skhynix()

    model = LSTMModelskhynix(input_size=5, hidden_size=64, output_size=1)
    model.load_state_dict(torch.load('best_model_skhynix.pth'))
    model.eval()

    with torch.no_grad():
        y_pred = model(x_test).squeeze().detach().numpy()

    return y_pred, y_test, days_2022
