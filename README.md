RTL Testbench Generator 🚀

Overview

rtl-testbench-gen is a Python-based tool that automatically generates SystemVerilog testbenches for different types of RTL modules.It simplifies the process of writing testbenches by dynamically generating them based on module type and user-defined ports.

Why Use This?

✅ Saves time by automating testbench creation
✅ Supports multiple hardware types (ALU, FSM, Memory, UART, Generic)
✅ Generates structured testbenches with clock, reset, test stimulus, assertions, and waveform dumping
✅ Uses Jinja2 templating for extensibility
✅ Helps verification engineers and hardware designers streamline their workflows

Installation

Ensure you have Python installed. Then, clone this repository and install dependencies:

git clone https://github.com/krishpatel1077/rtl-testbench-gen.git
cd rtl-testbench-gen
pip install jinja2

Usage

Run the script interactively:

python generate_tb.py

Example Run

$ python generate_tb.py
Enter module name: simple_alu
Enter module type (alu, fsm, memory, uart, generic): alu
Enter number of ports: 3
Port 1 direction (reg/wire): reg
Port 1 type (logic/int/...): logic
Port 1 name: a
Port 2 direction (reg/wire): reg
Port 2 type (logic/int/...): logic
Port 2 name: b
Port 3 direction (reg/wire): wire
Port 3 type (logic/int/...): logic
Port 3 name: sum

✅ Generated testbench: simple_alu_tb.sv

Supported Module Types

This tool provides different testbench structures depending on the selected module type:

Module Type

Description

alu

Arithmetic Logic Unit (ALU) testbench with basic operations (ADD, AND, XOR)

fsm

Finite State Machine (FSM) testbench with state transitions

memory

RAM/Cache testbench with read/write operations

uart

UART (Serial Communication) testbench with TX/RX verification

generic

A fallback template for any custom module

Generated Testbench Structure

Each testbench includes:
✅ Clock and Reset Generation
✅ DUT (Design Under Test) Instantiation
✅ Simulation Time Control ($finish)
✅ Waveform Dumping ($dumpfile, $dumpvars) for GTKWave
✅ Parameterized Stimulus Based on Module Type

Example Generated Testbenches

ALU Testbench (simple_alu_tb.sv)

`timescale 1ns/1ps

module simple_alu_tb;
    // Signals
    reg clk, rst;
    reg logic a, b;
    wire logic sum;

    // DUT Instantiation
    simple_alu uut (
        .a(a),
        .b(b),
        .sum(sum)
    );

    // Clock Generation
    always #5 clk = ~clk;

    // Test Sequence
    initial begin
        $dumpfile("simple_alu.vcd");
        $dumpvars(0, simple_alu_tb);

        clk = 0; rst = 1;
        a = 0; b = 0;

        #10 rst = 0;

        // Arithmetic Test Cases
        #10 a = 1; b = 1;
        #20 a = 0; b = 1;
        #30 a = 1; b = 0;

        #100 $finish;
    end
endmodule

Project Structure

rtl-testbench-gen/
│── generate_tb.py          # Main Python script
│── templates/              # Directory for Jinja2 testbench templates
│   ├── alu_template.txt    # ALU testbench template
│   ├── fsm_template.txt    # FSM testbench template
│   ├── memory_template.txt # Memory testbench template
│   ├── uart_template.txt   # UART testbench template
│   ├── generic_template.txt # Generic testbench template
│── README.md               # Project documentation


License

This project is open-source under the MIT License.Feel free to modify and contribute!

Author

Krish Patel🔗 GitHub: krishpatel1077🔗 LinkedIn: krishpatel9999

