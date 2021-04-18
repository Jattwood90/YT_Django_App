
<!-- ABOUT THE PROJECT -->

![webapp](https://user-images.githubusercontent.com/56833060/108557921-25b16680-72f1-11eb-9ef2-324aae8b9da4.gif)

App made using the Django framework, Bootstrap, PostgresSQL, and the YouTube API. The idea of the project is for my app to hold a list of YouTube videos, which have had copyright strikes made against them. 

The app allows the user to login, create a list of videos, and add videos to that list. There is a CRUD based system that makes it easy for users to interact with the UI and manipulate the data. It is also possible to import csv/excel data as well as export it from the database.

The Django app makes use of Class based forms, and CRUD actions for the videos.

Environment variables are hidden using dotenv, and the whole project in production mode is managed from a virtual environment.


### Built With

* [Django]()


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Jattwood90/YT_Django_App.git
   ```
2. Create virtual environment
   ```sh
   python3 -m venv djangoenv
   ```
3. Activate environment
   ```sh
   source djangoenv/bin/activate (windows users djangoenv\Scripts\activate.bat)
   ```
4. Install pip dependencies
   ```sh
   cd pip install -r requirements.txt
   ```
5. Activate localhost server (ensure your current directory is correct)
   ```sh
   python manage.py runserver
   ```


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
