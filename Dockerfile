FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /rest
WORKDIR /rest

RUN pip install --upgrade pip
RUN pip install ipython==7.13.0

RUN pip install Django==2.2.4
RUN pip install django-annoying==0.10.4
RUN pip install django-cors-headers==2.3.0
RUN pip install django-extensions==2.0.7
RUN pip install django-filter==2.2.0
RUN pip install django-fernet-fields==0.6

RUN pip install django-rest-passwordreset==0.9.5
RUN pip install djangorestframework==3.8.2
RUN pip install djangorestframework-filters==0.10.2
RUN pip install djangorestframework-jwt==1.11.0
RUN pip install drf-writable-nested==0.4.2
RUN pip install PyJWT==1.6.4

RUN pip install pymysql==0.9.3
RUN pip install mysqlclient==1.3.13

RUN pip install gunicorn==19.9.0

RUN pip install pandas==1.0.2
RUN pip install rest-pandas==1.1.0
RUN pip install pandas-profiling==2.9.0

RUN pip install seaborn==0.10.0