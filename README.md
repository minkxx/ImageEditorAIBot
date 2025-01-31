# ImageEditorAIBot

ImageEditorAIBot is an AI-powered image editing tool that allows users to apply various filters and effects to their images. This project leverages machine learning algorithms to enhance and transform images with ease.

## Features

- Apply various filters (e.g., sepia, grayscale, blur)
- Adjust image properties (e.g., brightness, contrast, saturation)
- Crop and resize images
- Undo and redo functionality
- User-friendly interface
- User authentication via forced subscription to a channel
- API key management for Cloudinary
- Broadcast messages to all users
- Fetch and display uploaded images

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ImageEditorAIBot.git
    cd ImageEditorAIBot
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://localhost:5000` to start using the ImageEditorAIBot.

## Setting Up the Bot Locally

### Environment Variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```
API_ID=<your_api_id>
API_HASH=<your_api_hash>
BOT_TOKEN=<your_bot_token>
MONGO_DB_URI=<your_mongo_db_uri>
LOG_GROUP=<your_log_group_id>
ADMIN_USERS_ID=<your_admin_user_ids>
FORCE_SUB_CHANNEL=<your_force_sub_channel_id>
GITHUB_USERNAME=<your_github_username>
GITHUB_REPO_NAME=<your_github_repo_name>
GITHUB_BRANCH=<your_github_branch>
```

### Running the Bot

1. Start the bot:
    ```bash
    python -m ImageBot
    ```

2. The bot should now be running. You can interact with it on Telegram.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [aryuokk@gmail.com](mailto:aryuokk@gmail.com).
