from utils import get_drive_values
import logging

def get_bera_testnet_validator_performance(url):
    logging.info('Getting bera testnet validator performance information')
    try:
        commission_voting_power_value_list = get_drive_values(url + "staking", 10, "table-responsive-sm")[1]
        commission_voting_power_lines = commission_voting_power_value_list.split('\n')
        nodeinfra_index = commission_voting_power_lines.index('nodeinfra')

        voting_power = commission_voting_power_lines[nodeinfra_index+1].split(' ')[0] + 'ABGT'
        commission = commission_voting_power_lines[nodeinfra_index+2].split(' ')[1]
        ranking_value_list = get_drive_values(url + "uptime", 10, "row")[3].replace(' ', '')
        ranking_lines = ranking_value_list.split('\n')

        for line in ranking_lines:
            if "nodeinfra" in line:
                ranking = line[0]

        bera_performance_info = {
            'Commission': commission,
            'Uptime': "",
            'Voting_Power': voting_power,
            'Ranking': ranking
        }
        logging.info('Bera testnet validator performance information successfully geted.')
        return bera_performance_info
    except Exception as e:
        logging.error(f'Error getting bera testnet validator performance information: {e}')    
