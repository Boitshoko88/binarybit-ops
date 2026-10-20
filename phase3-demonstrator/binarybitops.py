import argparse

MAX_OPERAND = 0xFFFF
BINARY_WIDTH = 16


def parse_operand(raw_value):
    """Parse a decimal, hexadecimal, or binary unsigned 16-bit value."""
    try:
        value = int(raw_value, 0)
    except ValueError as error:
        raise argparse.ArgumentTypeError(
            "enter a decimal value or use the 0b/0o/0x prefix"
        ) from error

    if value < 0 or value > MAX_OPERAND:
        raise argparse.ArgumentTypeError("value must be between 0 and 65535")
    return value


def calculate_operations(left, right):
    """Calculate the supported Binary Bit Ops demonstration operations."""
    return {"AND": left & right, "OR": left | right, "XOR": left ^ right}


def run_bitwise_demo(left, right):
    """Print the inputs and results in decimal and 16-bit binary."""
    print("Binary Bit Ops Phase 3 Demonstrator")
    print("Inputs (unsigned 16-bit integers):")
    print(f"  A = {left:5d}  {left:0{BINARY_WIDTH}b}")
    print(f"  B = {right:5d}  {right:0{BINARY_WIDTH}b}")
    print("Results:")
    for operation, result in calculate_operations(left, right).items():
        print(f"  {operation:3s} = {result:5d}  {result:0{BINARY_WIDTH}b}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Demonstrate binary AND, OR, and XOR operations."
    )
    parser.add_argument("left", nargs="?", type=parse_operand, default=12)
    parser.add_argument("right", nargs="?", type=parse_operand, default=10)
    args = parser.parse_args(argv)
    run_bitwise_demo(args.left, args.right)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
