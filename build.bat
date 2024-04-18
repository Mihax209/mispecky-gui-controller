call .\venv\Scripts\activate.bat

pyinstaller --onefile --hide-console hide-early --clean -y -n "MiSpecky Controller" --add-data="icons/system_tray.png:icons" --add-data="ui/mispecky_controller.ui:ui" .\mispecky_gui_controller.py

call .\venv\Scripts\deactivate.bat