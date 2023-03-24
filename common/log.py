# import logging
# import logging.handlers
# import os
#
#
# # 日志封装
# class Logger(object):
#
#     def __init__(self, log_name='log.txt', project_name='API', log_path='', log_level='DEBUG'):
#         """
#         :param log_name:        日志文件名称
#         :param project_name:    项目名称
#         :param log_path:        日志输出的路径,非必传
#         :param log_level:       日志级别
#         """
#
#         self.logger = logging.getLogger(project_name)  # 指定输出日志的程序名
#         self.logger.setLevel(logging.DEBUG)  # 设定全局的日志级别
#         logging_level = eval("logging." + log_level)
#         fh = ''  # 初始化fh
#         fh_err = ''  # 初始化错误日志fh_err
#         if log_path:
#             log_path_name = os.path.join(log_path, log_name)
#             # 对文件日志进行分割,已天为单位
#             fh = logging.handlers.TimedRotatingFileHandler(log_path_name, when='D', interval=1, backupCount=10)
#             fh.suffix = "%Y-%m-%d"
#             fh.setLevel(logging_level)  # 输入的日志级别
#             # # create formatter
#             formatterFh = logging.Formatter('%(asctime)s - %(name)s - '
#                                             '%(levelname)s - '
#                                             '%(filename)s - %(funcName)s - %(lineno)d - %(message)s')
#             # 错误日志输出到文件
#             log_path_name_err = os.path.join(log_path, log_name.split('.')[0] + '.txt')
#             fh_err = logging.handlers.TimedRotatingFileHandler(log_path_name_err, when='D', interval=1, backupCount=10)
#             fh_err.suffix = "%Y-%m-%d"
#             fh_err.setLevel('ERROR')  # 输入的日志级别
#             # 定义handler的输出格式
#             fh.setFormatter(formatterFh)
#             fh_err.setFormatter(formatterFh)
#
#         # 向屏幕上打印
#         ch = logging.StreamHandler()
#         ch.setLevel(logging_level)
#         formatterCh = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')
#
#         # 定义handler的输出格式
#         ch.setFormatter(formatterCh)
#
#         # 给logger添加handler
#         if not self.logger.handlers:
#             self.logger.addHandler(ch)
#             if fh:
#                 self.logger.addHandler(fh)
#             if fh_err:
#                 self.logger.addHandler(fh_err)
#
#     def get_logger(self):
#         return self.logger
#
#
# if __name__ == '__main__':
#     # 先实例化
#     logger = Logger('log_test.log', 'test').get_logger()
#     for i in range(10):
#         logger.error('打印日志')
#