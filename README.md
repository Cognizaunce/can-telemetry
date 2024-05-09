# can-telemetry
General purpose CAN telemetry tool written in Python 3 

### Purpose of this Tool:

If any hardware runs CAN, this application should be able to simulate both the send and receive comms, down to the
capability of running _signals-based-unit-tests_.

### Project Structure
```graphql
can_tool/
│  
├── src/  
│   ├── main.py                   # Main entry point for the application  
│   ├── can_interface.py          # Module for handling CAN communication  
│   ├── db_manager.py             # Module for SQLite-based storage and logging  
│   ├── dbc_parser.py             # Module for DBC file parsing and message encoding/decoding  
│   ├── config_manager.py         # Module for managing configurations (TOML)  
│   └── gui/  
│       ├── main_window.py        # PyQt6 main window setup  
│       └── plot_widget.py        # Custom PyQt6 widget for plotting (Matplotlib)  
│  
├── configs/  
│   ├── example_config1.toml     # Example TOML configuration files  
│   └── example_config2.toml  
│  
├── dbc_files/  
│   ├── can_database.dbc         # DBC files for CAN message decoding  
│   └── other_dbc_file.dbc  
│  
├── data/                         # Directory for storing logged data of their respective types
│   └── ascii/                    # SQLite database for logging CAN messages  
│   └── csv/                      # SQLite database for logging CAN messages  
│   └── sqlite/                   # SQLite database for logging CAN messages  
│  
├── tests/                        # Directory for storing diagnostic test scripts  
│   ├── battery_voltage_test.py  
│   ├── throttle_percentage_test.py  
│   ├── can_bus_health_test.py  
│   ├── ecu_communication_test.py  
│   └── error_code_read_test.py  
│  
├── Dockerfile                   # Dockerfile for containerization  
├── requirements.txt             # Python dependencies  
└── README.md                    # Project documentation
```

### Example Diagnostic Tests (`tests/`):

- **battery_voltage_test.py**: A test to measure the battery voltage of the vehicle. This test could include steps to 
send a request for battery voltage measurement and then parse the response to extract the voltage value.

- **throttle_percentage_test.py**: A test to measure the throttle position percentage. This test could involve sending a
request for throttle position data and then decoding the response to calculate the throttle position percentage.

- **can_bus_health_test.py**: A test to check the health of the CAN bus. This test could involve sending a series of
test messages and checking for proper responses to ensure that the CAN bus is functioning correctly.

- **ecu_communication_test.py**: A test to verify communication with an Electronic Control Unit (ECU). This test could
involve sending a request for ECU identification data and then checking the response to ensure that it matches the
expected values.

- **error_code_read_test.py**: A test to read error codes from the vehicle's diagnostic system. This test could involve
sending a request for error code data and then parsing the response to extract the error codes.

These tests can be implemented as Python scripts that use your tool's CAN communication functionality to interact with
the vehicle's diagnostic system. They can be run manually or as part of an automated test suite to verify the
functionality of the vehicle's systems.

### What are Custom Dynamic Notifiers?
Custom dynamic notifiers are a way to manage and notify listeners of events or messages in a flexible and customizable
manner.
This logic is handled 

``` plantuml
@startuml
class CustomNotifier {
    - listeners: list[Callable[[Message], None]]
    - lock: threading.Lock()
    --
    + __init__(listeners: list[Callable[[Message], None]] | None = None)
    + add_listener(new_listener: Callable[[Message], None])
    + remove_listener(rem_listener: Callable[[Message], None])
    + notify_listeners(msg: Message)
    + simulate(messages: list[Message])
}

note right of CustomNotifier
    CustomNotifier is a class for managing
    dynamic listeners and notifying them
    of events or messages.
end note
@enduml
```