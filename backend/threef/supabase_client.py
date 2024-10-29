import os
from supabase import create_client
from dotenv import load_dotenv
import requests
from django.conf import settings

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET_NAME = 'threef_bucket'

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

MEDIA_URL = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET_NAME}/"

def upload_to_supabase(file, file_name):
    """
    Uploads a file to the specified Supabase bucket and returns the file's public URL.
    
    Args:
        file: The file object to be uploaded.
        file_name: The name to save the file as in Supabase.

    Returns:
        str: Public URL of the uploaded file.
    """
    url = f"{SUPABASE_URL}/storage/v1/object/{SUPABASE_BUCKET_NAME}/{file_name}"
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
    }
    
    # Upload the file to Supabase
    response = requests.post(url, headers=headers, files={"file": file})
    
    if response.status_code == 200:
        return f"{MEDIA_URL}{file_name}"  # Return the public URL of the file
    else:
        raise Exception("Failed to upload file to Supabase")
