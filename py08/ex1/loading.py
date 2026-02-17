import importlib


def check_dependencies() -> bool:
    """just check all dependecies are installed """
    required = ["pandas", "numpy", "matplotlib"]

    for package in required:
        value = True
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {package} ({version} - Ready)")
        except ModuleNotFoundError:
            print(f"[MISSING] {package} - Please install")
            value = False

    return value


if __name__ == "__main__":
    print("Checking dependencies:")
    if check_dependencies():
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        print("Analyzing Matrix data..")

        missions = [
            "Mission 1",
            "Mission 2",
            "Mission 3",
            "Mission 4",
            "Mission 5",
            "Mission 6",
            "Mission 7",
            "Mission 8",
            "Mission 9",
            "Mission 10",
        ]

        success_rate = [45, 52, 48, 67, 72, 68, 75, 82, 78, 85]

        data = pd.DataFrame(
            {"Mission": missions, "Success_Rate": success_rate}
        )

        print(f"Processing {len(data)} data points...")
        average = np.mean(success_rate)
        max_success = np.max(success_rate)
        min_success = np.min(success_rate)

        print("\nAnalysis Results:")
        print(f"  Best Mission: {max_success}%")
        print(f"  Worst Mission: {min_success}%")

        print("\nGenerating visualization...")
        plt.figure(figsize=(10, 6))
        plt.plot(missions, success_rate, marker="o", color="blue", linewidth=2)
        plt.title(
            "Matrix Resistance - Mission Success Rate",
            fontsize=16,
            fontweight="bold",
            color="red",
        )

        plt.xlabel("Missions", fontsize=12)
        plt.ylabel("Success Rate (%)", fontsize=12)
        plt.grid(True, alpha=0.5)
        plt.xticks(rotation=45)
        plt.tight_layout()

        output_file = "matrix_analysis.png"
        plt.savefig(output_file)
