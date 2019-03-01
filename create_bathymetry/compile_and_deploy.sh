
pyuic5 create_bathymetry_dialog_base.ui -o create_bathymetry_dialog.py
pyrcc5 -o resources.py resources.qrc
cp -r ../create_bathymetry/ ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
