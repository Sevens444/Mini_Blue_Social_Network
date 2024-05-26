#!/bin/bash
flask db upgrade
read -p "Press enter to continue"
exec gunicorn -b 0.0.0.0:5000 "app:create_app()"
read -p "Press enter to continue"