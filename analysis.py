import marimo

__generated_with = "0.9.14"
app = marimo.App()

@app.cell
def imports():
    import marimo as mo
    return mo,

@app.cell
def input_section(mo):
    # Email: 23f3000339@ds.study.iitm.ac.in
    
    # Cell 1: Interactive Input
    # This acts as the source of the data flow.
    slider = mo.ui.slider(start=1, end=20, step=1, label="Select Data Quantity")
    return slider,

@app.cell
def calculation_section(slider):
    # Cell 2: Variable Dependency
    # This cell depends on 'slider'. Marimo guarantees this runs 
    # automatically whenever the slider value changes.
    calculated_value = slider.value * 5
    return calculated_value,

@app.cell
def display_section(calculated_value, mo, slider):
    # Cell 3: Dynamic Markdown Output
    # This cell documents the flow and updates the visualization based on widget state.
    mo.md(
        f"""
        # Data Analysis Dashboard
        
        ### 1. Control Panel
        {slider}
        
        ### 2. Live Results
        - **Input Value:** {slider.value}
        - **Calculated Result (Input × 5):** {calculated_value}
        
        ### 3. Visual Representation
        {'🟦' * slider.value}
        """
    )
    return

if __name__ == "__main__":
    app.run()
