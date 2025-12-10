# ===== Stage 1: Builder =====
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# ===== Stage 2: Runner =====
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY app/ src/
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["python", "src/app.py"]