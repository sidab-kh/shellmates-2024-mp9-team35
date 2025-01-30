# shellmates-2024-mp9-team35

## Setup Instructions

1. **Create a Virtual Environment**  
    Run the following command to create a virtual environment:
    ```
    python -m venv venv
    ```

2. **Activate the Virtual Environment**  
    - On Windows:
      ```
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```
      source venv/bin/activate
      ```

3. **Install Dependencies**  
    Install the required packages using pip:
    ```
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**  
    Update the `.env` file with your environment variables, such as `SECRET_KEY` and database credentials.

5. **Run Migrations**  
    Apply database migrations:
    ```
    python manage.py migrate
    ```

6. **Start the Development Server**  
    Run the development server:
    ```
    python manage.py runserver
    ```

## Creating a New App

1. **Create the App**  
    Run the following command to create a new Django app:
    ```
    python manage.py startapp <app_name>
    ```

2. **Register the App**  
    Add the new app to the `INSTALLED_APPS` list in `settings.py`:
    ```python
    INSTALLED_APPS = [
         ...
         '<app_name>',
    ]
    ```

3. **Create Models**  
    Define your models in `<app_name>/models.py`.

4. **Create Views**  
    Define your views in `<app_name>/views.py`.

5. **Create URLs**  
    Add URL patterns in `<app_name>/urls.py` and include them in the project's main `urls.py`.

6. **Run Migrations for the New App**  
    Apply migrations for the new app:
    ```
    python manage.py makemigrations <app_name>
    python manage.py migrate
    ```

7. **Create Endpoints for Blog Requests**  
    Use Django REST Framework to create endpoints to handle blog requests:
    - Create serializers in `<app_name>/serializers.py`:
      ```python
      from rest_framework import serializers
      from .models import Blog

      class BlogSerializer(serializers.ModelSerializer):
          class Meta:
              model = Blog
              fields = '__all__'
      ```
    - Create views in `<app_name>/views.py`:
      ```python
      from rest_framework import viewsets
      from .models import Blog
      from .serializers import BlogSerializer

      class BlogViewSet(viewsets.ModelViewSet):
          queryset = Blog.objects.all()
          serializer_class = BlogSerializer
      ```