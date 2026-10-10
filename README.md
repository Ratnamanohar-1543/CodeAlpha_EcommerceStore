# CodeAlpha_EcommerceStore (Task 1)
pip install -r requirements.txt
python manage.py makemigrations store
python manage.py migrate
python manage.py seed          # 50 products with unique photos
python manage.py createsuperuser
python manage.py runserver
