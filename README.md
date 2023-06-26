# Car Collection API

The Car Collection API is a web application that allows users to manage and display a collection of cars. It provides endpoints to retrieve, add, update, and delete cars from the collection.

## Features

- Landing page with information about the API
- Two separate blueprints for different sections of the API
- Customizable HTML templates for each blueprint
- Static files (CSS, images, etc.) for styling and assets
- Flask configuration file for environment-specific settings

## File Structure

The file structure of the project is organized as follows:

```
car_inventory/
├── blueprint1/
│   ├── templates_folder/
│   │   └── index.html
│   └── routes.py
├── blueprint2/
│   ├── templates_folder/
│   │   └── index.html
│   └── routes.py
├── static/
├── templates/
│   └── index.html
├── __init__.py
└── config.py
```

- `blueprint1`: Contains the routes and templates for blueprint1 section.
- `blueprint2`: Contains the routes and templates for blueprint2 section.
- `static`: Holds static files like CSS, images, etc.
- `templates`: Contains the HTML templates for the main package.
- `__init__.py`: Initializes the Flask application and registers the blueprints.
- `config.py`: Configuration file for any environment-specific settings.

## Getting Started

To get started with the Car Collection API, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/car-collection-api.git
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```shell
   python3 -m venv car_api_venv
   source car_api_venv/bin/activate
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Configure the application (if needed) by modifying the `config.py` file.

5. Run the application:

   ```shell
   flask run
   ```

6. Open your web browser and access the API at `http://localhost:5000`.

## Customization

- Customize the HTML templates in the respective `templates_folder` directories for each blueprint to modify the look and feel of the API pages.
- Add additional routes, functionalities, and database interactions as per your project requirements.
- Modify the `styles.css` file in the `static` folder to customize the visual styles of the API pages.

## Contributions

Contributions to the Car Collection API are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).

