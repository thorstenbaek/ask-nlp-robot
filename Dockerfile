# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#
RUN python -m spacy download nb_core_news_sm

ENV PYTHONPATH /code

# 
COPY . /code/



# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
