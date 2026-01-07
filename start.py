import os
import time
import shutil

MODE_FILE = os.path.expanduser("~/.termux_mode")

def clear():
    os.system("clear")

def center(text):
    cols = shutil.get_terminal_size().columns
    return text.center(cols)

# ===== DOWNLOAD SCREEN (แดงเรืองแสง) =====
def loading_red():
    BAR = 28
    DURATION = 3.5
    start = time.time()

    while True:
        p = min((time.time() - start) / DURATION, 1)
        fill = int(BAR * p)
        bar = "█" * fill + "░" * (BAR - fill)

        clear()
        print("\n" * 6)
        print(center("\033[1;91mDOWNLOADING SYSTEM\033[0m"))
        print()
        print(center(f"\033[91m[{bar}]\033[0m"))
        print(center(f"\033[2;91m{int(p*100)}%\033[0m"))
        print()
        print(center("\033[2;91mInitializing core modules...\033[0m"))

        if p >= 1:
            break
        time.sleep(0.05)

    time.sleep(0.5)

# ===== BANNER เดิมของมึง =====
def banner():
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    DIM = "\033[2m"

    clear()
    print(RED + BOLD)
    print("╔════════════════════════════════════════════════════╗")
    print("║                                                    ║")
    print("║         ███████╗██████╗  █████╗ ███╗   ███╗        ║")
    print("║         ██╔════╝██╔══██╗██╔══██╗████╗ ████║        ║")
    print("║         ███████╗██████╔╝███████║██╔████╔██║        ║")
    print("║         ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║        ║")
    print("║         ███████║██║     ██║  ██║██║ ╚═╝ ██║        ║")
    print("║         ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝        ║")
    print("║                                                    ║")
    print("║              W E B S I T E   M O D E               ║")
    print("║                                                    ║")
    print("╚════════════════════════════════════════════════════╝")
    print(RESET)

# ===== เลือกครั้งเดียว =====
def first_select():
    clear()
    print("\n")
    print(center("SELECT MODE"))
    print()
    print(center("[1] ENABLE WEBSITE MODE (PERMANENT)"))
    print()
    c = input(center("TYPE 1 AND PRESS ENTER : "))

    if c.strip() == "1":
        with open(MODE_FILE, "w") as f:
            f.write("website")

# ===== MAIN =====
def main():
    if not os.path.exists(MODE_FILE):
        first_select()
        return

    with open(MODE_FILE) as f:
        mode = f.read().strip()

    if mode == "website":
        loading_red()
        banner()

if __name__ == "__main__":
    main()
