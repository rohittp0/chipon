import numpy as np


class Linear:
    @classmethod
    def layer_from(cls, layer, index: int):
        return cls(layer.in_features, layer.out_features, layer.weight.detach().numpy().T, layer.bias.detach().numpy(),
                   index)

    def __init__(self, in_features: int, out_features: int, weight: np.ndarray, bias: np.ndarray, index: int):
        self.in_features = in_features
        self.out_features = out_features

        self.bias = bias
        self.weight = weight

        self.verify_weights()

        self.name = f'layer_{index}_linear_{str(self.in_features)}_{str(self.out_features)}'
        self.shape = (self.in_features, self.out_features)

    def __str__(self):
        return f'Linear({self.in_features} -> {self.out_features})'

    def verify_weights(self):
        if self.weight is None:
            raise ValueError('Weight is not defined')

        bias_shape = (self.out_features,)
        weight_shape = (self.in_features, self.out_features)

        if self.weight.shape != weight_shape:
            raise ValueError(f'Weight shape is not correct, expected {weight_shape}, got {self.weight.shape}')

        if self.bias is not None and self.bias.shape != bias_shape:
            raise ValueError(f'Bias shape is not correct, expected {bias_shape}, got {self.bias.shape}')

    def emit(self):
        """
        Emit Verilog code for this layer
        :return: Verilog code
        """

        add_bias = [f'add[{i}] = mul[{i}] + {self.bias[i]};\n' for i in range(self.out_features)]
        multiply_weight = []

        for i in range(self.out_features):
            for j in range(self.in_features):
                multiply_weight.append(f"mul[{i}] = mul[{i}] + in[{j}] * {self.weight[j][i]};\n")

        return f"""
module {self.name}(in, out);
    input [{self.in_features - 1}:0] in;
    output [{self.out_features - 1}:0] out;
    
    reg [{self.out_features - 1}:0] mul;
    reg [{self.out_features - 1}:0] add;
    
    reg [{self.out_features - 1}:0] out;
    
    always @(in)
    begin
        {'        '.join(multiply_weight)}
        {'        '.join(add_bias)}
        
        out = add;
    end
endmodule
"""
