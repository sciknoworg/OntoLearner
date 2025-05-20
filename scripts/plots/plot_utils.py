import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def setup_plotting():
    """Set up common plotting styles and settings"""
    # Use a clean white background style
    plt.style.use('default')
    # Set figure face color to white
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    # Use a modern grid style
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.alpha'] = 0.3
    # Set color palette
    sns.set_palette("viridis")


def load_data(file_path=None):
    """Load the metrics data from Excel file"""
    if file_path is None:
        file_path = Path("../../data/metrics/metrics.xlsx")

    df = pd.read_excel(file_path)
    return df


def ensure_output_dir(output_dir=None):
    """Ensure the output directory exists"""
    if output_dir is None:
        output_dir = Path("figures")
    elif isinstance(output_dir, str):
        output_dir = Path(output_dir)

    output_dir.mkdir(exist_ok=True)
    return output_dir
