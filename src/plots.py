from pathlib import Path

import matplotlib.pyplot as plt
from loguru import logger

# Configure Matplotlib global settings
plt.rc("font", size=14)
plt.rc("axes", labelsize=14, titlesize=14)
plt.rc("legend", fontsize=14)
plt.rc("xtick", labelsize=10)
plt.rc("ytick", labelsize=10)

# Define the path for saving figures
IMAGES_PATH = Path("..") / "reports" / "figures"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)


# Define the save_fig function
def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    """
    Save a matplotlib figure to a file.

    Parameters:
    fig_id (str): The identifier for the figure, used as the filename.
    tight_layout (bool, optional): Whether to use tight layout for the figure. Defaults to True.
    fig_extension (str, optional): The file extension for the saved figure (e.g., 'png', 'jpg'). Defaults to 'png'.
    resolution (int, optional): The resolution in dots per inch (DPI) for the saved figure. Defaults to 300.

    Raises:
    Exception: If there is an error during the saving process, an exception is raised and logged.
    """
    try:
        path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
        logger.info(f"Attempting to save figure as {path}")

        if tight_layout:
            plt.tight_layout()

        plt.savefig(path, format=fig_extension, dpi=resolution)
        logger.success(f"Figure successfully saved at {path}")
    except Exception as e:
        logger.error(f"Failed to save figure: {e}")
        raise
