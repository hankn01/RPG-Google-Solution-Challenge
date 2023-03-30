from collections import OrderedDict

config = OrderedDict()

config['batch_size'] = 32
config['image_size'] = 224
config['epochs'] = 10

# Model Parameters
config['block'] = 'Basic'
config['base_channel'] = 64
config['num_layer'] = [2,2,2,2]