call .\venv\Scripts\activate.bat

pyinstaller --onefile --hide-console hide-early --clean -y -n "MiSpecky Controller" --add-data="icons/system_tray.png:icons" --add-data="ui/mispecky_controller.ui:ui" --icon="icons/system_tray.png" .\mispecky_gui_controller.py

call .\venv\Scripts\deactivate.bat