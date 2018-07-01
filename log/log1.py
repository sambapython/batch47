import logging
logging.basicConfig(level=logging.DEBUG,
	filename="log.txt",
	format="%(asctime)s=>%(levelname)s==>%(message)s")
logging.error("Error message") # fro exceptions
logging.debug("debug message") # track the variable values
logging.info("info message")# for normal messages
logging.warn("warning message")
logging.error("Error message") # fro exceptions
logging.debug("debug message") # track the variable values
logging.info("info message")# for normal messages
logging.warn("warning message")