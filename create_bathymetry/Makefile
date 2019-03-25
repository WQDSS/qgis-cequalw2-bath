compile:
	pyuic5 create_bathymetry_dialog_base.ui -o create_bathymetry_dialog.py
	pyrcc5 -o resources.py resources.qrc

deploy:
	cp -r ../create_bathymetry/ ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/

clean: 
	rm -fr __pycache__ *.pyc

unittest:
	PYTHONPATH=. python test/test_calc_volumes.py

zip:
	rm -f ../create_bathymetry.zip
	cd .. && zip create_bathymetry.zip create_bathymetry/calc_volumes.py create_bathymetry/create_bathymetry* create_bathymetry/dialog.py create_bathymetry/icon.png create_bathymetry/ create_bathymetry/__init__.py create_bathymetry/metadata.txt create_bathymetry/pylintrc create_bathymetry/resources.py create_bathymetry/resources.qrc
