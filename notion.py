from dotenv import load_dotenv
from notion_client import Client
import requests
import os
import sys
import logging

load_dotenv()

notion = Client(auth=os.environ.get('NOTION_TOKEN'))
header = {
        "Authorization": "Bearer " + os.environ.get('NOTION_TOKEN'),
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",  # Check what is the latest version here: https://developers.notion.com/reference/changes-by-version
    }

def get_child_page_info():
    logging.info('Getting child page information')
    try:
        persent_database_id = notion.databases.query(database_id=os.environ.get('DATABASE_ID'))['results'][0]['id']
        res = requests.get(
            f"https://api.notion.com/v1/blocks/{persent_database_id}/children", 
            headers=header)
        child_page_info = res.json()['results']
        logging.info('Child page information successfully geted.')
        return child_page_info
    except Exception as e:
        logging.error(f'Error getting child page information: {e}')
        sys.exit(1)


def nodes_info():
    logging.info('Getting nodes information')
    try:
        my_dict = []
        database_id = get_child_page_info()[2]['id']
        page_content = notion.databases.query(database_id=database_id)

        for i in page_content['results']:
            my_dict.append(i['properties']['Node']['title'][0]['text'])
        logging.info('Nodes information successfully geted.')
        return my_dict
    except Exception as e:
        logging.error(f'Error getting nodes information: {e}')
        sys.exit(1)

def nodes_performance_info(node_name):
    logging.info('Getting nodes performance information')
    try:
        database_id = get_child_page_info()[2]['id']
        page_content = notion.databases.query(
            database_id=database_id,
            filter={
                "property": "Node",
                "title": {
                    "equals": node_name
                }
            }
        )
        my_list = page_content['results'][0]['properties']['Performance']['rich_text'][0]['text']['content'].split('\n')
        data_dict = {item.split(": ")[0]: item.split(": ")[1] for item in my_list}
        logging.info('Nodes performance information successfully geted.')
        return data_dict
    except IndexError:
        data_dict = {"Uptime": "", "Commission": "", "Voting Power": ""}
        return data_dict
    except Exception as e:
        logging.error(f'Error getting nodes performance information: {e}')
        sys.exit(1)

def nodes_performance_content_update(node_name, content):
    logging.info('Updating nodes performance notion content')
    try:
        database_id = get_child_page_info()[2]['id']
        page_content = notion.databases.query(
            database_id=database_id,
            filter={
                "property": "Node",
                "title": {
                    "equals": node_name
                }
            }
        )
        pages = page_content.get("results", [])
        if pages:
            for page in pages:
                page_id = page["id"]
                update_response = notion.pages.update(
                    page_id=page_id,
                    properties={
                        "Performance": {
                            "rich_text": [
                                {"text": {"content": content['performance']}}
                            ]
                        },
                        "순위": {
                            "rich_text": [
                                {"text": {"content": content['ranking']}}
                            ]
                        }
                    }
                )
                logging.info('Nodes performance notion content successfully updateed.')
                logging.info(f"Updated page ID {page_id}: {update_response['properties']['Node']['title'][0]['text']['content']}")
        else:
            print("No pages found with the specified condition.")
    except Exception as e:
        logging.error(f'Error updating nodes performance notion content: {e}')
        sys.exit(1)

    