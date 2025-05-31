import kagglehub

# Download latest version
path = kagglehub.dataset_download("arianazmoudeh/airbnbopendata")

print("Path to dataset files:", path)