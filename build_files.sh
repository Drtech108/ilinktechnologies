echo "BUILD START"
Python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo "BUILD END"