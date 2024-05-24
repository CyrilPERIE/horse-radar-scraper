FROM python:3.9

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Installer Playwright et les navigateurs
# RUN python -m playwright install

COPY . .

CMD ["python", "-m", "app.scheduler"]
