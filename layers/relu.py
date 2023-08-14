class ReLU:

    def __init__(self, shape: int, index: int):
        self.shape = (shape,)
        self.name = f'layer_{index}_relu_{shape}'

    def __str__(self):
        return f'ReLU({self.shape})'

    def emit(self):
        """
        Emit the Verilog code for this layer
        :return:
        """

        relu_code = [f'out[{i}] = in[{i}] > 0 ? in[{i}] : 0;\n' for i in range(self.shape[0])]

        return f"""
module {self.name}(in, out);
    input [{self.shape[0] - 1}:0] in;
    output [{self.shape[0] - 1}:0] out;
    reg [{self.shape[0] - 1}:0] out;
            
    always @(in) 
    begin
        {"        ".join(relu_code)}
    end
endmodule
"""
