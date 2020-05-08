FROM python:3.6
MAINTAINER apurva
WORKDIR /calculator
ADD . /calculator
EXPOSE 4000
CMD ["python","calc.py"]
