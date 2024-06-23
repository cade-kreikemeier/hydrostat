# Hydrostat

A web application for monitoring the properties of water within hydroponic systems.

## Installation

### Prerequisites

- **Docker**: Ensure you have Docker installed on your system. If not, download and install Docker from [Docker's official website](https://www.docker.com/get-started).

### Getting Started

1. **Clone the Repository**

   Open a terminal, navigate to the desired location and run the following command to clone the repository:

   ```bash
   git clone https://github.com/ckreikemeier/hydrostat.git
   ```

2. **Navigate to the Project**

   After cloning, navigate into the project directory:

   ```bash
   cd hydrostat
   ```

3. **Setup the .env files**

   Rename the `.env-copy` files to `.env`

   ```bash
   mv ./backend/.env-copy ./backend/.env && mv ./webui/.env-copy ./webui/.env
   ```

   Open each `.env` file within a text editor and change the appropriate values

### How to Start the Environment

   From the top project directory, use Docker Compose to build and start the environment. Run:

   ```bash
   docker compose up -d
   ```

   This command will download the necessary Docker images, build the containers, and start the services defined in your docker-compose.yml file in the background.
   
   You can now open http:localhost:

### How to Teardown the Environment

   To stop and remove the containers, and to remove the volumes associated with the containers, run the following command:

   ```
   docker compose down -v
   ```

   To persist data after teardown, remove the `-v` flag from the command above.
