from config import DATA_FILE, REPORT_FILE
from data_handler import load_data, process_data
from report_generator import generate_report
from email_service import send_email
from logger import setup_logger, log_info

def main():
    setup_logger()
    log_info("Automation System Started")

    # Step 1: Load data
    data = load_data(DATA_FILE)
    if data is None:
        return

    # Step 2: Process data
    summary = process_data(data)
    if summary is None:
        return

    # Step 3: Generate report
    generate_report(summary, REPORT_FILE)

    # Step 4: Send email
    with open(REPORT_FILE, "r") as f:
        report_content = f.read()

    send_email(
        receiver_email="receiver@gmail.com",
        subject="Automated Business Report",
        body=report_content
    )

    log_info("Automation Completed Successfully")

if __name__ == "__main__":
    main()