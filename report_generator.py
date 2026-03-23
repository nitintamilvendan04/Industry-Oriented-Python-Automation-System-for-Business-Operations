from logger import log_info, log_error

def generate_report(summary, file_path):
    try:
        with open(file_path, "w") as f:
            f.write("Business Data Report\n")
            f.write("="*40 + "\n\n")
            f.write(str(summary))
        log_info("Report generated successfully")
    except Exception as e:
        log_error(f"Error generating report: {e}")