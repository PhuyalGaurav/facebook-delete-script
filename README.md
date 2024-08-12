# Facebook Post Deletion Script

This script allows you to delete posts from a Facebook page using the Facebook Graph API.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your machine with venv.
- Facebook user access token
- Facebook page ID

## Setup

1. Clone the repository:

    ```shell
    git clone [https://github.com/your-username/facebook-delete.git](https://github.com/PhuyalGaurav/facebook-delete-script)
    ```

2. Navigate to the project directory:

    ```shell
    cd facebook-delete
    ```

3. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory and add the following environment variables:

    ```plaintext
    USER_ACCESS_TOKEN=your-user-access-token
    PAGE_ID=your-page-id
    ```

## Usage

To run the script, execute the following command:

```shell
python main.py
```

The script will fetch all the posts from the specified Facebook page and delete them one by one. If a post cannot be deleted, the script will retry after a 5-second delay.

Please note that this script will continuously run until manually stopped. To stop the script, press `Ctrl + C`.
