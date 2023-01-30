pip uninstall zdppy_elasticsearch -y
rm dist/zdppy_elasticsearch-0.1.0.tar.gz
poetry build
pip install dist/zdppy_elasticsearch-1.0.1-py3-none-any.whl