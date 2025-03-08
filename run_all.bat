@echo off
python load_data.py
python store_to_sql.py
python data_cleaning.py
python eda.py
python ml_model.py
python export_excel.py
echo All steps completed!
pause
