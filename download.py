import pdfkit

url = "https://www.coursera.org/learn/fundamentals-of-reinforcement-learning/assignment-submission/lMCZf/sequential-decision-making/view-feedback"  # Thay bằng trang web bạn cần lưu
pdfkit.from_url(url, "output.pdf")
