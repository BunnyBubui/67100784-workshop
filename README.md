# Machine Learning API Workshop

Learning APIs for flight prices, recommendations, depression-related classification and animal classification. Models are demonstrations, not medical tools.

## Technology

Python, FastAPI, Pydantic, scikit-learn, TensorFlow.

## Portfolio status

Classification: **supporting**. This description reflects the checked-in implementation. It does not assert production usage, ownership of every team contribution, measured performance or a passing test run.

For a resume, describe only your own contributions and include a screenshot or a reproducible demo. No customer, student, payment or credential data is required to review this code.

## Local configuration

Copy any `*.env.example` files to the corresponding local environment paths and fill in your own values. Never commit these filled files. A removed credential must also be revoked at its provider; deleting a file does not remove it from Git history.

## Review and attribution

Team work and third-party assets retain their original authorship and licensing. Check the implementation and existing package scripts for available commands. Scaffolds and deployment-only copies are not complete application showcases.

## Run this checkout

The workshop application is under `FASTAPI-LM-main/app`. Install its requirements in a virtual environment, then run `python -m uvicorn main:app --reload --port 8001` from that `app` directory. Set `ML_MODEL_DIR` to an absolute path if model artifacts are stored elsewhere. Model files and their runtime dependencies must be present before importing routes that load models.

The companion `67100784-web` interface reads `VITE_API_URL` and defaults to `http://localhost:8001`. Treat health-related classifiers as learning demonstrations; do not claim clinical validation.
