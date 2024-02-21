from utils import get_drive_values
import logging
import sys

def get_dydx_mainnet_validator_performance(url):
    logging.info('Getting dydx mainnet validator performance information')
    try:
        commssion_voting_power_uptime_list = get_drive_values(url, 10, "s-UR0RXdEDmUvA")
        commission = commssion_voting_power_uptime_list[commssion_voting_power_uptime_list.index('Commission') + 1]
        uptime = commssion_voting_power_uptime_list[commssion_voting_power_uptime_list.index('Uptime') + 1]
        voting_power = commssion_voting_power_uptime_list[commssion_voting_power_uptime_list.index('Voting Power') + 1]

        ranking_value_list = get_drive_values("https://www.mintscan.io/visualization/validators/nodeinfra", 3, "s-6DphA2GZzKLK")
        ranking = ranking_value_list[6]

        dydx_mainnet_performance_info = {
            'Commission': commission,
            'Uptime': uptime,
            'Voting_Power': voting_power,
            'Ranking': ranking
        }
        logging.info('Dydx mainnet validator performance information successfully geted.')
        return dydx_mainnet_performance_info
    except Exception as e:
        logging.error(f'Error getting dydx mainnet validator performance information: {e}')

def get_dydx_testnet_validator_performance(url):
    logging.info('Getting dydx testnet validator performance information')
    try: 
        performance_value_list = get_drive_values(url, 8, "css-1fzq8sc", "css-1jijfcn", "css-1fakasn")
        commission = performance_value_list["css-1fzq8sc"][0].split('\n')[2]
        voting_power = performance_value_list["css-1jijfcn"][0]
        uptime = performance_value_list["css-1fakasn"][0]

        dydx_testnet_performance_info = {
            'Commission': commission,
            'Uptime': uptime,
            'Voting_Power': voting_power,
            'Ranking': "" # 임의로 지정
        }
        logging.info('Dydx testnet validator performance information successfully geted.')
        return dydx_testnet_performance_info
    except Exception as e:
        logging.error(f'Error getting dydx testnet validator performance information: {e}')