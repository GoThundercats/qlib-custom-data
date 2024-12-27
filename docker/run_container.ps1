docker run -it `
    -v C:/Users/murra/qlib-data/csv_data:/root/.qlib/csv_data/my_data `
    -v C:/Users/murra/qlib-data/qlib_data:/root/.qlib/qlib_data/my_data `
    -v C:/Users/murra/qlib-custom-data/scripts:/root/scripts `
    microsoft/qlib


./docker/run_container.ps1


# First build the image
docker build -t qlib-custom -f docker/Dockerfile .

# Then run with volumes
docker run -it `
    -v C:/Users/murra/qlib-data/csv_data:/root/.qlib/csv_data/my_data `
    -v C:/Users/murra/qlib-data/qlib_data:/root/.qlib/qlib_data/my_data `
    -v C:/Users/murra/qlib-custom-data/scripts:/root/scripts `
    qlib-custom