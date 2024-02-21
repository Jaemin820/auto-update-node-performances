from utils import get_drive_values
import logging
import sys

def get_eth_ssv_validator_performance(url):
    logging.info('Getting eth ssv validator performance information')
    try:
        eth_ssv_validater_performance_info = {
            "Performance": get_drive_values(url, 5, "col-md-8")[8].split(' ')[0]
        }
        logging.info('Eth ssv validator performance information successfully geted.')
        return eth_ssv_validater_performance_info
    except Exception as e:
        logging.error(f'Error getting eth ssv validator performance information: {e}')