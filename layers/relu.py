class ReLU:

    def __init__(self, shape: int):
        self.shape = shape
        self.name = f'relu_{shape}'

    def __str__(self):
        return f'ReLU({self.shape})'

    def emit(self):
        """
        Emit the Verilog code for this layer
        :return:
        """

        relu_code = [f'assign out[{i}] = in[{i}] > 0 ? in[{i}] : 0;\n' for i in range(self.shape)]

        return f"""
module {self.name}(in, out);
    input [{self.shape - 1}:0] in;
    output [{self.shape - 1}:0] out;
            
    @always @(in) 
    begin
        {"        ".join(relu_code)}
    end
endmodule
"""
