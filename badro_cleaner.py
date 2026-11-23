import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import pandas as pd

root = tk.Tk()
root.title("BADRO Data Cleaner")
root.geometry("440x240")

def clean_csv():
    filename = filedialog.askopenfilename(
        title="Choose a CSV file",
        filetypes=[("CSV files", "*.csv")]
    )
    if not filename:
        return
    try:
        df = pd.read_csv(filename)
        before = len(df)
        df.columns = df.columns.str.strip()
        for col in df.select_dtypes(include=["object"]).columns:
            df[col] = df[col].str.strip()
        df = df.dropna(how="all").drop_duplicates()
        output = Path(filename).with_name(
            Path(filename).stem + "_cleaned.csv"
        )
        df.to_csv(output, index=False)
        messagebox.showinfo(
            "Success",
            f"Rows before: {before}\nRows after: {len(df)}\nSaved to:\n{output}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Label(
    root, text="BADRO Data Cleaner",
    font=("Arial", 18, "bold")
).pack(pady=25)

tk.Button(
    root, text="Choose CSV and Clean",
    command=clean_csv, font=("Arial", 12)
).pack(pady=10)

tk.Label(
    root, text="Your original file will not be overwritten."
).pack(pady=10)

root.mainloop()
