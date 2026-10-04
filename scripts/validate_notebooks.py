"""Execute repository notebooks from clean kernels and retain validated results."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parents[1]
output_dir = root / "validation-output"
output_dir.mkdir(exist_ok=True)
for name, relative in [
    ("crop", "Crop Recommender Based on Soils/crop-recommendation.ipynb"),
    ("house-rent", "Predicting House Rent Model/house-rent-prediction.ipynb"),
]:
    source = root / relative
    notebook = nbformat.read(source, as_version=4)
    nbformat.validate(notebook)
    NotebookClient(
        notebook, timeout=900, kernel_name="python3",
        resources={"metadata": {"path": str(source.parent)}},
    ).execute()
    nbformat.validate(notebook)
    target = output_dir / f"{name}-executed.ipynb"
    nbformat.write(notebook, target)
    print(f"{name}: all code cells passed; saved {target.relative_to(root)}")

