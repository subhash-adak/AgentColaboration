import sys
from main import run_a2a_loop

if __name__ == '__main__':
    print("\n🚀 A2A CLI Console Running")
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        run_a2a_loop()
    else:
        print("Usage: python cli.py run")