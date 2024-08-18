# Step 1: Use Python base image
FROM python:3.9

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy requirements.txt to the working directory
COPY requirements.txt ./

# Step 4: Install Python dependencies
RUN pip install -r requirements.txt

# Step 5: Copy the rest of the application code
COPY . .

# Step 6: Expose the port Flask will run on
EXPOSE 5001

# Step 8: Run the Flask app
CMD ["python3", "app.py"]