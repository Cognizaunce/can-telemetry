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
