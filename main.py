from update import Update
import sys
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(filename)s - Line: %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[
                        logging.FileHandler("update_log.log"),
                        logging.StreamHandler()
                    ])

def main():
    try:
        Update()
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main()