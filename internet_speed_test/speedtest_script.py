import speedtest
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

def measure_internet_speed():
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1000000  # Convert to Mbps
        upload_speed = st.upload() / 1000000  # Convert to Mbps

        return download_speed, upload_speed
    except speedtest.ConfigRetrievalError as e:
        logging.error("Error: Failed to retrieve Speedtest configuration - %s", str(e))
        return None, None
    except speedtest.SpeedtestCLIError as e:
        logging.error("Error: Failed to execute Speedtest CLI - %s", str(e))
        return None, None
    except Exception as e:
        logging.error("Error: %s", str(e))
        return None, None

# Main script execution
download_speed, upload_speed = measure_internet_speed()

if download_speed is None or upload_speed is None:
    logging.error("Internet speed measurement failed.")
else:
    logging.info("Internet Speed:")
    logging.info("Download: {:.2f} Mbps".format(download_speed))
    logging.info("Upload: {:.2f} Mbps".format(upload_speed))
