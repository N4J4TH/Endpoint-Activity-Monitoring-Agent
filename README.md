# Endpoint-Activity-Monitoring-Agent
The Endpoint Activity Monitoring Agent is a modular, Python-based telemetry collection framework designed to simulate core behaviors of modern Endpoint Detection &amp; Response (EDR) systems.
This project demonstrates real-time endpoint data collection, structured logging, and basic behavioral anomaly detection using a multi-threaded, object-oriented architecture.

The system is intended for controlled lab environments and cybersecurity research purposes.

## Key Capabilities
- Endpoint Telemetry Collection

- Keystroke monitoring

- Clipboard change detection

- Active window tracking

- Periodic screen capture

- Behavioral Detection

- Keystroke rate monitoring (>50 keys per second)

- Automatic alert generation

- Structured alert logging

- Structured Logging

- Local timestamp (human-readable)

- UTC timestamp (ISO 8601)

- Unix epoch timestamp

- CSV-based log output for easy analysis

## System Architecture

The application follows a modular Object-Oriented Programming (OOP) design with dedicated background threads for each monitoring function.

project/  
 │  
├── main.py  
├── loggingKeystrokes.py  
├── clipboardContent.py  
├── trackWindows.py  
├── screenshotTaker.py  
 │  
├── logs/  
│   ├── keystrokes.csv  
│   ├── clipboard.csv  
│   ├── windows.csv  
│   └── alerts.csv  
│  
└── screenshots/  

Each module runs independently using daemon threads, ensuring concurrent execution and continuous monitoring.

## Technical Highlights

- Python 3

- Object-Oriented Design

- Multi-threading

- Structured CSV Logging

- ISO 8601 Timestamping

- Behavioral Anomaly Detection Logic

- Automatic Directory Management

- Modular Codebase

## Logging Format

Each telemetry record includes normalized timestamps:

- Field	Description
- local_time	Local system time
- utc_time	ISO 8601 UTC time
- unix_time	Epoch timestamp
- activity_data	Event-specific data

Example:

    2026-03-01 15:48:12,2026-03-01T10:18:12Z,1772358327.7126455,a

This format mirrors structured event logging practices used in enterprise monitoring systems and SIEM platforms.

## Behavioral Detection Logic

The system implements a simple anomaly detection mechanism:

- Maintains a rolling 1-second window of keystroke timestamps

- Triggers alert if more than 5 keystrokes occur within that window

- Logs alert events to alerts.csv

This demonstrates foundational principles of:

- Automated activity detection

- Behavioral baselining

- Insider threat detection logic

- Scripted input monitoring concepts

## Installation

Install required dependencies:

     pip install pynput pyperclip pillow pygetwindow

Ensure appropriate system permissions are granted depending on operating system.

## Execution

Run from the project root directory:

     python main.py

Logs and screenshots will be automatically generated.

## Security & Ethical Notice

This project is intended strictly for:

- Cybersecurity education

- Lab experimentation

- Defensive research

- Authorized monitoring environments

Unauthorized monitoring of systems without explicit consent may violate legal and ethical standards.

## Potential Enhancements

Future development opportunities include:

- Encrypted log storage
- Log rotation and retention policies

- JSON-based structured logging

- SIEM integration simulation

- Centralized log aggregation

- Detection rule engine

- Visualization dashboard

- Network telemetry module

- Graceful shutdown handling

## Learning Outcomes Demonstrated

- Endpoint monitoring fundamentals

- Real-time telemetry collection

- Thread-based concurrency

- Behavioral anomaly detection

- Security-focused software architecture

- Structured logging practices

- Modular Python application design

## Author

Developed as part of cybersecurity practical research and applied lab development.
