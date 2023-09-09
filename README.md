# PyTorch to Verilog Transpiler

This project is a PyTorch to Verilog transpiler, designed to convert neural network models created in PyTorch into hardware description language (HDL) code written in Verilog. This conversion allows for the deployment of machine learning models on hardware accelerators such as FPGAs, enabling real-time inference at low power consumption.

## Overview

The PyTorch to Verilog transpiler takes a PyTorch model, represented as an instance of `nn.Sequential`, and converts it into Verilog code that can be synthesized and deployed on FPGA or other hardware platforms. The generated Verilog code represents the neural network as a hardware module, enabling efficient and low-latency inference.

## Features

- Conversion of PyTorch `nn.Linear` layers to Verilog hardware modules.
- Conversion of PyTorch `nn.ReLU` activation layers to Verilog hardware modules.
- Automatic generation of Verilog code for the entire model.
- Modular design for easy extension to support more layer types and configurations.

## Prerequisites

Before using this transpiler, make sure you have the following prerequisites installed:

- PyTorch: The PyTorch deep learning framework for defining and training neural networks.
- Python: The Python programming language, used to run the transpiler script.
- FPGA Development Tools (if deploying on FPGA): Necessary tools and hardware to compile and deploy Verilog code on FPGA platforms.

## Usage

1. **Define Your PyTorch Model**: Create your neural network model using PyTorch's `nn.Sequential`. Configure the model architecture by adding `nn.Linear` and `nn.ReLU` layers as needed.

2. **Instantiate the Transpiler**: Create an instance of the `Model` class, passing your PyTorch model as an argument.

3. **Parse Layers**: Call the `parse_layers` method on the transpiler object to analyze the PyTorch model and generate a list of equivalent hardware layers.

4. **Generate Verilog Code**: Use the `emit` method to generate Verilog code for the entire model, including input and output interfaces.

5. **Test Bench Generation**: Optionally, you can use the `emit_test_bench` method to generate a test bench template in Verilog for simulating and testing your model.

6. **Save Verilog Code**: Save the generated Verilog code to a `.v` file, e.g., `test.v`, using standard file I/O operations.

7. **Compile and Deploy (FPGA)**: If your goal is to deploy the model on FPGA hardware, you will need to use FPGA development tools to compile the Verilog code and program the FPGA.

## Example

The provided `test` function demonstrates how to use the transpiler to convert a simple PyTorch model into Verilog code. You can modify this function and the PyTorch model to match your specific requirements.

## Files and Directories

- `transpiler.py`: Contains the main transpiler code.
- `layers.py`: Provides Verilog layer representations for supported PyTorch layers.
- `constants.py`: Contains constants and templates used in the project.
- `test.v`: The generated Verilog code for your model.
- `test_tb.v`: The generated Verilog test bench for simulating your model (optional).

## Contributing

Contributions to this project are welcome! Please feel free to open issues or submit pull requests to improve the transpiler or add support for additional PyTorch layer types.

Thank you for using the PyTorch to Verilog Transpiler!
