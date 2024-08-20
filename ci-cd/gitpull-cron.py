# Python function to run git pull on a cloned repository directory on a local machine in a specifc period of time
# Run this script in a cron job to automate the git pull process
# Author: Navendran Ramadas
# Date: 2021-06-14
# Version: 1.0
# Usage: python gitpull-clone.py
import subprocess
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def git_pull(repo_dir):
    """
    Runs git pull in the specified repository directory.
    
    :param repo_dir: Path to the local git repository
    """
    if not os.path.isdir(repo_dir):
        logging.error(f"The directory {repo_dir} does not exist.")
        return
    
    try:
        # Change to the repository directory
        os.chdir(repo_dir)
        
        # Run git pull
        result = subprocess.run(['git', 'pull'], capture_output=True, text=True)
        
        if result.returncode == 0:
            logging.info(f"Successfully pulled latest changes in {repo_dir}")
        else:
            logging.error(f"Failed to pull latest changes in {repo_dir}: {result.stderr}")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    repo_directory = "/home/navendran/workshop/github/intellitest"
    git_pull(repo_directory)
    logging.info("Completed git pull process")

# Note:
# To automate this script using a cron job, you can add an entry to your crontab. 
# For example, to run the script every hour, you can add the following line to your crontab:
# 0 * * * * /usr/bin/python3 /path/to/your/gitpull-clone.py
#You can edit your crontab by running `crontab -e` in the terminal. 
# Make sure to replace [`/path/to/your/gitpull-clone.py`] with the actual path to your script.