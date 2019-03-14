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
	zip ../create_bathymetry.zip calc_volumes.py create_bathymetry* dialog.py icon.png __init__.py metadata.txt pylintrc resources.py resources.qrc
