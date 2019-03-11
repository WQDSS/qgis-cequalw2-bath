compile:
	pyuic5 create_bathymetry_dialog_base.ui -o create_bathymetry_dialog.py
	pyrcc5 -o resources.py resources.qrc
	python3.6 test_calc_volumes.py

deploy:
	cp -r ../create_bathymetry/ ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/

clean: 
	rm -fr __pycache__