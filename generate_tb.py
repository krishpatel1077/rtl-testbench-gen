import jinja2
import os

# Directory where template files are stored
TEMPLATE_DIR = "templates"

# Mapping module types to template filenames
TEMPLATE_MAP = {
    "alu": "alu_template.txt",
    "fsm": "fsm_template.txt",
    "memory": "memory_template.txt",
    "uart": "uart_template.txt",
    "generic": "generic_template.txt"  # Fallback if no match
}

def get_template(module_type):
    """Retrieve the correct template based on module type."""
    filename = TEMPLATE_MAP.get(module_type, "generic_template.txt")
    template_path = os.path.join(TEMPLATE_DIR, filename)

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file '{template_path}' not found!")

    with open(template_path, "r") as file:
        return file.read()

def generate_testbench(module_name, module_type, ports):
    """Generate a SystemVerilog testbench using Jinja2 templates."""
    try:
        template_content = get_template(module_type)
        template = jinja2.Template(template_content)
        testbench = template.render(module_name=module_name, ports=ports)

        # Write to file
        output_filename = f"{module_name}_tb.sv"
        with open(output_filename, "w") as f:
            f.write(testbench)

        print(f"✅ Generated testbench: {output_filename}")

    except Exception as e:
        print(f"❌ Error generating testbench: {e}")

if __name__ == "__main__":
    # User input for module details
    module_name = input("Enter module name: ").strip()
    module_type = input("Enter module type (alu, fsm, memory, uart, generic): ").strip().lower()

    # Define module ports (hardcoded for simplicity, could be extended to user input)
    port_count = int(input("Enter number of ports: "))
    ports = []

    for i in range(port_count):
        direction = input(f"Port {i+1} direction (reg/wire): ").strip().lower()
        port_type = input(f"Port {i+1} type (logic/int/...): ").strip()
        name = input(f"Port {i+1} name: ").strip()
        ports.append({"direction": direction, "type": port_type, "name": name})

    # Generate testbench
    generate_testbench(module_name, module_type, ports)