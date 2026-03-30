
# main.py
# --------
# Entry point for the country data visualization project.
# Launches the Tkinter GUI for visualizing country data using Matplotlib.

if __name__ == "__main__":
    # Import the main Tkinter application class
    from src.tk_app import CountryDataApp
    # Create and run the GUI application
    app = CountryDataApp()
    app.mainloop()
