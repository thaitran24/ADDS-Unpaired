import torch.nn as nn

class FCDiscriminator(nn.Module):
	def __init__(self, num_classes, ndf = 64):
		super(FCDiscriminator, self).__init__()
		self.conv1 = nn.Conv2d(num_classes, ndf, kernel_size=4, stride=2, padding=1)
		self.conv2 = nn.Conv2d(ndf, ndf*2, kernel_size=4, stride=2, padding=1)
		self.conv3 = nn.Conv2d(ndf*2, ndf*4, kernel_size=4, stride=1, padding=1)
		self.conv4 = nn.Conv2d(ndf*4, ndf*8, kernel_size=4, stride=1, padding=1)
		self.pool = nn.AdaptiveAvgPool2d((1, 1))
		self.leaky_relu = nn.LeakyReLU(negative_slope=0.2, inplace=True)
		self.norm = nn.BatchNorm2d(ndf*8)
		self.flatten = nn.Flatten()
		self.linear = nn.Linear(ndf*8, 1)
		self.activation = nn.Sigmoid()

	def forward(self, x):
		x = self.conv1(x)
		x = self.leaky_relu(x)		
		x = self.conv2(x)
		x = self.leaky_relu(x)
		x = self.conv3(x)
		x = self.leaky_relu(x)
		x = self.conv4(x)
		# x = self.leaky_relu(x)
		# x = self.pool(x)
		# x = self.norm(x)
		# x = self.flatten(x)
		# x = self.linear(x)
		# x = self.activation(x)
		return x