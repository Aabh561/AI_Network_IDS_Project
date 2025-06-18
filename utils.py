import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def preprocess_log(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['packet_size'] = df['packet_size'].astype(int)
    df['src_ip_encoded'] = df['src_ip'].astype('category').cat.codes
    df['dst_ip_encoded'] = df['dst_ip'].astype('category').cat.codes
    label_encoder = LabelEncoder()
    df['attack_type_encoded'] = label_encoder.fit_transform(df['attack_type'])
    features = df[['packet_size', 'src_ip_encoded', 'dst_ip_encoded']]
    scaler = MinMaxScaler()
    features_scaled = scaler.fit_transform(features)
    return features_scaled, df['attack_type_encoded']
