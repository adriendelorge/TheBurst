FROM python:3.8.12

# Expose port you want your app on
EXPOSE 8501

# Upgrade pip and install requirements
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install streamlit

# Copy app code and set working directory
COPY /pages /pages
COPY app.py app.py
COPY /TheBurst /TheBurst
COPY /image /image
WORKDIR .

# Run
# ENTRYPOINT [“streamlit”, “run”, “app.py”, “–server.port=8501”, “–server.address=0.0.0.0”]
CMD streamlit run app.py –server.port=8501 –server.address=0.0.0.0