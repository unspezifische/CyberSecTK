import os
import numpy as np
from sklearn.model_selection import train_test_split
from cybersectk.iot import iot

# Specify the directory path where the PCAP files are located
pcap_directory = './pcap_files'

# Create an empty list to hold the features from all PCAP files
all_features = []

# Iterate through each file in the directory
for filename in os.listdir(pcap_directory):
    if filename.endswith('.pcap'):
        # Construct the full file path
        file_path = os.path.join(pcap_directory, filename)

        # Call the iot() function with the file path
        # Use the default ip_filter settings
        data = iot(file_path)

        # Append the features from this PCAP file to the all_features list
        all_features.append(data)

# After processing all files, convert the list of arrays to a single numpy array
all_features = np.concatenate(all_features, axis=0)

# Split the data into features and labels
X = all_features[:, :-1]
y = all_features[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check if TensorFlow is installed
try:
    import tensorflow as tf
    from tensorflow.keras import Sequential
    from tensorflow.keras.layers import Dense
    print("TensorFlow is installed.")

    # Normalize the feature data
    X_train = tf.keras.utils.normalize(X_train, axis=1)
    X_test = tf.keras.utils.normalize(X_test, axis=1)

    # Define the model
    model = Sequential()
    model.add(Dense(32, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=10, batch_size=32)

    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test accuracy: {accuracy}')
except ImportError:
    print("TensorFlow is not installed.")

# Check if PyTorch is installed
try:
    import torch
    from torch import nn, optim
    from torch.utils.data import DataLoader, TensorDataset
    print("PyTorch is installed.")

    # Convert the data to PyTorch tensors
    X_train = torch.FloatTensor(X_train)
    y_train = torch.FloatTensor(y_train)
    X_test = torch.FloatTensor(X_test)
    y_test = torch.FloatTensor(y_test)

    # Create data loaders
    train_data = TensorDataset(X_train, y_train)
    train_loader = DataLoader(train_data, batch_size=32)
    test_data = TensorDataset(X_test, y_test)
    test_loader = DataLoader(test_data, batch_size=32)

    # Define the model
    model = nn.Sequential(
        nn.Linear(X_train.shape[1], 32),
        nn.ReLU(),
        nn.Linear(32, 16),
        nn.ReLU(),
        nn.Linear(16, 1),
        nn.Sigmoid()
    )

    # Define the loss function and the optimizer
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters())

    # Train the model
    for epoch in range(10):
        for inputs, labels in train_loader:
            # Zero the parameter gradients
            optimizer.zero_grad()

            # Forward pass
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            # Backward pass and optimization
            loss.backward()
            optimizer.step()

    # Evaluate the model
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            predicted = (outputs > 0.5).float()
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'Test accuracy: {correct / total}')
except ImportError:
    print("PyTorch is not installed.")