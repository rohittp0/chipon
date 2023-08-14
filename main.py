from torch import nn

import layers


class Model:
    def __init__(self, model: nn.Sequential):
        self.model = model
        self.layers = []

    def __str__(self):
        return '\n'.join(str(layer) for layer in self.layers)

    def parse_layers(self):
        for i, layer in enumerate(self.model):
            if isinstance(layer, nn.Linear):
                self.layers.append(layers.Linear.layer_from(layer))
            elif isinstance(layer, nn.ReLU):
                self.layers.append(layers.ReLU(self.model[i - 1].out_features))
            else:
                raise ValueError(f'Unknown layer type {layer}')

    def emit(self):
        return '\n'.join(layer.emit() for layer in self.layers)


def test():
    simple_model = nn.Sequential(
        nn.Linear(2, 2),
        nn.ReLU(),
        nn.Linear(2, 2),
        nn.ReLU(),
        nn.Linear(2, 1),
    )

    model = Model(simple_model)
    model.parse_layers()

    print(model)
    print(model.emit())


if __name__ == '__main__':
    test()
