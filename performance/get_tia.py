from utils import get_drive_values
import logging

def get_celestia_testnet_validator_performance(url):
    logging.info('Getting celestia testnet validator performance information')
    try:
        performance_value_list = get_drive_values(url, 5, "ValidatorInfo_rank__d1s55", "ValidatorInfo_infoCard__1dw-p")
        ranking = performance_value_list['ValidatorInfo_rank__d1s55'][0]
        value_list = performance_value_list['ValidatorInfo_infoCard__1dw-p'][0]
        lines = value_list.split('\n')

        # 결과를 저장할 딕셔너리
        info = {}

        # 줄바꿈으로 분리된 각 줄을 순회하며 정보 추출
        for i, line in enumerate(lines):
            if "Commission" in line:
                commission = lines[i+1].strip() + lines[i+2].strip() + "%"
                info['Commission'] = commission
            elif "Uptime" in line:
                uptime = lines[i+1].strip()
                info['Uptime'] = uptime
            elif "Voting Power" in line:
                voting_power = lines[i+1].strip() + lines[i+2].strip() + "%"
                info['Voting Power'] = voting_power

        tia_performance_info = {
            'Commission': info['Commission'],
            'Uptime': info['Uptime'],
            'Voting_Power': info['Voting Power'],
            'Ranking': ranking
        }
        logging.info('Celestia testnet validator performance information successfully geted.')
        return dict(tia_performance_info)
    except Exception as e:
        logging.error(f'Error getting celestia testnet validator performance information: {e}')

    
