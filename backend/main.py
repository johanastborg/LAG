from app.main import create_app

# Entry point for Google Cloud Functions / Firebase Functions
# The function name must match the 'function' key in firebase.json rewrites or the deployed function name.
api = create_app()
