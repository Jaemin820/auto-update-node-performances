from notion import nodes_info, nodes_performance_info, nodes_performance_content_update

from performance.get_tia import get_celestia_testnet_validator_performance
from performance.get_bera import get_bera_testnet_validator_performance
from performance.get_eth import get_eth_ssv_validator_performance
from performance.get_dydx import get_dydx_mainnet_validator_performance, \
    get_dydx_testnet_validator_performance

import logging

class Update:
    # Performance 
    # uptime = None
    # commission = None
    # voting_power = None
    # performance = None
    # ranking = None
    
    # Nodes
    nodes = {}

    # Nodes Performance functions
    performance_functions = {
        'celestia-testnet-validator': get_celestia_testnet_validator_performance,
        'bera-testnet-validator': get_bera_testnet_validator_performance,
        'eth-ssv-validator': get_eth_ssv_validator_performance,
        'dydx-mainnet-validator': get_dydx_mainnet_validator_performance,
        'dydx-testnet-validator': get_dydx_testnet_validator_performance,
    }

    notion_contents_nodes_performance = {}

    def __init__(self):
        logging.info('Initializing Update class and fetching nodes info.')
        self.get_nodes_info()
        self.get_nodes_performance()
        # self.get_notion_performance_content()
        self.update_notion_performance_content()
        

    def get_nodes_info(self):
        logging.info('Fetching nodes information.')
        try:
            info = nodes_info()
            for i in info:
                self.nodes[i['content']] = {'url': i['link']['url']}
            logging.info('Nodes information successfully fetched.')
        except Exception as e:
            logging.error(f'Error fetching nodes information: {e}')
    
    def get_nodes_performance(self):
        logging.info('Fetching nodes performance.')
        try:
            for key, value in self.nodes.items():
                if key in self.performance_functions:
                    performance_function = self.performance_functions[key]
                    self.nodes[key].update({
                        'performance': performance_function(value['url'])
                    })
            logging.info('Nodes performance successfully fetched and updated.')
        except Exception as e:
            logging.error(f'Error fetching nodes performance: {e}')
    
    # def get_notion_performance_content(self):
    #     for key, value in self.nodes.items():
    #         notion_nodes_performance_info = nodes_performance_info(key)
    #         if len(list(notion_nodes_performance_info.keys())) < 3:
    #             self.notion_contents_nodes_performance[key] = {
    #                 'performance_24h': notion_nodes_performance_info['Performance 24H']
    #             }
    #         uptime = notion_nodes_performance_info['Uptime']
    #         commission = notion_nodes_performance_info['Commission']
    #         voting_power = notion_nodes_performance_info['Voting Power']
    #         self.notion_contents_nodes_performance[key] = {
    #             'uptime': uptime,
    #             'commission': commission,
    #             'voting_power': voting_power
    #         }

    def update_notion_performance_content(self):
        logging.info('Updating Notion performance content.')
        try:
            for key, value in self.nodes.items():
                if key in list(self.performance_functions.keys()):
                    if key == "eth-ssv-validator":
                        print(value)
                        performance =  f"Performance 24H: {value['performance']['Performance']}"
                        ranking = ""
                    else:
                        performance = f"Uptime: {value['performance']['Uptime']}\nVoting Power: {value['performance']['Voting_Power']}\nCommission: {value['performance']['Commission']}"
                        ranking = value['performance']['Ranking']

                else:
                    performance = ""
                    ranking = ""
                content = {
                    'performance': performance,
                    'ranking': ranking
                }
                nodes_performance_content_update(key, content)
        except Exception as e:
            logging.error(f'Error updating Notion performance content: {e}')


