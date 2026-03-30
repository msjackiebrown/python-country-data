
# tk_app.py
# ---------
# Tkinter GUI application for visualizing country data with Matplotlib.

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.get_country_details import get_country_details
from src.visualize_countries import create_country_plots


class CountryDataApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Country Data Visualizer")
        self.geometry("1366x768")
        # List of matplotlib Figure objects for each plot
        self.figures = []
        # Index of the currently displayed plot
        self.current_plot = 0
        # Build the UI widgets
        self._setup_ui()
        # Load country data and generate plots
        self._load_data_and_plots()
        # Show the first plot
        self._show_plot(0)
        # Handle window close event
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _on_close(self):
        # Properly close all matplotlib figures and exit the app
        import matplotlib.pyplot as plt
        plt.close('all')
        self.destroy()

    def _setup_ui(self):
        # Header label
        header = tk.Label(self, text="Country Data Visualizer", font=("Arial", 20, "bold"))
        header.pack(pady=10)

        # Button to show the data table in a popup window
        self.data_btn = tk.Button(self, text="Show Data Table", command=self._show_data_table_window)
        self.data_btn.pack(pady=(5, 0))

        # Navigation buttons for cycling through plots
        nav_frame = tk.Frame(self)
        nav_frame.pack(pady=5)
        self.prev_btn = tk.Button(nav_frame, text="Previous", command=self._prev_plot)
        self.prev_btn.grid(row=0, column=0, padx=5)
        self.next_btn = tk.Button(nav_frame, text="Next", command=self._next_plot)
        self.next_btn.grid(row=0, column=1, padx=5)

        # Frame to hold the matplotlib plot
        self.plot_frame = tk.Frame(self)
        self.plot_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    def _show_data_table_window(self):
        # Create a new top-level window for the data table
        table_win = tk.Toplevel(self)
        table_win.title("All Countries Data")
        table_win.geometry("600x500")
        label = tk.Label(table_win, text="All Countries Data", font=("Arial", 12, "bold"))
        label.pack(pady=(10,0))
        frame = tk.Frame(table_win)
        frame.pack(pady=5, fill=tk.BOTH, expand=True)
        columns = ("Country", "Area", "Population")
        # Treeview widget for tabular data
        table = ttk.Treeview(frame, columns=columns, show="headings", height=20)
        for col in columns:
            # Enable sorting by clicking column headers
            table.heading(col, text=col, command=lambda c=col: self._sort_table_column(table, c, False))
        table.column("Country", width=180)
        table.column("Area", width=120, anchor=tk.E)
        table.column("Population", width=120, anchor=tk.E)
        vsb = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=vsb.set)
        table.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        # Fill table with all countries
        for name, area, pop in zip(self.country_names, self.areas, self.populations):
            table.insert("", "end", values=(name, f"{area:,.0f}", f"{pop:,}"))
        # Make sure the window is focused and modal
        table_win.transient(self)
        table_win.grab_set()
        table_win.focus()
        # Store reference to table for sorting
        table_win._table = table

    def _sort_table_column(self, table, col, reverse):
        # Sort the table by the given column
        data = [(table.set(k, col), k) for k in table.get_children("")]
        def try_num(val):
            # Try to convert to float for numeric sorting
            try:
                return float(val.replace(",", ""))
            except Exception:
                return val
        data.sort(key=lambda t: try_num(t[0]), reverse=reverse)
        # Rearrange items in sorted positions
        for index, (val, k) in enumerate(data):
            table.move(k, '', index)
        # Reverse sort next time
        table.heading(col, command=lambda: self._sort_table_column(table, col, not reverse))

        # Footer with Save and Exit buttons
        footer = tk.Frame(self)
        footer.pack(pady=10)
        save_btn = tk.Button(footer, text="Save Plot", command=self._save_plot)
        save_btn.grid(row=0, column=0, padx=5)
        exit_btn = tk.Button(footer, text="Exit", command=self.destroy)
        exit_btn.grid(row=0, column=1, padx=5)

    def _load_data_and_plots(self):
        # Fetch and process country data from the web
        country_names, populations, areas = get_country_details()
        # Convert population and area to numeric types
        populations = [int(p.replace(",", "")) for p in populations]
        areas = [float(a.replace(",", "")) for a in areas]
        self.country_names = country_names
        self.populations = populations
        self.areas = areas
        # Generate matplotlib figures for the plots
        self.figures = create_country_plots(country_names, areas, populations)

    def _show_plot(self, idx):
        # Display the plot at the given index
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        fig = self.figures[idx]
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.current_plot = idx
        # Enable/disable navigation buttons as appropriate
        self.prev_btn.config(state=tk.NORMAL if idx > 0 else tk.DISABLED)
        self.next_btn.config(state=tk.NORMAL if idx < len(self.figures)-1 else tk.DISABLED)


    def _next_plot(self):
        # Show the next plot, if available
        if self.current_plot < len(self.figures)-1:
            self._show_plot(self.current_plot + 1)

    def _prev_plot(self):
        # Show the previous plot, if available
        if self.current_plot > 0:
            self._show_plot(self.current_plot - 1)

    def _save_plot(self):
        # Save the currently displayed plot as a PNG image
        from tkinter import filedialog
        fig = self.figures[self.current_plot]
        filetypes = [("PNG Image", "*.png"), ("All Files", "*.*")]
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=filetypes)
        if filename:
            fig.savefig(filename)


# Run the app if this file is executed directly
if __name__ == "__main__":
    app = CountryDataApp()
    app.mainloop()
