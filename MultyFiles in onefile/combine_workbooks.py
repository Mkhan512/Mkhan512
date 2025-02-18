import pandas as pd
import os
from pathlib import Path

def combine_excel_workbooks(input_folder, output_file):
    combined_data = {}
    excel_files = [f for f in os.listdir(input_folder) if f.endswith(('.xlsx', '.xls'))]
    
    if not excel_files:
        print(f"No Excel files found in {input_folder}")
        return
    
    # Create Excel writer with nan_inf_to_errors option
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter', 
                           engine_kwargs={'options': {'nan_inf_to_errors': True}})
    
    # Process each sheet separately
    for file in excel_files:
        file_path = os.path.join(input_folder, file)
        print(f"Processing {file}...")
        excel = pd.ExcelFile(file_path)
        
        for sheet in excel.sheet_names:
            try:
                # Read the sheet
                df = pd.read_excel(excel, sheet_name=sheet)
                
                # Initialize combined data for this sheet if not exists
                if sheet not in combined_data:
                    combined_data[sheet] = df.copy()
                else:
                    # Ensure columns match by taking union of columns
                    all_columns = list(set(combined_data[sheet].columns) | set(df.columns))
                    
                    # Fill missing columns with NaN
                    for col in all_columns:
                        if col not in combined_data[sheet].columns:
                            combined_data[sheet][col] = pd.NA
                        if col not in df.columns:
                            df[col] = pd.NA
                    
                    # Reorder columns to match
                    df = df[combined_data[sheet].columns]
                    
                    # Concatenate
                    combined_data[sheet] = pd.concat([combined_data[sheet], df], 
                                                   ignore_index=True)
                
                # Format numeric columns
                numeric_cols = combined_data[sheet].select_dtypes(include=['float64', 'float32']).columns
                for col in numeric_cols:
                    combined_data[sheet][col] = combined_data[sheet][col].fillna(0).astype(int)
                
            except Exception as e:
                print(f"Error processing sheet {sheet} in {file}: {str(e)}")
    
    # Write to Excel with formatting
    for sheet_name, data in combined_data.items():
        # Write data
        data.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Get worksheet
        worksheet = writer.sheets[sheet_name]
        
        # Add formats
        header_format = writer.book.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
            'bg_color': '#D3D3D3',
            'border': 1
        })
        
        data_format = writer.book.add_format({
            'align': 'center',
            'border': 1
        })
        
        # Format headers and data
        for col_num, col_name in enumerate(data.columns):
            worksheet.write(0, col_num, col_name, header_format)
            worksheet.set_column(col_num, col_num, len(str(col_name)) + 5)
            
            # Format data cells
            for row_num in range(len(data)):
                value = data.iloc[row_num, col_num]
                if pd.isna(value):
                    value = ""
                worksheet.write(row_num + 1, col_num, value, data_format)
    
    writer.close()
    print(f"\nCombined workbook has been saved to {output_file}")

if __name__ == "__main__":
    os.makedirs("workbooks", exist_ok=True)
    input_folder = "workbooks"
    output_file = "combined_workbook.xlsx"
    combine_excel_workbooks(input_folder, output_file) 