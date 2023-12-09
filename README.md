# Marzban V2Ray Panel User Management CLI

A command-line interface (CLI) for easily managing user creation on the Marzban V2Ray panel.

## Overview

The Marzban V2Ray Panel User Management CLI is designed to simplify the user management process, enabling users to create multiple accounts with just a click. This is especially beneficial for those who need to manage a large number of users without the hassle of creating them individually.

### Key Features

- **Bulk User Creation:**
  The project streamlines the user creation process, allowing users to generate multiple accounts simultaneously. This is particularly useful for scenarios where creating users one by one is impractical.

- **Effortless User Deletion:**
  Users can easily delete multiple accounts at once, providing a convenient solution for user management tasks.

- **Subscription Link Retrieval:**
  The CLI facilitates the retrieval of subscription links for all users, making it easy to manage and distribute these links as needed.

### Wholesale User Management

The project is tailored to accommodate wholesale user management needs. Whether you need to create, delete, or retrieve subscription links for a large number of users, this CLI offers a quick and efficient solution. Simplify your user management tasks and enhance your wholesale user operations with this powerful tool.


## Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/VQIVS/Marzban-V2Ray-Panel-User-Management-CLI.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd Seller_Admin
    ```

## Usage

Follow these steps to use the Marzban V2Ray Panel User Management CLI:

1. **Create a Virtual Environment:**
   - For Windows:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - For macOS or Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. **Install the Required Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Edit the `config.json` File:**
   Replace the placeholder values in `config.json` with your actual Marzban V2Ray panel details:

   ```json
   {
     "base_url": "https://your_actual_panel_domain/api/",
     "username": "your_actual_panel_username",
     "password": "your_actual_panel_password"
   }

## Commands
1. create users form start number to end number:
    ```
    python cli.py create
    ````
2. delete users from start number to end number:
    ```
    python cli.py delete 
    ```
3. get and save users subscription links in a text file:
    ``` 
    python cli.py sublink
    ```
    
## License
In this version, I added a License section at the end and made a few other adjustments for clarity and completeness. Remember to include your actual license file (e.g., LICENSE) in the project repository.
