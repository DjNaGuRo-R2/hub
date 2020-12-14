#!/usr/bin/env python3
""" Generating a discord release notification for a job

.. moduleauthor:: Alexandre Burgoni <alexandre@go2scale.com>

"""

import sys
import os
import random
import argparse
import logging
import requests
import yaml

ROOT_DIR = os.getenv("CI_PROJECT_DIR", "../")
QUOTES_URL = "https://gitlab.com/r2devops/hub/-/snippets/2046463/raw/master/snippetfile1.txt" # Link to snippet
AVATAR_URL = "https://go2scale.io/wp-content/uploads/2020/07/cropped-favicon_bleu-192x192.png" # Avatar of the author showed in the footer also
USERNAME = "R2" # Message's author
EMBED_COLOR = 1127128 # Trailing color at left of message
EMBED_TITLE = "A new job version is available for " # Title of the message
EMBED_DESCRIPTION = "Wanna see what's new ? :point_down:" # Content of the message (body)
DOC_LINK = "https://r2devops.io/jobs/"

def get_yaml_property(file_path, property_name):
    """Fetch a yaml property from a specified file

    Args:
        file_path (str): Path to the yaml file
        property_name (str): Property name we want
    """

    if not os.path.exists(file_path):
        logging.error("[ERROR] Could not find the following yaml property's path %s", file_path)
        sys.exit(1)

    with open(file_path, "r") as file:
        try:
            content = yaml.safe_load(file)
            return content[property_name]
        except yaml.YAMLError as expt:
            logging.error("[ERROR] Failed to parse YAML file %s", file_path)
            logging.error("[ERROR] Error content: %s", expt)
            sys.exit(1)
        except IndexError:
            logging.error("[ERROR] Property %s not found in file %s", property_name, file_path)
            sys.exit(1)

def get_random_quote():
    """Retrieve a random quote from R2Devops Snippet

    Returns:
        str: A quote from R2
    """
    with requests.get(QUOTES_URL) as response:
        data = response.json()
        return random.choice(data)

def generate_data(name: str, version: str):
    """Generate the body of the request

    Args:
        name (str): Name of the job
        version (str): Version of the job

    Returns:
        object: Describe the format and content of discord notification
    """

    logging.debug("generateData(%s, %s)", name, version)

    job_path = "{0}/jobs/{1}/job.yml".format(ROOT_DIR, name.lower())
    icon = get_yaml_property(job_path, "icon")
    stage = get_yaml_property(job_path, "default_stage")

    changelog_path = "{0}/jobs/{1}/versions/{2}.md".format(ROOT_DIR, name.lower(), version)
    logging.debug("Changelog path is %s", changelog_path)

    if not os.path.exists(changelog_path):
        logging.error("[ERROR] Could not find the following changelog %s", changelog_path)
        sys.exit(1)

    changelog = open(changelog_path, "r").read()
    data_format = {
        "username": USERNAME,
        "avatar_url": AVATAR_URL,
        "embeds": [
            {
                "title": "{} {}`{}`".format(EMBED_TITLE, icon, name),
                "color": EMBED_COLOR,
                "description": EMBED_DESCRIPTION,
                "fields": [
                        {
                            "name": "Documentation",
                            "value": "{0}{1}/{2}/".format(DOC_LINK, stage, name.lower())
                        },
                        {
                            "name": "Version",
                            "value": "*{}*".format(version)
                        },
                        {
                            "name": "Version changelog",
                            "value": changelog
                        }
                    ],
                "footer": {
                    "text": get_random_quote(),
                    "icon_url": AVATAR_URL
                }
            }
        ]
    }

    logging.debug("Dataformat content %s", data_format)
    return data_format

def send_message(web_hook: str, data_format: object):
    """Create the HTTP request to discord API

    Args:
        webHook (str): Discord webhook link
        dataFormat (object): Message body generated from generateData()
    """
    logging.debug("sendMessage(%s, %s)", web_hook, data_format)

    if not web_hook:
        logging.error("[ERROR] Cannot send discord notification as no webHook URL is defined")
        logging.error("[ERROR] Either define environment variable DISCORD_WEBHOOK_RELEASE")
        logging.error("[ERROR] or add argument --webhook")
        sys.exit(1)

    result = requests.post(web_hook, json=data_format)

    if result.status_code != 204:
        logging.error("[ERROR] A problem occured when sending discord message for this release")
        logging.error("[ERROR] Result body: %s", result.text)
        sys.exit(1)

    logging.info("Discord notification sent successfully")

def main():
    """Main function of this script
    """
    parser = argparse.ArgumentParser(description="Discord Release Notifier")

    parser.add_argument("--name", '-n',
    type=str, required=True, help="R2DevOps job's name")

    parser.add_argument("--version", "-v",
    type=str, required=True, help="R2DevOps job's version")

    parser.add_argument("--webhook", "-w",
    type=str, default=os.getenv("DISCORD_RELEASE_WEBHOOK"),
    help="Custom Discord WebHook (default: {})".format(os.getenv("DISCORD_RELEASE_WEBHOOK")))

    parser.add_argument("--debug", "-d",
    dest="loglevel", action="store_const", const=logging.DEBUG,
    default=logging.INFO, help="Logging Level")

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    data_format = generate_data(args.name, args.version)
    send_message(args.webhook, data_format)

if __name__ == "__main__":
    main()
