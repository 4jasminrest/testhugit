import  logging
import os.path
from logging.handlers import RotatingFileHandler

#第一步，设置logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#获取当前日志工具所在的路径
base_path = os.path.dirname(os.path.abspath(__file__))

#日志的路径
log_dir_path = os.sep.join([base_path,f'log'])

if os.path.isdir(log_dir_path) is None:
    os.mkdir(log_dir_path)

# 第二步：创建Handler并设置
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 第三步：创建Formatter
#file_log_handler = RotatingFileHandler(os.sep.join[log_dir_path,'log/log'],maxBytes=102400)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 第四步：将Formatter添加到Handler
ch.setFormatter(formatter)

date_str = '%Y-%M-%D %H:%M:%S'
# 第五步：将Handler添加到Logger
logger.addHandler(ch)

# 通过logger对象来记录日志信息

logger.debug('debug message')

logger.info('info message')

logger.warning('warn message')

logger.error('error message')

logger.critical('critical message')