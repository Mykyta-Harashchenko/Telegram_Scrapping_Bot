Telegram Scraping Bot
Telegram Scraping Bot is a Python-based bot built using the Aiogram library to interact with Telegram's API. The bot allows users to scrape information from Telegram channels, such as product prices, weather forecasts, and currency rates. Additionally, it offers various interactive features, like responding to user requests for information and handling multiple states to search and display data.

This bot leverages MongoDB for storing user data and integrates Google Translate for language translation. It is designed to perform automated scraping of various sources and respond with useful, dynamic content.

This bot is primarily built for scraping various types of information from external sources and providing it to users through Telegram messages. Key features include scraping product information from Hotline (a popular Ukrainian product search site), weather forecasts, and currency exchange rates.

The bot interacts with users using a custom-built keyboard interface, and it also performs various asynchronous tasks like fetching and sending information based on user commands.

Features
Hotline Product Search:
Users can search for products on Hotline by entering the product name. The bot scrapes product details like the price and image, then displays them with comparison buttons.

Currency Rate:
Users can check current currency exchange rates, including the buying and selling rates for different currencies.

Weather Information:
The bot fetches weather data for any city and translates the results into Ukrainian using Google Translate.

Bot Information:
The bot provides information about itself when requested by the user. This includes details about the bot’s functionality, technology stack, and a link for feedback.

Interactive Interface:
The bot uses Aiogram's FSM (Finite State Machine) to handle various states like searching products, entering weather cities, and more.

User Data Management:
The bot saves user data, including their Telegram ID, first and last name, and language code, to MongoDB.

Admin Features:
The bot can send test messages to users in the database, helping administrators verify bot functionality or send updates.

Tech Stack
Python 3.x: The programming language used for the bot's development.
Aiogram: Python library for building Telegram bots that use the asyncio framework.
MongoDB: NoSQL database used for storing user data.
Google Translate: For translating weather data from English to Ukrainian.
Telegram API: For interacting with Telegram and sending messages.

Getting Started
Follow these steps to set up the Telegram Scraping Bot on your local machine.
Prerequisites
Python 3.8+: Ensure you have Python 3.8 or later installed. Download Python
MongoDB: The bot uses MongoDB to store user data. You can run MongoDB locally or use a cloud-based MongoDB service like MongoDB Atlas.
Telegram Account: Create a Telegram bot using the BotFather and get your API token.
Google Cloud Translate API (optional): If you want to use Google Translate for language translation, you’ll need to set up the Google Translate API and get your API key.

Installation
Clone the repository:
git clone https://github.com/Mykyta-Harashchenko/Telegram_Scrapping_Bot.git

Navigate to the bot directory:
cd Telegram_Scrapping_Bot/gerkules

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install required dependencies:
pip install -r requirements.txt

Configure the bot:
Set up your Telegram Bot Token in the config/config.py file.
Set up your MongoDB URI and other configuration settings in the same file.
(Optional) If you're using the Google Translate API, ensure your credentials are correctly configured.

Run the bot:
python main.py
The bot should now be running and available on your Telegram account.

Bot Commands and Features
/start:
Initializes the bot and sends a welcome message with the main menu (buttons for currency, weather, and Hotline product search).

Пошук товарів Hotline:
Starts the product search flow, allowing the user to enter a product name and receive product results from Hotline.

Про бота:
Provides information about the bot, including the technology stack and a feedback link.

Погода:
Prompts the user to enter a city and retrieves weather information for that city.

Курс Валют:
Fetches and displays the current currency exchange rates.

Other Commands:
The bot can also handle miscellaneous queries and will echo user messages with a copy when an unrecognized command is entered.

Contact
For any questions or issues, feel free to contact the project maintainers:

GitHub: https://github.com/Mykyta-Harashchenko
Thank you for exploring the Telegram Scraping Bot! We hope it helps you gather valuable information from Telegram channels and sources. Happy coding! 🚀
