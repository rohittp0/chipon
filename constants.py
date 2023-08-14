test_bench_template = """`timescale 1ns / 1ps

module tb_top;
    reg [1:0] in;
    wire [0:0] out;
    
   localparam INPUT_LENGTH = {input_length};
    
    integer i;

    top dut(
        .in(in),
        .out(out)
    );

    initial begin
        $dumpfile("tb_top.vcd");
        $dumpvars(0, tb_top);
        
        // Wait a bit before starting simulation
        #2;
        
        // Iterate through different input values
        for (i = 0; i < INPUT_LENGTH; i = i + 1) begin
            in = i[1:0];

            // Perform test
            $display("Input: in = %b", in);
            #1;
        end

        $finish;
    end
endmodule
"""
