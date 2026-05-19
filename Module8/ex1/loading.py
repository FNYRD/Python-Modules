#!/usr/bin/env python3
import importlib
import importlib.metadata
try:
    import pandas as pd
    import requests
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError as e:
    print(f"An error happened importing the modules\n{e}")


def comparison() -> list[str | None]:
    print("Checking dependencies:")
    modules: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }
    non_installed: list[str | None] = []
    for module, description in modules.items():
        try:
            version: str = importlib.metadata.version(module)
            print(f"[OK] {module} ({version}) - {description}")
        except importlib.metadata.PackageNotFoundError:
            print(f"[KO] {module} - Aren't "
                  "installed, the program cannot work")
            non_installed.append(module)
    return non_installed


def main() -> None:
    try:
        print("LOADING STATUS: Loading programs...\n")
        non_installed: list[str | None] = comparison()
        if non_installed:
            for module in non_installed:
                print(f"{module} non installed")
            print("\nFor a correct installation run one of these:\n")
            print("pip3 install package_name")
            print("  - Installs globally or in active venv")
            print("  - Does not manage dependencies automatically\n")
            print("poetry add package_name")
            print("  - Installs and adds to pyproject.toml")
            print("  - Manages dependencies and virtual "
                  "environment automatically")
            return
        url: str = "https://api.binance.com/api/v3/klines"
        params: dict[str, str | int] = {
            "symbol": "BTCUSDC",
            "interval": "1d",
            "limit": 365
        }
        response: requests.Response = requests.get(url, params)
        data: list = response.json()
        raw_data_frame: pd.DataFrame = pd.DataFrame(data, columns=[
            'timestamp', 'open', 'high', 'low', 'close',
            'volume', 'close_time', 'quote_volume', 'trades',
            'taker_buy_base', 'taker_buy_quote', 'ignore'
        ])
        raw_data_frame['close'] = raw_data_frame['close'].astype(float)
        clean_data_frame: pd.DataFrame = raw_data_frame[['timestamp', 'close']]
        clean_data_frame['timestamp'] = pd.to_datetime(
            clean_data_frame['timestamp'], unit='ms')
        print("\nAnalyzing Matrix data...")
        print(f"Processing {len(clean_data_frame['close'])} data points...")
        print(f"The avg price is {np.mean(clean_data_frame['close']):.2f}")
        print(f"The volatility is {np.std(clean_data_frame['close']):.2f}")
        print(f"The max price is {np.max(clean_data_frame['close']):.2f} "
              f"and the min is {np.min(clean_data_frame['close']):.2f}\n")
        print("Generating visualization...")
        plt.plot(clean_data_frame['timestamp'], clean_data_frame['close'])
        plt.title('BTCUSDC')
        plt.xlabel('time')
        plt.ylabel('price')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('matrix_analysis.png')
        plt.close()
        print("\nAnalysis complete!\n")
        print("Results saved to: matrix_analysis.png")
    except requests.exceptions.ConnectionError as e:
        print(f"Error calling the API: {e}")
    except AttributeError as e:
        print(f"Error calling an atribute from a library: {e}")
    except ModuleNotFoundError as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
