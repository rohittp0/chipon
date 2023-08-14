from torch import nn

import layers
from constants import test_bench_template


class Model:
    def __init__(self, model: nn.Sequential):
        self.model = model
        self.layers = []

    def __str__(self):
        return '\n'.join(str(layer) for layer in self.layers)

    def parse_layers(self):
        for i, layer in enumerate(self.model):
            if isinstance(layer, nn.Linear):
                self.layers.append(layers.Linear.layer_from(layer, i))
            elif isinstance(layer, nn.ReLU):
                self.layers.append(layers.ReLU(self.model[i - 1].out_features, i))
            else:
                raise ValueError(f'Unknown layer type {layer}')

    def emit(self):
        out = ["`timescale 1ns / 1ps"]

        top = [
            "module top(in, out);",
            f"    input [{self.layers[0].shape[0] -1}:0] in;",
            f"    output [{self.layers[-1].shape[-1] -1}:0] out;\n"
        ]

        for i, layer in enumerate(self.layers):
            out.append(layer.emit())
            top.append(f"    wire [{layer.shape[-1] - 1}:0] layer_{i}_out;")

            if i == 0:
                top.append(f"    {layer.name} layer_{i}(in, layer_{i}_out);")
            else:
                top.append(f"    {layer.name} layer_{i}(layer_{i - 1}_out, layer_{i}_out);")

        top.append(f"\n    assign out = layer_{len(self.layers) - 1}_out;")
        top.append("endmodule")

        out.append('\n'.join(top))

        return '\n'.join(out)

    def emit_test_bench(self):
        return test_bench_template.format(input_length=2 ** self.layers[0].shape[0])


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
    code = model.emit()

    with open('test.v', 'w') as f:
        f.write(code)

    with open('test_tb.v', 'w') as f:
        f.write(model.emit_test_bench())


if __name__ == '__main__':
    test()
