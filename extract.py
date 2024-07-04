from faker import Faker
import random
import pandas as pd
from google.cloud import storage
import os

# Initialize Faker
fake = Faker()

# Function to generate dummy streaming service data
def clean_data(s):
    return s.replace("\n", "_").replace('"', '')

# Function to generate dummy streaming service data
def generate_streaming_data(num_records):
    data = []

    for _ in range(num_records):
        user_id = fake.uuid4()
        username = clean_data(fake.user_name())
        email = clean_data(fake.email())
        password = clean_data(fake.password())
        full_name = clean_data(fake.name())
        address = clean_data(fake.address())
        age = random.randint(18, 70)
        subscription_plan = clean_data(random.choice(['Basic', 'Standard', 'Premium']))
        watch_time_minutes = random.randint(0, 500)
        movie_title = clean_data(fake.sentence(nb_words=3))
        genre = clean_data(random.choice(['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Documentary']))
        watched_on = fake.date_time_this_year()

        data.append({
            'User_ID': user_id,
            'Username': username,
            'Email': email,
            'Password': password,
            'Full_Name': full_name,
            'Address': address,
            'Age': age,
            'Subscription_Plan': subscription_plan,
            'Watch_Time_minutes': watch_time_minutes,
            'Movie_Title': movie_title,
            'Genre': genre,
            'Watched_On': watched_on,
        })

    return data


# Function to upload file to GCS
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the GCS bucket."""
    # Initialize a client
    storage_client = storage.Client()
    
    # Get the bucket
    bucket = storage_client.bucket(bucket_name)
    
    # Create a blob object
    blob = bucket.blob(destination_blob_name)
    
    # Upload the file
    blob.upload_from_filename(source_file_name)
    
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Generate data
os.environ["GCLOUD_PROJECT"] = "etl-data-pipeline-427816"
num_records = 1000  # Adjust the number of records as needed
streaming_data = generate_streaming_data(num_records)

# Convert to DataFrame
df = pd.DataFrame(streaming_data)

# Save to CSV
csv_filename = 'dummy_streaming_data.csv'
df.to_csv(csv_filename, index=False)

print(f"Dummy streaming service data generated and saved to '{csv_filename}'")

# Specify your bucket name and destination file name
bucket_name = 'bkt-streaming-data'
destination_blob_name = 'streaming-data/dummy_streaming_data.csv'

# Upload the CSV file to GCS
upload_to_gcs(bucket_name, csv_filename, destination_blob_name)
