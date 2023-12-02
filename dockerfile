# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Add Script
ADD Almaden_Internship_Eval.py /


# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org biopython



# Run script when the container launches
CMD ["python", "Almaden_Internship_Eval.py"]

