# sign-lang-detection

## How to run
Before you run this project make sure you have MongoDB Atlas account and you have the shipping dataset into it.

Step 1. Cloning the repository.
```
https://github.com/Deep-Learning-01/Sign-Language-Detection-from-Video
```
Step 2. Create a conda environment.
```
conda create --prefix ./venv python=3.7 -y
```
```
conda activate venv/
````
Step 3. Install the requirements 
```
pip install -r requirements.txt
```
Step 4. Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>
```


Step 5. Run the application server

```
python app.py
```

Step 6. Train application

```bash
http://localhost:8080/train
```

Step 7. Prediction application

```bash
http://localhost:8080/live
```


## Run in Docker

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image

```
docker build --build-arg AWS_ACCESS_KEY_ID="" --build-arg AWS_SECRET_ACCESS_KEY="" --build-arg AWS_DEFAULT_REGION="" -t sign . 
```

3. Run the Docker image

```
docker run -d -p 8080:8080 --ipc="host" sign