FROM python:3.12-rc-alpine
RUN mkdir /cooktoday
COPY . /cooktoday
WORKDIR /cooktoday
RUN pip install -r requirements.txt
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]