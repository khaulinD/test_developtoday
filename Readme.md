# test_DevelopToday

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/khaulinD/test_developtoday/
    cd test_synergyway
    ```

# Using Docker
1. **Start the docker:**

    ```bash
    docker-compose up --build -d
    ``` 
2. **Set up database tables**
   ```bash
    docker-compose exec web alembic upgrade head
    ``` 
3. **Visit the application:**

   -  Open a browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to see the running application.
   - You can see JSON representation when open http://0.0.0.0:8000/openapi.json or visit https://web.postman.co/workspace/My-Workspace~26a4fbe6-7e60-45e3-853d-ad6f44044cb5/collection/29391551-81b839d7-7639-4a45-a638-667de9392d91?action=share&source=copy-link&creator=29391551 to see some small version of it

   - Adminer - for database review in browser: http://localhost:8080
