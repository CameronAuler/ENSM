import torch
import torch.nn as nn
import torch.nn.functional as F

class LeakyReLUModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(LeakyReLUModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, num_classes)
        
    def forward(self, x):
        x = F.leaky_relu(self.fc1(x), negative_slope=0.01)
        x = self.fc2(x)
        return x
    
# Define the model, loss function and optimizer
model = LeakyReLUModel(input_size=64, hidden_size=128, num_classes=10)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Train the model
for epoch in range(100):
    # Train the model with some sample data
    optimizer.zero_grad()
    outputs = model(sample_data)
    loss = criterion(outputs, sample_labels)
    loss.backward()
    optimizer.step()
    
    # Print the loss for each epoch
    if (epoch + 1) % 10 == 0:
        print('Epoch [{}/100], Loss: {:.4f}'.format(epoch+1, loss.item()))
        
# Analyze the logs
def analyze_logs(log_file):
    with open(log_file, 'r') as f:
        logs = f.readlines()
        
    # Extract the loss from each epoch
    loss_values = [float(log.split(',')[1].strip().split(':')[1]) for log in logs]
    
    # Plot the loss
    import matplotlib.pyplot as plt
    plt.plot(loss_values)
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Loss vs Epochs')
    plt.show()
    
    # Calculate the average loss
    avg_loss = sum(loss_values) / len(loss_values)
    print('Average Loss: {:.4f}'.format(avg_loss))

# Give a comprehensive report
def generate_report(log_file):
    analyze_logs(log_file)
    print('The Leaky ReLU AI model has been trained for 100 epochs.')
    print('The final loss after training is {:.4f}'.format(loss.item()))
    print('The average loss over all epochs is {:.4f}'.format(avg_loss))